import sys
import requests

def main():
    amount = check_argv(sys.argv)
    current_price = get_price()
    price = amount * current_price
    print(f"${price:,.4f}")
    sys.exit()

def check_argv(argv):
    if len(argv) == 1:
        sys.exit("Missing command-line argument")
    try:
        amount = float(argv[1])
        return(amount)
    except ValueError:
        sys.exit("Command-line argument is not a number")

def get_price():
    api_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return(float(api_response["bpi"]["USD"]["rate_float"]))

if __name__ == "__main__":
    main()
