import requests
import json

# The API endpoint URL
url = "https://api.jsrates.com/shopify/cappedheads-3-shipping"

# Headers required by the API
headers = {
    "x-jsrates-shop-domain": "cappedheads-3.myshopify.com",  # Make sure to replace with your actual Shopify domain
    "x-jsrates-api-key": "6e2b1bc8cbe2c593ea96a2f0b322d1ca222d6f3d002b88e5036af70f4b20869b",
    "Content-Type": "application/json",
    "Origin": "https://www.swagbulk.com"
}

# Adjusted JSON request payload reintroducing the "rate" key
payload = {
    "rate": {
        "origin": {},
        "destination": {
            "country": "AU",
            "postal_code": None
        },
        "items": [
            {
                "quantity": 300,
                "requires_shipping": True,
                "alibaba_id": "1600706815490"
            }
        ],
        "currency": "USD",
        "locale": "en",
        "from_woo": True
    }
}

def get_data_from_api():
    # Making a POST request to the API
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the response JSON and returning it
        return response.json()
    else:
        # Printing the error for debugging purposes
        print("Error:", response.status_code, response.text)
        return f"Error: Unable to fetch data from the API, status code {response.status_code}"

if __name__ == "__main__":
    # Getting the data from the API
    data = get_data_from_api()
    # Printing the data
    print(data)
