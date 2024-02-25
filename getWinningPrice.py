from collections import Counter

def getPrize(ticketType, yourNumbers, winningNumbers):
    if(ticketType == "Shanida"):
        return shanidaPrize(yourNumbers,winningNumbers)
    if(ticketType == "Govisetha"):
        return govisethaPrize(yourNumbers,winningNumbers)
    if(ticketType == "KAPRUKA"):
        return kaprukaPrize(yourNumbers,winningNumbers)
    if(ticketType == "Dhana"):
        return dhanaPrize(yourNumbers,winningNumbers)
    if(ticketType == "SAMPATHA"):
        return mahajanaPrize(yourNumbers,winningNumbers)
    if(ticketType == "KOTIPATHI"):
        return kotipathiPrize(yourNumbers,winningNumbers)

def shanidaPrize(your_letter_and_numbers,winning_letter_and_numbers):

    yourNumbers = your_letter_and_numbers[1:]
    winningNumbers = winning_letter_and_numbers[1:]

    counter1 = Counter(yourNumbers)
    counter2 = Counter(winningNumbers)
    common_elements = list((counter1 & counter2).elements())

    number_of_common = len(common_elements)
    
    if your_letter_and_numbers[0] != winning_letter_and_numbers[0]:
        if(number_of_common == 0):
            return("No winning prize")
        elif(number_of_common == 1):
            return("you won Rs-20")
        elif(number_of_common == 2):
            return("you won Rs-100")
        elif(number_of_common == 3):
            return("you won Rs-2000")
        elif(number_of_common == 4):
            return("you won Rs-1,000,000")
    else:
        if(number_of_common == 0):
            return("you won Rs-20")
        elif(number_of_common == 1):
            return("you won Rs-100")
        elif(number_of_common == 2):
            return("you won Rs-1000")
        elif(number_of_common == 3):
            return("you won Rs-100,000")
        elif(number_of_common == 4):
            return("you won Rs-30,000,000")

def govisethaPrize(your_letter_and_numbers,winning_letter_and_numbers):

    yourNumbers = your_letter_and_numbers[1:]
    winningNumbers = winning_letter_and_numbers[1:]

    counter1 = Counter(yourNumbers)
    counter2 = Counter(winningNumbers)
    common_elements = list((counter1 & counter2).elements())

    number_of_common = len(common_elements)
    
    if your_letter_and_numbers[0] != winning_letter_and_numbers[0]:
        if(number_of_common == 0):
            return("No winning prize")
        elif(number_of_common == 1):
            return("you won Rs-20")
        elif(number_of_common == 2):
            return("you won Rs-100")
        elif(number_of_common == 3):
            return("you won Rs-2000")
        elif(number_of_common == 4):
            return("you won Rs-1,000,000")
    else:
        if(number_of_common == 0):
            return("you won Rs-20")
        elif(number_of_common == 1):
            return("you won Rs-100")
        elif(number_of_common == 2):
            return("you won Rs-1000")
        elif(number_of_common == 3):
            return("you won Rs-100,000")
        elif(number_of_common == 4):
            return("you won Rs-60,000,000")


def kaprukaPrize(your_letter_and_numbers,winning_letter_and_numbers):

    yourNumbers = your_letter_and_numbers[1:]
    winningNumbers = winning_letter_and_numbers[1:]

    counter1 = Counter(yourNumbers)
    counter2 = Counter(winningNumbers)
    common_elements = list((counter1 & counter2).elements())

    number_of_common = len(common_elements)
    
    if your_letter_and_numbers[0] != winning_letter_and_numbers[0]:
        if(number_of_common == 0):
            return("No winning prize")
        elif(number_of_common == 1):
            return("you won Rs-20")
        elif(number_of_common == 2):
            return("you won Rs-100")
        elif(number_of_common == 3):
            return("you won Rs-2000")
        elif(number_of_common == 4):
            return("you won Rs-1,000,000")
    else:
        if(number_of_common == 0):
            return("you won Rs-20")
        elif(number_of_common == 1):
            return("you won Rs-60")
        elif(number_of_common == 2):
            return("you won Rs-1000")
        elif(number_of_common == 3):
            return("you won Rs-100,000")
        elif(number_of_common == 4):
            return("you won Rs-75,000,000")

def dhanaPrize(your_letter_and_numbers,winning_letter_and_numbers):

    yourNumbers = your_letter_and_numbers[1:]
    winningNumbers = winning_letter_and_numbers[1:]

    counter1 = Counter(yourNumbers)
    counter2 = Counter(winningNumbers)
    common_elements = list((counter1 & counter2).elements())

    number_of_common = len(common_elements)
    
    if your_letter_and_numbers[0] != winning_letter_and_numbers[0]:
        if(number_of_common == 0):
            return("No winning prize")
        elif(number_of_common == 1):
            return("you won Rs-20")
        elif(number_of_common == 2):
            return("you won Rs-100")
        elif(number_of_common == 3):
            return("you won Rs-3000")
        elif(number_of_common == 4):
            return("you won Rs-1,000,000")
    else:
        if(number_of_common == 0):
            return("you won Rs-20")
        elif(number_of_common == 1):
            return("you won Rs-60")
        elif(number_of_common == 2):
            return("you won Rs-1000")
        elif(number_of_common == 3):
            return("you won Rs-100,000")
        elif(number_of_common == 4):
            return("you won Rs-80,000,000")

def mahajanaPrize(your_letter_and_numbers,winning_letter_and_numbers):

    reverse = 0
    reverse_price = 0
    for i in range(6,-1,-1):
        if your_letter_and_numbers[i] != winning_letter_and_numbers[i]:
            break
        else:
            reverse+=1

    if(reverse == 0):
        reverse_price = 0
    if reverse == 1:
        reverse_price = 20
    elif reverse == 2:
        reverse_price = 100
    elif reverse == 3:
        reverse_price = 1000
    elif reverse == 4:
        reverse_price = 10000
    elif reverse == 5:
        reverse_price = 100000
    elif reverse == 6:
        reverse_price = 2000000
    elif reverse == 7:
        reverse_price = 10000000


    font = 0
    font_price = 0 
    for i in range (1,6):
        if your_letter_and_numbers[i] != winning_letter_and_numbers[i]:
            break
        else:
            font+=1
    
    if font == 0:
        font_price = 0  # No winning prize
    elif font == 1:
        font_price = 0  # No winning prize
    elif font == 2:
        font_price = 50
    elif font == 3:
        font_price = 100
    elif font == 4:
        font_price = 1000
    elif font == 5:
        font_price = 100000

    letter_price = 0
    if your_letter_and_numbers[0] == winning_letter_and_numbers[0]:
        letter_price = 20

    maximum_price = max(font_price,reverse_price,letter_price)

    return("You won Rs:",maximum_price)    


def kotipathiPrize(your_letter_and_numbers,winning_letter_and_numbers):

    yourNumbers = your_letter_and_numbers[1:]
    winningNumbers = winning_letter_and_numbers[1:]

    counter1 = Counter(yourNumbers)
    counter2 = Counter(winningNumbers)
    common_elements = list((counter1 & counter2).elements())

    number_of_common = len(common_elements)
    
    if your_letter_and_numbers[0] != winning_letter_and_numbers[0]:
        if(number_of_common == 0):
            return("No winning prize")
        elif(number_of_common == 1):
            return("you won Rs-20")
        elif(number_of_common == 2):
            return("you won Rs-100")
        elif(number_of_common == 3):
            return("you won Rs-2000")
        elif(number_of_common == 4):
            return("you won Rs-1,000,000")
    else:
        if(number_of_common == 0):
            return("you won Rs-20")
        elif(number_of_common == 1):
            return("you won Rs-100")
        elif(number_of_common == 2):
            return("you won Rs-1000")
        elif(number_of_common == 3):
            return("you won Rs-100,000")
        elif(number_of_common == 4):
            return("you won Rs-50,000,000")
