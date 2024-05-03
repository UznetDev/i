def is_valid_phone_number(number :str) -> int:
  ln = len(number)
  if ln != 18:
      return False
  if not number.startswith("(998) ") or number.count('-') != 3:
      return False
  part = number[6:].split("-")
  if len(part) != 4:
      return False
  for part in part:
      if not part.isdigit():
          return False
  return True


# print(is_valid_phone_number("(998) 98-123-45-67"))
# print(is_valid_phone_number("(998) 90-12-12-12"))
# print(is_valid_phone_number("998) 95-987-65-43"))
# print(is_valid_phone_number("(998) 93-654-12-78"))


try:
    check = is_valid_phone_number(input(">>>    "))
    if check:
      print('Bu haqiqiy raqam')
    else:
      print("Bu notug'ri raqam")
except:
    print('Xato qiymat kritildi')