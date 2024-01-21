print("Welcome to the tip calculator ")
bill_total = float(input("enter the amount of total bill $ : " ))

# tip should be given and tip should be how much given 
tip_given = int(input("enter the tip should be given ? 10 , 12 and 15 ? "))

# people the bill should be split among the members 
people = int(input("how many people split the bill among them : ")) # it can be 5 , 7 ,9

total_bill_tip = float(tip_given / 100 * bill_total + bill_total)
print(f"your total bill at the end is :{total_bill_tip}")
 
split_bill = float(total_bill_tip / people)

final_amount = round(split_bill, 2)
# it divide among the number of bill should be divided among the people ie 100/5 ... each has to pay 20$
print(f"Each person should pay : {final_amount} ")
 

