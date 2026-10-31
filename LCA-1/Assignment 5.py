#Q5
import re

pan_num = input("Enter your PAN number: ").strip()

pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

if re.match(pattern, pan_num):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")