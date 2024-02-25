import requests
from bs4 import BeautifulSoup

def mahjanaResult(draw_no):

    url = "https://www.nlb.lk/results/mahajana-sampatha/"+str(draw_no)

    response = requests.get(url)

    if(response.status_code==200):
        soup = BeautifulSoup(response.content,'html5lib')

        if soup.find('li',class_='Letter Circle Blue bM'):
            letter = soup.find('li',class_='Letter Circle Blue bM').text
            numbers = [number.text for number in soup.find_all('li', class_='Number-1')if number.text.strip()]
            draw_info_ = soup.find('div',class_='lresult')
            draw_infos = [draw_info.text for draw_info in draw_info_.find_all('p')]

            # print("Lot Name:", lot_name)
            print("Draw Info:", draw_infos)
            print("Numbers:", numbers)
            print("Letter :",letter)
        else:
            print("Result not found in the site")
            print("Draw number :",draw_no)
    else:
        print("Error occourd",response.status_code)

def mahjanaResultGovDoc(draw_no):

    url = "https://results.govdoc.lk/results/mahajana-sampatha-"+str(draw_no)

    response = requests.get(url)

    if(response.status_code==200):
        soup = BeautifulSoup(response.content,'html5lib')

     
        letter = soup.find('div',class_='result-block letter').text
        numbers = [number.text for number in soup.find_all('div', class_='result-block number')if number.text.strip()]
        draw_info = soup.find('h1',class_='mb-0').text

        winning_letter_and_numbers = numbers
        winning_letter_and_numbers.insert(0,letter)

        # print("Lot Name:", lot_name)
        # print("Draw Info:", draw_info)
        # print("Numbers:", numbers)
        # print("Letter :",letter)
        
    else:
        winning_letter_and_numbers = []
        print("Error occured :",response.status_code)

    return winning_letter_and_numbers
    
def dhanaNidanayaResultGovDoc(draw_no):

    url = "https://results.govdoc.lk/results/dhana-nidhanaya-"+str(draw_no)

    response = requests.get(url)

    if(response.status_code==200):
        soup = BeautifulSoup(response.content,'html5lib')

     
        letter = soup.find('div',class_='result-block bonus1').text
        numbers = [number.text for number in soup.find_all('div', class_='result-block number')if number.text.strip()]
        draw_info = soup.find('h1',class_='mb-0').text

        winning_letter_and_numbers = numbers
        winning_letter_and_numbers.insert(0,letter)

        # print("Lot Name:", lot_name)
        # print("Draw Info:", draw_info)
        # print("Numbers:", numbers)
        # print("Letter :",letter)
        
    else:
        winning_letter_and_numbers = []
        print("Error occured :",response.status_code)

    return winning_letter_and_numbers

def govisethaResultGovDoc(draw_no):

    url = "https://results.govdoc.lk/results/govi-setha-"+str(draw_no)


    response = requests.get(url)

    if(response.status_code==200):
        soup = BeautifulSoup(response.content,'html5lib')

     
        letter = soup.find('div',class_='result-block bonus1').text
        numbers = [number.text for number in soup.find_all('div', class_='result-block number')if number.text.strip()]
        draw_info = soup.find('h1',class_='mb-0').text

        winning_letter_and_numbers = numbers
        winning_letter_and_numbers.insert(0,letter)

        # print("Lot Name:", lot_name)
        # print("Draw Info:", draw_info)
        # print("Numbers:", numbers)
        # print("Letter :",letter)
        
    else:
        winning_letter_and_numbers = []
        print("Error occured :",response.status_code)

    return winning_letter_and_numbers

