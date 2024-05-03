def format_currency(amount, currency):

  if currency == "UZS":
    formatted_amount = "{:,.2f} so'm".format(amount)
  elif currency == "USD":
    formatted_amount = "${:,.2f}".format(amount)
  else:
    raise ValueError("Unsupported currency: {}".format(currency))
  return formatted_amount

def convert_currency(amount, from_currency, to_currency):
  """Converts an amount from one currency to another.

  Args:
      amount: The amount to convert.
      from_currency: The currency code of the amount to convert from.
      to_currency: The currency code of the amount to convert to.

  Returns:
      The converted amount as a float.
  """

  # For this example, we'll assume a fixed exchange rate of 1 USD = 10000 UZS
  # In practice, you'd use a currency exchange API to get the latest rate.
  exchange_rate = {
      "USD": 1.0,
      "UZS": 0.0001,
  }
  if from_currency not in exchange_rate or to_currency not in exchange_rate:
    raise ValueError("Unsupported currency: {}".format(from_currency or to_currency))
  converted_amount = amount * exchange_rate[to_currency] / exchange_rate[from_currency]
  return converted_amount

def main():
  """Prompts the user for an amount in UZS, converts it to USD, and prints the result."""

  while True:
    try:
      amount = float(input("Enter an amount in Uzbekistani som (UZS): "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  converted_amount = convert_currency(amount, "UZS", "USD")
  formatted_amount = format_currency(converted_amount, "USD")
  print(f"{amount} UZS is equivalent to {formatted_amount}.")

if __name__ == "__main__":
  main()


  def elevator(lst: list, cm: str):
    flour = int(cm[0])
    print(flour)

# A faqat toq qavatlar uchun
# B birinchi eng pastgfa kiyyin tepaga
# C birinchi eng tepaga va pastga


lft = {'A': 9, 'B': 3, 'C': 10}
print(elevator(lft, '5UP'))

