import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import re
from pytesseract import Output

def correct_angle(image, verbose=False):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    angle = -(90 + angle) if angle < -45 else -angle
    
    h, w = image.shape[:2]
    (c_x, c_y) = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D((c_x, c_y), angle, 1.0)
    
    cos = np.abs(matrix[0, 0])
    sin = np.abs(matrix[0, 1])
    
    n_w = int((h * sin) + (w * cos))
    n_h = int((h * cos) + (w * sin))
    
    matrix[0, 2] += (n_w / 2) - c_x
    matrix[1, 2] += (n_h / 2) - c_y
    
    return cv2.warpAffine(image, matrix, (n_w, n_h), borderValue=(255, 255, 255))

def detect_flip(image, verbose=False):
    mask = np.zeros(image.shape, dtype=np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    adaptive = cv2.adaptiveThreshold(
        blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,15,4
    )

    cnts = cv2.findContours(adaptive, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        area = cv2.contourArea(c)
        if area < 45000 and area > 20:
            cv2.drawContours(mask, [c], -1, (255,255,255), -1)
            # plt.imshow(cv2.cvtColor(mask,cv2.COLOR_BGR2RGB))
            # plt.show()
            
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    h, w = mask.shape
    
    if verbose:
        fig, ax = plt.subplots(1,3, figsize=(20, 20))
        ax[0].imshow(image)
        ax[0].set_title('Original', fontsize=12)
        ax[0].axis('off')
        ax[1].imshow(adaptive, cmap='gray')
        ax[1].set_title('Thresholded', fontsize=12)
        ax[1].axis('off')
        ax[2].imshow(mask, cmap='gray')
        ax[2].set_title('Mask', fontsize=12)
        ax[2].axis('off')
        plt.show()
    
    
    left = mask[0:h, 0:0+w//2]
    right = mask[0:h, w//2:]
    left_pixels = cv2.countNonZero(left)
    right_pixels = cv2.countNonZero(right)
    print(left_pixels,right_pixels)
    return 0 if left_pixels >= right_pixels else 180


# doc_200 = cv2.imread("rotated image.png",1)
# corrected_image = correct_angle(doc_200, True)
# plt.imshow(corrected_image)
# plt.show()

# doc_180 = corrected_image
# angle = detect_flip(doc_180, True)
# print(angle)
# corrected_image = Image.fromarray(corrected_image).rotate(angle)
# corrected_image



#----------chatgpt

def get_rotation_angle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)


    plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
    plt.show()
    

    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            angle_deg = theta * 180 / np.pi
            if angle_deg > 45:  # Avoid nearly horizontal lines
                return 90 - angle_deg
    return 0  # No significant rotation detected

image = cv2.imread("Resource\Images\IMG_20230826_103214.jpg",1)
# rotation_angle = get_rotation_angle(image)
# print(rotation_angle)

#--------use tesract


# osd = pytesseract.image_to_osd(image)
# angle = re.search('(?<=Rotate: )\d+', osd).group(0)
# script = re.search('(?<=Script: )\d+', osd).group(0)
# print("angle: ", angle)
# print("script: ", script)

# import pytesseract
# import re
# from PIL import Image


# Perform OCR to get OSD information
osd = pytesseract.image_to_osd(image)

# Extract rotation angle and script using regular expressions
angle_match = re.search(r'(?<=Rotate: )\d+', osd)
script_match = re.search(r'(?<=Script: )\d+', osd)

if angle_match:
    angle = int(angle_match.group(0))
    print("angle:", angle)
else:
    print("Angle not found in OSD")

if script_match:
    script = int(script_match.group(0))
    print("script:", script)
else:
    print("Script not found in OSD")
