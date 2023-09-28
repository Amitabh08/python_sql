## FIND MAXIMUM NUMBER IN A GIVEN SEQUENCE
n = int(input("Enter n: "))
max = None
for i in range(n):
    num = int(input("enter number\t" ))
    if max is None or num > max:
        max = num
        
print("maximum number is:  ",max) 
