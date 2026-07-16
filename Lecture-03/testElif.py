num_employees = int(input("Enter the number of employees :"))

if num_employees < 50:
    print("The is a small company.")
elif num_employees < 250:
    print("This is medaium-sized company.")
elif num_employees >= 250: 
    print("This is a large company.")