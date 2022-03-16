valid = False
while not valid:
 
    response = float(input("Enter a Number? "))
    
    if response > 0:
        valid = True
    
    else:
        print("Please enter a number that is not zero.")
        print()
        