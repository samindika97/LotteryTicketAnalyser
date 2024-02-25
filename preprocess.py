import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import get_ticket_type
import easyocr
import re

def enhanceImage(originalColorImage,showEged):									#first image comes to this and make edged image send it to getCountiurs
    gray = cv2.cvtColor(originalColorImage,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)  #pre = 11,13
    edged = cv2.Canny(gray, 0, 40)   	#prev =80,70,60
    dilatedEdge = cv2.dilate(edged, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (69,69)))  #prev = 69
    if showEged == True:
        plt.subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
        
        plt.subplot(1, 3, 2)
        plt.imshow(cv2.cvtColor(dilatedEdge, cv2.COLOR_BGR2RGB))
        
        plt.subplot(1, 3, 3)
        plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
        
        plt.show()

    warped = getContours(dilatedEdge,originalColorImage)
    return warped


def getContours(edgedImage,originalColorImage):    
    contours, _ = cv2.findContours(edgedImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    doc_cnts = []
    # cv2.drawContours(originalColorImage,contours, -1,(0,255,255) , 40)
    # plt.imshow(cv2.cvtColor(originalColorImage,cv2.COLOR_BGR2RGB))
    # plt.show()

    for contour in contours:
        # we approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.1 * peri, True) 
        
        # if we found a contour with 4 points we break the for loop
        # (we can assume that we have found our document) and 
        #  draw countour around the original image
        if len(approx) == 4:
            doc_cnts = approx
            # cv2.drawContours(originalColorImage, [doc_cnts], -1,(0,255,255) , 40)
            # plt.imshow(cv2.cvtColor(originalColorImage,cv2.COLOR_BGR2RGB))
            # plt.show()

            reshaped_doc_cnts = np.reshape(doc_cnts, (4, 2))

            #Send counour data and image to fourpointtranform fuction to get transformed image
            warped = four_point_transform(originalColorImage,reshaped_doc_cnts)

            return warped

def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
        
	return rect


def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
        
    #showing the wraped image and original image side by side
	# plt.subplot(1,2,1)
	# plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
	# plt.title("original")
	# plt.subplot(1,2,2)
	# plt.imshow(cv2.cvtColor(warped,cv2.COLOR_BGR2RGB))
	# plt.title("transformed")
	# plt.show()

	# return the warped image
	return warped


def separateNumLatter(result_text):	
	letter = re.findall("[A-Za-z]",result_text)
	numbers = re.findall("\d{2}",result_text)
	result = letter+numbers
	return(result)


def KOTIPATHI_KAPRUKA(image,result):
	result_string = ','.join(result)
	# print(result_string)
	number_pattern = r'[A-Za-z][ ,]\d{2}[ ,]\d{2}[ ,]\d{2}[ ,]\d{2}'
	draw_no_pattern = r'\b7[1-9][1-9]\b'

	draw_no = re.findall(draw_no_pattern,result_string)
	letter_and_numbers = re.findall(number_pattern,result_string)
	if len(letter_and_numbers) != 0:
		letter_and_numbers = separateNumLatter(letter_and_numbers[0])
	else:
		print("empty",result_string)
			
	return letter_and_numbers,draw_no[-1]


def MAHAJANA_SAMPATHA(result):

	result_string = ','.join(result)
	# print(result_string)
	number_pattern = r'[A-Za-z][ ,]\d{1} \d{1} \d{1} \d{1} \d{1} \d{1}'
	draw_no_pattern = r'\b4[2-6][0-9][0-9]\b'

	draw_no = re.findall(draw_no_pattern,result_string)
	letter_and_numbers = re.findall(number_pattern,result_string)
	if len(letter_and_numbers) != 0:
		letter = re.findall("[A-Za-z]",letter_and_numbers[0])
		numbers = re.findall("\d{1}",letter_and_numbers[0])
		letter_and_numbers = letter+numbers
	else:
		print("Empty :",result_string)

	return letter_and_numbers,draw_no[-1]

def Shanida(image,result):

	result_string = ','.join(result)
	# print(result_string)
	number_pattern = r'[A-Za-z][ ,]\d{2}[ ,]\d{2}[ ,]\d{2}[ ,]\d{2}[ ,]'
	draw_no_pattern = r'\b3[6-7][2-8][1-9]\b'

	draw_no = re.findall(draw_no_pattern,result_string)
	letter_and_numbers = re.findall(number_pattern,result_string)
	letter_and_numbers = separateNumLatter(letter_and_numbers[0])
	return letter_and_numbers,draw_no[-1]



def Dhana_Nidhanaya(result):

	result_string = ','.join(result)
	# print(result_string)

	number_pattern = r"[A-Z],\d{2} *,*\d{2} *,*\d{2} *,*\d{2}"
	draw_no_pattern = r'\b0[5-6][0-9][0-9]\b'

	draw_no = re.findall(draw_no_pattern,result_string)[0]
	draw_no = draw_no[1:]
	letter_and_numbers = re.findall(number_pattern,result_string)
	if len(letter_and_numbers) != 0:
		letter_and_numbers = separateNumLatter(letter_and_numbers[0])
	else:
		print("Empty :",result_string)

	return letter_and_numbers,draw_no

def Govisetha(result):

	result_string = ','.join(result)

	number_pattern = r"[A-Za-z][ *,*]\d{2}[ *,*]\d{2}[ *,*]\d{2}[ *,*]\d{2}"
	draw_no_pattern = r'\b2[1-9][0-9][0-9]\b'

	draw_no = re.findall(draw_no_pattern,result_string)[0]
	letter_and_numbers = re.findall(number_pattern,result_string)
	if len(letter_and_numbers) != 0:
		letter_and_numbers = separateNumLatter(letter_and_numbers[0])
	else:
		print("Empty :",result_string)

	return letter_and_numbers,draw_no


def KOTIPATHI(image,result):
	h,w,c = image.shape
	top = image[h//2:3*h//4,0:w]
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	gray = get_ticket_type.opening(gray)

	reader = easyocr.Reader(['en'],gpu=True)
	result = reader.readtext(gray,detail = 0)

	result_string = ','.join(result)

	# print(result)

	number_pattern = r"[A-Za-z][ *,*]\d{2}[ *,*]\d{2}[ *,*]\d{2}[ *,*]\d{2}"
	draw_no_pattern = r'\b1[0-9][0-9][0-9]\b'

	draw_no = re.findall(draw_no_pattern,result_string)
	letter_and_numbers = re.findall(number_pattern,result_string)
	if len(letter_and_numbers) != 0:
		letter_and_numbers = separateNumLatter(letter_and_numbers[0])
	else:
		print("Empty :",result_string)

	return letter_and_numbers,draw_no[+1]


def extractData(ticketType,warped,ocrText):
	if(ticketType=='Shanida'):
			letter_and_numbers,draw_no = Shanida(warped,ocrText)
			return letter_and_numbers,draw_no 
	elif(ticketType=='KAPRUKA'):
			letter_and_numbers,draw_no = KOTIPATHI_KAPRUKA(warped,ocrText)
			return letter_and_numbers,draw_no
	elif(ticketType=="SAMPATHA"):
			letter_and_numbers,draw_no = MAHAJANA_SAMPATHA(ocrText)
			return letter_and_numbers,draw_no
	elif(ticketType=="Dhana"):
			letter_and_numbers,draw_no = Dhana_Nidhanaya(ocrText)
			return letter_and_numbers,draw_no
	elif(ticketType=="Govisetha"):
			letter_and_numbers,draw_no = Govisetha(ocrText)
			return letter_and_numbers,draw_no
	elif(ticketType=="KOTIPATHI"):
			letter_and_numbers,draw_no = KOTIPATHI(warped,ocrText)
			return letter_and_numbers,draw_no
	else:
		letter_and_numbers = []
		draw_no = 0
		print("Unidentified : ",ocrText)
		return letter_and_numbers,draw_no

