import re

def separateNumLatter(result_text):
	
	letter = re.findall("[A-Za-z]",result_text)
	numbers = re.findall("\d{2}",result_text)
	result = letter+numbers
	print(result)
	



result_string = "OBa,X912S,0c,IA,952),@wmom,Shanida,24,B53) &0r 6Oa) 0dojod,23],d),JDo3),Oigugnghdo @slmeomdo,E,11 19 46 70,EEE,ELVN,NINTN,FORST,SVNTY,8p0 4a0,8o@ 0voo,Liocouy,2021/07/23,Qoupopf)   ourpto ,3652,3652,246329570,1,07,7,Booba) 001a0Aca,RS,20:,Oialuss 0es 4oe,65080,6,La"
number_pattern = r"\b3[6-7][2-8][1-9]\b"


# answer = re.findall(number_pattern,result_string)
# print(answer)

separateNumLatter('A,03,23,28,36,')