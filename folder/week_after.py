from datetime import datetime, timedelta


def add_week(date_string):
    date_object = datetime.strptime(date_string, '%d/%m/%Y')
    new_date = date_object + timedelta(weeks=1)
    return new_date.strftime('%d/%m/%Y')


# Test qilingan sana
date_string = "29/12/2020"
print("Boshlang'ich sana:", date_string)
print("Keyingi hafta sana:", add_week(date_string))