n = int(input("Enter total number of values(at least 2): "))


max = int(input("Enter number 1: "))
max2 = None

i = 2
while i <= n:

        value = int(input(f"Enter number{i} "))

        if(value > max):
            max2 = max
            max = value
        elif value < max and (max2 is None or value > max2):
            max2 = value
        i += 1

if max != max2:
    print("second highest is ", max2)
   

else:
    print("All values are same")
    