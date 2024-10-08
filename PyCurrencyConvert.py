import requests
import time
import os
from CurrencyCodes import codeDictionary

#'https://v6.exchangerate-api.com/v6/80c772aad2e7ff37519f5ec5/latest/CURRENCY_CODE' #API key

ITEMS_PER_PAGE = 20

def displayPage(codeDictionary, pageNum):

    startIndex = (pageNum - 1) * ITEMS_PER_PAGE
    endIndex = startIndex + ITEMS_PER_PAGE

    sortedCodeDictionary = dict(sorted(codeDictionary.items(), key=lambda item: item[1]))
    items = list(sortedCodeDictionary.items())[startIndex:endIndex]

    print(f"Currency Code Guide - Page {pageNum}/{(len(codeDictionary) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE}")
    print("----------------------------------------")
    
    for code, description in items:
        print(f"{code}: {description}")
    
    print("----------------------------------------")
    print(f"Showing {startIndex + 1} to {min(endIndex, len(codeDictionary))} of {len(codeDictionary)} currencies")
    print("Enter 'n' for next page, 'p' for previous page, 'q' to quit.")



def currencyCodePages():
    pageNum = 1
    total_pages = (len(codeDictionary) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    while True:
        displayPage(codeDictionary, pageNum)
        userInput = input("Enter your choice: ").lower()

        if userInput == 'n' and pageNum < total_pages:
            os.system("cls")
            pageNum += 1
        elif userInput == 'p' and pageNum > 1:
            os.system("cls")
            pageNum -= 1
        elif userInput == 'q':
            os.system("cls")
            break
        else:
            os.system("cls")
            print("\n*** Invalid input. Enter 'n' (next), 'p' (previous), or 'q' (quit) ***\n")



def errorCodes(code):
    if code == 'unsupported-code':
        print("\n*** ERROR: The base code entered in not available in the API ***")
        print("*** Refer to the currency code in the main menu for more information ***\n")
    if code == 'malformed-request':
        print("\n*** ERROR: Request did not follow the valid API structure ***\n")
    elif code == 'invalid-key':
        print("\n*** ERROR: The API key is invalid ***\n")
    elif code == 'quota-reached':
        print("\n*** ERROR: Account has reached the number of requests allowed by your plan ***\n")



def getConversionRate(baseCurrency, targetCurrency):
    url = f'https://v6.exchangerate-api.com/v6/80c772aad2e7ff37519f5ec5/latest/{baseCurrency}' #API key

    response = requests.get(url) #http get request
    data = response.json()

    if data.get('result') == 'error':
        errorCode = data.get('error-type')
        errorCodes(errorCode)
        return None
    else:     
        if targetCurrency in data['conversion_rates']:
            return data['conversion_rates'][targetCurrency]
        else:
            print(f"*** ERROR: {targetCurrency} is not available in the API ***")
            return None



def printConversion(conversionRate, baseCurrency, targetCurrency, value):
    newValue = round(value * conversionRate, 2)
    message = f"{value} {baseCurrency} is equivalent to {newValue} {targetCurrency}"
    borderLength = len(message) + 4
    print("\n")
    print("-" * borderLength)
    print(f"* {message} *")
    print("-" * borderLength)



def customConversion():

    print("--------------------------------------------------------")
    print("|                  Custom Conversion                   |")
    print("--------------------------------------------------------")
    baseCurrency = input("Enter currency you wish to convert (e.g. GBP, EUR): ").upper()

    while True:
        try:
            value = float(input("Enter the amount of money: "))
            break
        except ValueError:
            print("*** ERROR: Invalid input. Please enter a valid numerical value. ***")

    targetCurrency = input("Enter desired currency (e.g. USD, JPY): ").upper()



    conversionRate = getConversionRate(baseCurrency, targetCurrency)

    if conversionRate:
        printConversion(conversionRate, baseCurrency, targetCurrency, value)

    while True:
        print("\n1) Convert a different amount")
        print(f"2) Change base currency (currently {baseCurrency})")
        print(f"3) Change target currency (currently {targetCurrency})")
        print("4) Exit to main menu")

        userInput = input("Enter your selection [1-4]: ")

        if userInput == "1":
            while True:
                try:
                    value = float(input("Enter the amount of money: "))
                    break
                except ValueError:
                    print("*** ERROR: Invalid input. Please enter a valid numerical value. ***")

            conversionRate = getConversionRate(baseCurrency, targetCurrency)
            
            if conversionRate:
                printConversion(conversionRate, baseCurrency, targetCurrency, value)

        elif userInput == "2":
            baseCurrency = input("\nEnter base currency (e.g. GBP, EUR): ").upper()
            conversionRate = getConversionRate(baseCurrency, targetCurrency)

            if conversionRate:
                printConversion(conversionRate, baseCurrency, targetCurrency, value)

        elif userInput == "3":
            targetCurrency = input("\nEnter desired currency (e.g. USD, JPY): ").upper()
            conversionRate = getConversionRate(baseCurrency, targetCurrency)

            if conversionRate:
                printConversion(conversionRate, baseCurrency, targetCurrency, value)

        elif userInput == "4":
            os.system("cls")
            return
        else:
            print("Invalid choice, try again")



def quickConversion(baseCurrency):
    print("--------------------------------------------------------")
    print(f"|                Quick Conversion ({baseCurrency})                |")
    print("--------------------------------------------------------")

    while True:
        try:
            value = float(input("Enter the amount of money: "))
            break
        except ValueError:
            print("*** ERROR: Invalid input. Please enter a valid numerical value. ***")

    targetCurrency = input("Enter desired currency (e.g. USD, JPY): ").upper()

    conversionRate = getConversionRate(baseCurrency, targetCurrency)

    if conversionRate:
        printConversion(conversionRate, baseCurrency, targetCurrency, value)

    while True:
        print("\n1) Convert a different amount")
        print(f"2) Change target currency (currently {targetCurrency})")
        print("3) Exit to main menu")

        userInput = input("Enter your selection [1-3]: ")

        if userInput == "1":
            while True:
                try:
                    value = float(input("Enter the amount of money: "))
                    break
                except ValueError:
                    print("*** ERROR: Invalid input. Please enter a valid numerical value. ***")
                    
            conversionRate = getConversionRate(baseCurrency, targetCurrency)
            
            if conversionRate:
                printConversion(conversionRate, baseCurrency, targetCurrency, value)

        elif userInput == "2":
            targetCurrency = input("\nEnter desired currency (e.g. USD, JPY): ").upper()
            conversionRate = getConversionRate(baseCurrency, targetCurrency)

            if conversionRate:
                printConversion(conversionRate, baseCurrency, targetCurrency, value)

        elif userInput == "3":
            os.system("cls")
            return
        else:
            print("Invalid choice, try again")



def helpMenu():
    print("\n-------------------------------------------------------")
    print(f"|                      Help Menu                      |")
    print("-------------------------------------------------------")
    print("This program uses ExchangeRate-API for its currency codes, descriptions and exchange rates")
    print("For more information, visit their website: ")
    print("https://www.exchangerate-api.com/")
    print("This is a project made by William Chamberlain (wchamberlain8 on GitHub)")
    print("---------------------------------------------------------")
    print("To use the program, follow the instructions and enter in valid selections:")
    print("To navigate menus, use numbers [1-?] depending on the menu")
    print("To convert currencies, enter in a valid currency code and an amount of money to convert")
    print("Valid country codes are available from the main menu, or on the ExchangeRate-API website")
    print("\n")



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
            os.system('cls')
            currencyCodePages()
            return
        elif userInput == '3':
            os.system('cls')
            quickConversion("GBP")
            return
        elif userInput == '4':
            os.system('cls')
            quickConversion("USD")
            return
        elif userInput == '5':
            os.system('cls')
            quickConversion("EUR")
            return
        elif userInput == '6':
            os.system('cls')
            helpMenu()
            return
        elif userInput == '7':
            print("Exiting...")
            time.sleep(1)
            exit()
        else:
            print("Invalid choice, try again")

while True:
    menu()
    menuInput()