import requests
import time
import os

#'https://v6.exchangerate-api.com/v6/80c772aad2e7ff37519f5ec5/latest/CURRENCY_CODE' #API key

def errorCodes(code):
    if code == 'unsupported-code':
        print("*** ERROR: The base code entered in not available in the API ***")
        print("*** Refer to the currency code in the main menu for more information ***")
    if code == 'malformed-request':
        print("*** ERROR: Request did not follow the valid API structure ***")
    elif code == 'invalid-key':
        print("*** ERROR: The API key is invalid ***")
    elif code == 'quota-reached':
        print("*** ERROR: Account has reached the number of requests allowed by your plan ***")

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
    print("-" * borderLength)
    print(f"* {message} *")
    print("-" * borderLength)


def customConversion():

    print("--------------------------------------------------------")
    print("|                  Custom Conversion                   |")
    print("--------------------------------------------------------")
    baseCurrency = input("Enter currency you wish to convert (e.g. GBP, EUR): ").upper()
    value = float(input("Enter the amount of money: "))
    targetCurrency = input("Enter desired currency (e.g. USD, JPY): ").upper()

    conversionRate = getConversionRate(baseCurrency, targetCurrency)

    if conversionRate:
        printConversion(conversionRate, baseCurrency, targetCurrency, value)

    # TODO: Want to add these features, but don't want it to get messy
    # print("\n1) Convert a different amount")
    # print(f"2) Change base currency ({baseCurrency})")
    # print(f"3) Change target currency ({targetCurrency})")

    # userInput = input("Enter your selection [1-3]: ")

def quickConversion(baseCurrency):
    print("--------------------------------------------------------")
    print(f"|                Quick Conversion ({baseCurrency})                |")
    print("--------------------------------------------------------")
    value = float(input("Enter the amount of money: "))
    targetCurrency = input("Enter desired currency (e.g. USD, JPY): ").upper()

    conversionRate = getConversionRate(baseCurrency, targetCurrency)

    if conversionRate:
        printConversion(conversionRate, baseCurrency, targetCurrency, value)

    # print("\n1) Convert a different amount")



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
            # function call
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