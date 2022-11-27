import phonenumbers
from phonenumbers import timezone,geocoder,carrier

#print(dir(phonenumbers))
number=input("Interrogate Your  Number of Phone: ")
phone=phonenumbers.parse(number,"TR")
Time=timezone.time_zones_for_number(phone)
x=carrier.name_for_number(phone,"TR")
reg=geocoder.description_for_number(phone,"tr")
print(phone)
print("Current Location Of Your Phone: {}".format(Time))
print("Operator's Name: {0}".format(x))
print("Place of Registered SIM Card : {0}".format(reg))

