import sys
import requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    much = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourAPI")
    note = response.json()
    amount = float(note["data"]["priceUsd"]) * much
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()

