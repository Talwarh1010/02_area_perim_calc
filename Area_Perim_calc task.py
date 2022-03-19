# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = ("Please enter a number that is not zero.")
            
        try:
            
            # asks the user to enter a number
            response = float(input(question))
            
            # checks number  is more than zero
            if response > 0:
                return response
                
            # outputs error if input is invalid
            else:
                print(error)
                print()
            
        except ValueError:
            print(error)
            
            
            
# main routine goes here

# introduction / heading print statements
print()
print( " WELCOME TO AREA / PERIMETER CALCULATOR!")
print()
# loop begins
keep_going = ""
while keep_going == "":

    width = num_check("width: ")
    height = num_check("height: ") 

    # calculate area ( width x height)
    area = width * height
    print(area)
    # calculate perimeter
    Perimeter = width * 2 + height * 2
    print( " The perimeter is, {:.2f} square units". format(Perimeter))
    print(" The area is, {:.2f} units".format(area))
    print()
    
    keep_going = input("Press <enter> to keep going or any key to quit")

print()    
print("Thanks for using area / perimeter calculator!")   


