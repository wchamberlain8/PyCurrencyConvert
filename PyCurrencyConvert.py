import requests
import time
import os

#'https://v6.exchangerate-api.com/v6/80c772aad2e7ff37519f5ec5/latest/CURRENCY_CODE' #API key


def getConversionRate(userCurrency, targetCurrency):
    url = f'https://v6.exchangerate-api.com/v6/80c772aad2e7ff37519f5ec5/latest/{userCurrency}' #API key

    response = requests.get(url) #http get request
    data = response.json()

    if targetCurrency in data['conversion_rates']:
        return data['conversion_rates'][targetCurrency]
    else:
        print(f"Error: {targetCurrency} is not available in the API")
        return None


def customConversion():

    userCurrency = input("Enter currency you wish to convert: ").upper
    value = float(input("Enter the amount of money: "))
    targetCurrency = input("Enter desired currency: ").upper

    conversionRate = getConversionRate(userCurrency, targetCurrency)

    if conversionRate:
        newValue = value * conversionRate
        print(f"{value} {userCurrency} is equivalent to {newValue} {targetCurrency}")

    



def menu():
    print ("---------------------------------------")
    print("| PyCurrencyConvert                   |")
    print ("|-------------------------------------|")
    print("| 1) Convert custom currency          |")
    print("| 2) Preview supported currency codes |")
    print ("|-------------------------------------|")
    print("| 3) Quick convert GBP                |")
    print("| 4) Quick convert USD                |")
    print("| 5) Quick convert EUR                |")
    print ("|-------------------------------------|")
    print("| 6) Help menu                        |")
    print("| 7) Exit                             |")
    print ("---------------------------------------")

def menuInput():
    while True:
        userInput = input("Please enter your selection [1-7]: ")

        if userInput == '1':
            os.system('cls')
            customConversion()
            return
        elif userInput == '2':
            # function call
            return
        elif userInput == '3':
            # function call
            return
        elif userInput == '4':
            # function call
            return
        elif userInput == '5':
            # function call
            return
        elif userInput == '6':
            # function call
            return
        elif userInput == '7':
            print("Exiting...")
            time.sleep(1)
            exit()
        else:
            print("Invalid choice, try again")

menu()
menuInput()