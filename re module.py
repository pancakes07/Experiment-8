import re
data = input ("Enter emmail or phone number : ")
email_pattern = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern=r'^[0-9]{10}$'

if re.fullmatch(email_pattern,data):
    print("Invalid email id")

elif re.fullmatch(mobile_pattern,data):
    print("Invalid Mobile number")

else:
    print("Invalid email id or Invalid Mobile number")
