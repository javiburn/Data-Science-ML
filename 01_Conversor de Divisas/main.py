import os
from dotenv import load_dotenv
from model.model import Rate, Calculator

def load_api_key():
    load_dotenv()
    api_key = ""
    try:
        api_key += os.getenv('API_KEY')
    except:
        api_key = ""
    return api_key

def main():
    rate = Rate(load_api_key())
    rate.get_rate_value()
    print(rate.value)
    calculator = Calculator()

if __name__ == '__main__':
    main()