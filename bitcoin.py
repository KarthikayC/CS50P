import requests
import sys

try:
    number_of_bitcoins = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    bitcoin_rate = response["bpi"]["USD"]["rate_float"]
    print(f"${bitcoin_rate * float(sys.argv[1]):,.4f}")
except requests.RequestException:
    sys.exit("Exception Error")