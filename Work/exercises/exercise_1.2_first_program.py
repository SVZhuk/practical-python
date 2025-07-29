# One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. 
# Each day thereafter, you go out double the number of bills. How long does it take for the 
# stack of bills to exceed the height of the tower?

bill_thickness = 0.11 * 0.001  # meters (0.11 mm)
sears_height = 442  # meters
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(f"day: {day}, num bills: {num_bills}, thickness: {num_bills * bill_thickness:.3f}")
    num_bills *= 2
    day += 1
    
print(f"Number of days to stack bills: {day - 1}")
print(f"Number of bills: {num_bills}")
print(f"Final height of stack: {num_bills * bill_thickness:.3f} meters")
