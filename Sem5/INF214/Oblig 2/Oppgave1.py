# importing the requests library
import requests
import urllib.parse

operation = "simplify"


def getDef(expression):
    ex = urllib.parse.quote(expression)
    # api-endpoint
    URL = f"https://newton.now.sh/api/v2/{operation}/{ex}"

    r = requests.get(url = URL)

    # extracting data in json format
    data = r.json()

    return data["result"]

while True:
    inn = input("Input something to simplify. (q) to quit\n")
    if(inn == "q"):
        break
    print(f'Your result: {getDef(inn)}')
