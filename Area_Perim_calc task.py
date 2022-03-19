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
width = num_check("width: ")
height = num_check("height: ") 

# calculate area ( width x height)
area = width * height
print(area)
# calculate perimeter
Perimeter = width * 2 + height * 2
print( " The perimeter is, {} square units". format(Perimeter))
print(" The area is, {} units".format(area))


