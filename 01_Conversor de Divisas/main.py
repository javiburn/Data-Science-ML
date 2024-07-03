import os
from dotenv import load_dotenv
from model.model import Rate, Calculator, Printer

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
    calculator = Calculator()
    printer = Printer(rate, calculator)

if __name__ == '__main__':
    main()