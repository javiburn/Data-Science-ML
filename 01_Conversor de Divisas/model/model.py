import requests
import datetime

class Rate:
    api_key:str
    value: float
    
    def __init__(self, api_key):
        self.api_key = api_key

    def get_rate_value(self):
        endpoint = "https://v6.exchangerate-api.com/v6/" \
        + self.api_key + "/latest/USD"
        response = requests.get(endpoint)
        data = response.json()
        if response.status_code == 200:
            try:
                data_value = data['conversion_rates']['EUR']
                if not data_value:
                    self.value = 0.9
                    raise ValueError("No value for converting to EUR found")
                self.value = data_value
            except Exception as e:
                print(f"Error extracting data: {e}")
                self.value = 0.9
        else:
            self.value = 0.9
            print("Invalid URL, rate set by default to 0.9")

class Calculator:
    def __init__(self):
        self.insert_name()
        self.insert_date()
        self.insert_daytime()
        self.insert_money()

    def insert_name(self):
        self.name = ""
        while self.name == "":
            self.name = input("Please, enter your name: ")
            if self.name == "":
                print("Invalid name.")
        self.name.title()

    def insert_date(self):
        correct_date = False
        while correct_date == False:
            self.date = input("Date of transaction (format DD-MM-YYYY): ")
            if len(self.date) != 10:
                print("Invalid date.")
            else:
                day = int(self.date[0:2])
                month = int(self.date[3:5])
                year = int(self.date[6:])
                try:
                    new_date = datetime.datetime(year, month, day)
                    correct_date = True
                except:
                    correct_date = False
                    print("Invalid date.")

    def insert_daytime(self):
        array = ['morning', 'noon', 'night']
        self.daytime = ""
        while self.daytime == "":
            self.daytime = input("Time of transaction (morning, noon or night): ")
            if self.daytime == "":
                print("Invalid daytime.")
            else:
                self.daytime.lower()
            if self.daytime not in array:
                print("Invalid daytime.")
                self.daytime = ""
        
    def insert_money(self):
        self.money = ""
        while self.money == "":
            self.money = input("Amount of dollars to exchange: ")
            if self.money == "":
                print("Invalid amount.")
            try:
                float(self.money)
            except:
                print("Invalid amount.")
                self.money = ""

class Printer:
    def __init__(self, rate, calculator):
        self.rate = rate
        self.calculator = calculator
        self.print_all()
    
    def print_notes(self):
        string = ""
        if self.total == 0:
            print("You will receive no money at all")
        else:
            string = "You will receive "
            if self.total // 10 > 0:
                string += str(int(self.total // 10)) + " 10€-notes"
            if int(self.total) % 1 > 0:
                string += " and " + str(int(self.total % 1)) + " 1€ coins"
            if self.total - int(self.total) > 0:
                string += " and " + str("{:.2f}".format(self.total - int(self.total))) + (" €")
        print(string + ".")

    def print_all(self):
        print("Welcome, " + self.calculator.name)
        print("Your are going to exchange " + self.calculator.money + "$")
        self.total = float(self.calculator.money) * float(self.rate.value)
        print("You will receive " + str(self.total) + "€")
        self.print_notes()
        print("Goodbye!")
