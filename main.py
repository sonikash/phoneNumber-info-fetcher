import phonenumbers
import requests
from phonenumbers import geocoder
import os

def get_phone_details(phone_number, api_key):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"

    response = requests.get(url)
    data = response.json()

    if data.get("valid"):
        return {
            "country": data.get("country_name"),
            "location": data.get("location"),
            "city": data.get("city"),
            "carrier": data.get("carrier"),
        }
    else:
        return None


if __name__ == "__main__":
    phone_number = input("Enter the phone number (including country code, e.g., +14155550001): ")
    api_key = os.getenv('API_KEY')
    details = get_phone_details(phone_number, api_key)

    if details:
        print(f"Country: {details['country']}")
        print(f"Location: {details['location']}")
        print(f"City: {details['city']}")
        print(f"Carrier: {details['carrier']}")
    else:
        print("Invalid phone number or unable to retrieve details.")


