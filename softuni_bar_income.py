import re
some_string = input()
string_regex = r"%(\b[A-Z][a-z]+)%<([a-zA-Z]+)>([a-z]+)?\|(\d+)\|([a-z]+)?(\d+\.?\d*)\$"
final_price = 0
total_income = 0
prices = []
while some_string != "end of shift":
    match = re.search(string_regex, some_string)
    if match:
        name, product,some_things, quantity,another_things, price = match.groups()
        final_price = int(quantity) * float(price)
        prices.append(final_price)
        print(f"{name}: {product} - {final_price:.2f}")
    some_string = input()

print(f"Total income: {sum(prices):.2f}")


