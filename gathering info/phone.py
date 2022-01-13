import phonenumbers
from phonenumbers import carrier, geocoder, timezone

phone_number = input("Phone number with country code : ")
phone_number = phonenumbers.parse(phone_number)

print(timezone.time_zones_for_number(phone_number))
print(carrier.name_for_number(phone_number,"en"))
print(geocoder.description_for_number(phone_number,"en"))

print("Valid phone number : ", phonenumbers.is_valid_number(phone_number))

print("Checking possibility of number :", phonenumbers.is_possible_number(phone_number))