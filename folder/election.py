

def election(data: dict) -> None:
    count_false = [data[i] for i in data].count(0)
    count_true = [data[i] for i in data].count(1)

    if count_true> count_false:
        for i in data:
            if data[i]:
                print(i, end=' ')
    elif count_false > count_true:
        for i in data:
            if not data[i]:
                print(i, end=' ')
    else:
        for i in data:
            print(i, end=' ')


data = {'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}


while True:
    try:
        count = int(input('>>> '))
        i = 0
        while i < count:
            try:
                name = input('name >>> ')
                status = int(input('status >>> '))
                if not status > 1:
                    status = 1
            except Exception as err:
                print('Xato qiymat kritildi qayta urinib kurinbg.')
    except Exception as err:
        print('Xato qiymat kritildi qayta urinib kurinbg.')

print(election(data))