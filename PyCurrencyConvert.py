import requests

url = 'https://v6.exchangerate-api.com/v6/80c772aad2e7ff37519f5ec5/latest/GBP' #API key

#response = requests.get(url) #http get request
#data = response.json() 

def customConversion():
    userCurrency = input("Enter currency you wish to convert: ")
    value = input("Enter the amount of money: ")
    targetCurrency = input("Enter desired currency: ")

#print(data)

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
    lock = True
    while lock == True:
        userInput = input("Please enter your selection [1-7]: ")

        if userInput == '1':
            lock = False
            customConversion()
        else:
            print("Invalid choice, try again")

menu()
menuInput()