import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            input_value = float(sys.argv[1])
            btc_price = get_btc_price(input_value)
            if btc_price:
                print("BTC price:", btc_price)
            else:
                print("Error retrieving BTC price.")
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def get_btc_price(quantity):
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            data = response.json()
            price = data["bpi"]["USD"]["rate_float"]
            total = price * quantity
            return f"${total:,.4f}"
        else:
            return None
    except requests.RequestException:
        return None


if __name__ == "__main__":
    main()
