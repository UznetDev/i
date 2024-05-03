from datetime import date
class Date:
    # constructor to initialize a date object with year, month, and day
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# Drug class inherits from Date class
class Drug(Date):
    def __init__(self, year, month, day, drug_name, company_name):
        super().__init__(year, month, day)  # call parent class constructor
        self.drug_name = drug_name
        self.company_name = company_name

    # method to calculate the number of days since the creation of the drug object
    def days_since_created(self):
        today = date.today()
        delta = today - self  # calculate difference between today and the creation date
        return delta.days  # return the number of days

# create a Drug object with user input
# drug_name = input("Enter drug name: ")
# company_name = input("Enter company name: ")
# year = int(input("Enter year created: "))
# month = int(input("Enter month created (1-12): "))
# day = int(input("Enter day created: "))
#
# drug = Drug(year, month, day, drug_name, company_name)
#
# # call the method to find the number of days since creation
# days_elapsed = drug.days_since_created()
#
# print(f"The drug {drug.drug_name} has been in storage for {days_elapsed} days.")

print(date.today()-date.fromisoformat('2003-12-30'))