rent = int(input("Enter your hostel/flat rent : "))
food_ordered = int(input("Enter the amount of food ordered : "))
electricity_spend = int(input("Enter the total of electricity spend : "))
charge_per_unit = int(input("Enter the charge per unit : "))

persons = int(input("Enter the number of persons living in room/flat : "))
total_bill = electricity_spend * charge_per_unit 

output = (food_ordered + rent + total_bill) // persons
print("Each persons will pay : ",output)