import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
import easyocr

def template_matching(imageColor):

    template = cv2.imread(r"templates\govisetha_logo.jpg",1)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template_image = cv2.Canny(template, 0, 200)
    (template_h, template_w) = template.shape[:2]

    image_copy = imageColor.copy()
    input_image = cv2.cvtColor(imageColor,cv2.COLOR_BGR2GRAY)

    result_ssd = cv2.matchTemplate(input_image, template_image, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_ssd)
    top_left = min_loc
    bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])

    # Draw a rectangle around the matched region
    cv2.rectangle(input_image, top_left, bottom_right, 255, 2)

    result_cc = cv2.matchTemplate(input_image, template_image, cv2.TM_CCORR)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_cc)
    top_left = max_loc
    bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])

    # Draw a rectangle around the matched region
    cv2.rectangle(input_image, top_left, bottom_right, 255, 2)

    cv2.imshow('Input Image', input_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#equalise histogram
def equalise(image):
    return cv2.equalizeHist(image)

def cvtRGB(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


def ticket_type_by_ocr(image):
    plt.imshow(image)
    plt.show()

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = thresholding(gray)
    inverse = cv2.bitwise_not(thresh)
    open = opening(gray)
    edged = cv2.Canny(image, 100, 200)
    
    plt.subplot(1,5,1)
    plt.imshow(cvtRGB(image))
    plt.subplot(1,5,2)
    plt.imshow(gray,'gray')
    plt.subplot(1,5,3)
    plt.imshow(cvtRGB(thresh))
    plt.subplot(1,5,4)
    plt.imshow(cvtRGB(open))
    plt.subplot(1,5,5)
    plt.imshow(cvtRGB(edged))
    plt.show()

    text = pytesseract.image_to_string(image)
    print("Extracted Text from original:", text)
    print("-----------------")    
    getBoxes(img=image)

    text = pytesseract.image_to_string(gray)
    print("Extracted Text From gray:", text)
    print("-----------------")    
    getBoxes(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))

    text = pytesseract.image_to_string(inverse)
    print("Extracted Text from thresh:", text)
    print("-----------------")    
    getBoxes( cv2.cvtColor(inverse, cv2.COLOR_GRAY2BGR))

    text = pytesseract.image_to_string(open)
    print("Extracted Text from open:", text)
    print("-----------------")    
    getBoxes(cv2.cvtColor(open, cv2.COLOR_GRAY2BGR))

    text = pytesseract.image_to_string(edged)
    print("Extracted Text from edged:", text)
    print("-----------------")    
    getBoxes(cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR))


def getBoxes(img):
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img) 
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    imS = cv2.resize(img, (540, 960))
    cv2.imshow('img', imS)
    cv2.waitKey(0)


def ticketTypeTopPart(image):
    h,w,c = image.shape
    top = image[0:2*h//3,0:w]

    plt.imshow(top)
    plt.show(block=False)
    plt.pause(3)  # Adjust the pause time as needed (3 seconds in this case)
    plt.close()

    text = pytesseract.image_to_string(top)
    print(text)
    if(text.find("Shanida")!=-1):
        result = "Ticket is shanida"
    # elif    
    else:
        result = "NOT shanida"
    return result


def findByEasyOCR(image):
    tickets = ["Shanida","KAPRUKA","SAMPATHA","Dhana","Govisetha","KOTIPATHI"]

    reader = easyocr.Reader(['en'],gpu=True)
    result = reader.readtext(image,detail = 0)
    print(result)
    for ticket in tickets:
        for text in result:
            if ticket in text:
                return ticket,result 
        
    return -1,result