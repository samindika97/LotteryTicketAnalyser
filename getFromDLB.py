from bs4 import BeautifulSoup
from pprint import pprint
import requests


def getResult(ticketType,drawNo):

    lot_ids = {"Shanida" : 1,"KAPRUKA":12, "KOTIPATHI":11}

    url = "https://www.dlb.lk/lottery/popup"

    payload = {
        'datepicker2': '',
        'drawNo': drawNo,
        'lot_id': lot_ids[ticketType],
        'lastsegment': 'en'
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the parsed HTML
        lot_name = soup.find('h2', class_='lot_m_re_heading').text
        draw_info = soup.find('h3', class_='lot_m_re_date').text

        # # Extracting the list of numbers
        numbers = [number.text for number in soup.find_all('h6', class_='number_shanida number_circle')if number.text.strip()]
        letter = soup.find('h6',class_='eng_letter').text
        

        # Print or use the extracted data as needed

        winning_letter_and_numbers = numbers
        winning_letter_and_numbers.insert(0,letter)

        return winning_letter_and_numbers
        print(winning_letter_and_numbers)
        print("Lot Name:", lot_name)
        print("Draw Info:", draw_info)
        print("Numbers:", numbers)
        print("Letter :",letter)


    else :
        winning_letter_and_numbers = []
        print("Error occured :",response.status_code)


getResult("Shanida",3786)