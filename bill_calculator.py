print("Welcome to the tip calculator!")

bill = input("What was the total bill? $" )

bill_as_num = int(bill)

tip = input("How much tip would you like to give? 10, 12, or 15? " )

tip_as_num = int(tip)

number_of_people = input("How many people to split the bill? ")

number_of_people_as_num = int(number_of_people)

result = round((tip_as_num + bill_as_num)/number_of_people_as_num , 2)

final_result = "{:.2f}".format(result)

print(f"Each person should pay: ${final_result}")

