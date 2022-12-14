price = float(input("What is the original price of the item? "))

sdcd_36 = price*0.9
sdcd_30 = 1.2*sdcd_36 - 1.8
sdcd_24 = 1.5*sdcd_36 - 4.4
sdcd_18 = 2*sdcd_36 - 9
sdcd_12 = 3*sdcd_36 - 18

sdcd_36 = "{:.2f}".format(sdcd_36)
sdcd_30 = "{:.2f}".format(sdcd_30)
sdcd_24 = "{:.2f}".format(sdcd_24)
sdcd_18 = "{:.2f}".format(sdcd_18)
sdcd_12 = "{:.2f}".format(sdcd_12)

contract_length = ["Options: 36", "30", "24", "18", "12"]

customer_ask = input("How many months of contract do you need? ")

if customer_ask == "36": 
 print(sdcd_36 + " for 36 months")
elif customer_ask == "30": 
 print(sdcd_30+ " for 30 months")
elif customer_ask == "24": 
 print(sdcd_24 + " for 24 months")
elif customer_ask == "18": 
 print(sdcd_18 + " for 18 months") 
elif customer_ask == "12": 
 print(sdcd_12 + " for 12 months")

options = input("Options: iPhone, Samsung, Motorola ")
phone_options_iphone = input("Phone Options: iPhone 13, iPhone 14 Pro, iPhone 14 Plus, iPhone 14 Pro Max ")
phone_options_samsung = input("Phone Options: Galaxy S22, Galaxy S22+, Galaxy S22 Ultra 5G")
phone_options_motorola = input("Phone Options: Moto G22, Moto G50, Moto G62, Moto E20, Moto E30")

if options == "iPhone":
 phone_options_iphone
 if phone_options_iphone == "iPhone 14 Pro":
  print("iPhone 14 Pro")
elif options == "Samsung":
  phone_options_samsung
elif options == "Motorola":
  phone_options_motorola
else:
  print("Invalid Input")

