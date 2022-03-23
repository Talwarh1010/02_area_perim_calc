# functions go gere

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":
# Input for width, length and cost/mk   
    width =  num_check( "width: ")
    length = num_check( "Length: ")
    costm = num_check( "cost/m: ")
    
# calculate fence price
    Perimeter = ( width * 2 + length * 2)
    Cost = (Perimeter * costm)
    
    print(" The perimeter of the fence is {:.2f} metres". format(Perimeter))
    print(" The cost for the fence is {:.2f} dollers". format(Cost))
        
    
    keep_going = input("Press <enter> to keep going or press any key then enter to quit")
    
    print()
print("Thanks for using the Fencing cost calculator")