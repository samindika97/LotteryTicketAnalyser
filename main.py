import preprocess
import os
import matplotlib.pyplot as plt
import cv2
import get_ticket_type
import get_from_internet
import getWinningPrice
import numpy as np

valid_formats = [".jpg", ".jpeg", ".png"]
get_text = lambda f: os.path.splitext(f)[1].lower()
paths = ["Shanida","Kapruka","Mahajana","Dhana Nidhanaya","Govisetha","Kotipathi"]

path = 5

# img_files = ['images/' + f for f in os.listdir('images') if get_text(f) in valid_formats]
img_files = ['Resource/Images/'+ paths[path] +'/' + f for f in os.listdir('Resource/Images/'+ paths[path] +'/') if get_text(f) in valid_formats]


def runAllImage(limit):
     # go through each image file
	i=1
	for img_file in img_files:												
		if(i>limit) :									#break in 5 times	
			break
		print(str(i) + " : " + img_file)
		imageColour = cv2.imread(img_file,1)
		runImage(imageColour)		
		i+=1



def runSingleFile(path):
	imageColour = cv2.imread(path,1)
	runImage(imageColour)

def runFrom(start,end):
	for i in range(start,end):
		img_file = img_files[i-1]
		imageColour = cv2.imread(img_file,1)
		runImage(imageColour)
			
def runImage(imageColour):
		warped = preprocess.enhanceImage(originalColorImage=imageColour,showEged=False)
		forGraph = np.zeros((1600,4000),np.uint8)
		
		ticketType,ocrText = get_ticket_type.findByEasyOCR(warped)
		if ticketType!=-1:
			your_letter_and_numbers,draw_no = preprocess.extractData(ticketType,warped,ocrText)
			drawDetails = "ticket type is :"+ ticketType+"    Draw num:"+ str(draw_no)
			print(drawDetails)
			yourData = "Your letter & number :" + str(your_letter_and_numbers)
			print(yourData)
			winning_letter_and_numbers = get_from_internet.getWinnigNumbers(ticketType,draw_no)
			winingData = "Winning letter & number :" + str(winning_letter_and_numbers)
			print(winingData)
			if len(your_letter_and_numbers)!=0 and len(winning_letter_and_numbers)!= 0 :
				result = getWinningPrice.getPrize(ticketType,your_letter_and_numbers,winning_letter_and_numbers)
				print(result)
				if(warped.any()):
					width = 500
					height = 1000

					plt.subplot(1,3,1)
					plt.xticks([]), plt.yticks([])
					plt.imshow(cv2.cvtColor(imageColour,cv2.COLOR_BGR2RGB))
					# plt.title("Image :" + str(i))
					plt.subplot(1,3,2)
					plt.xticks([]), plt.yticks([])
					plt.imshow(cv2.cvtColor(warped,cv2.COLOR_BGR2RGB))
					# plt.title("Localized :",ticketType)
					plt.subplot(1,3,3)
					plt.xticks([]), plt.yticks([])
					plt.text(50,300,drawDetails,fontsize=10,c='yellow')
					plt.text(50,600,yourData,fontsize=10,c='yellow')
					plt.text(50,1000,winingData,fontsize=10,c='yellow')
					plt.text(50,1500,result,fontsize=10,c='yellow')
					plt.imshow(forGraph,'gray')
					# plt.figure(figsize=(width, height))
					plt.show()
					# plt.axis('off')
					# plt.show(block=False)
					# plt.pause(10)  # Adjust the pause time as needed (3 seconds in this case) 
					# plt.close()
			else:
				print("Looks like image is blured Winning  numbers or Your numbers are not found")
		else:
			print(ocrText)



# runSingleFile(r"images\1694094016106.jpg")
runAllImage(limit=40)
# runFrom(5,40)



