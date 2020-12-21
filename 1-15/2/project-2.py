print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n"))
tip = int(input(
    "What percentage tip would you like to give?\n10, 12, or 15?\n"))
persons = int(input("How many people to split the bill?\n"))
total_tip = total_bill * tip / 100
payment = (total_bill + total_tip) / persons
print(f"Each person should pay : ${round(payment, 2)}")
