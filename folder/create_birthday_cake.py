def create_birthday_cake(name: str, age: int) -> str:
    belgi = '#' if age // 2 == 0 else '*'
    message = f"{belgi} {age} Happy Birthday {name}! {age} {belgi}"
    belgilar = belgi*len(message)
    res = f'"{belgilar}"\n"{message}"\n"{belgilar}"'
    with open('data.sql', 'w') as f:
      f.write(res)
    return res


try:
    print(create_birthday_cake(input("name>>> "), int(input("age>>> "))))
except Exception as err:
    print(err)
