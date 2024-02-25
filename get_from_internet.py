import requests
from bs4 import BeautifulSoup
import getFromDLB
import getFromNLB

def getWinnigNumbers(ticketType,draw_no):
    if ticketType == "Shanida" or ticketType == "KAPRUKA" or ticketType == "KOTIPATHI":
        winning_letter_and_numbers = getFromDLB.getResult(ticketType,draw_no)
        return winning_letter_and_numbers
    elif ticketType == "SAMPATHA":
        winning_letter_and_numbers = getFromNLB.mahjanaResultGovDoc(draw_no)
        return winning_letter_and_numbers
    elif ticketType == "Dhana":
        winning_letter_and_numbers = getFromNLB.dhanaNidanayaResultGovDoc(draw_no)
        return winning_letter_and_numbers
    elif ticketType == "Govisetha":
        winning_letter_and_numbers = getFromNLB.govisethaResultGovDoc(draw_no)
        return winning_letter_and_numbers
                
        
def getFromLankaResults(ticketType, results):
    
    URL = "https://lankaresults.com/lottery-results/ada-kotipathi/1930"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content,'html5lib')
    # print(soup.prettify())

    table = soup.find_all(class_='text-center')         #list of BeautifulSoup Tag objects.
    print(table)

    for ele in table:
        letter = ele.find(class_='letter')
        numbers = ele.find_all(class_='dot')
        
        # Check if the 'letter' element exists before accessing its text.
        if letter:
            print("Letter:", letter.text)
        
        # Check if there are any 'dot' elements before accessing their text.
        if numbers:
            for number in numbers:
                print("Dot Number:", number.text)


    
