s = int(input("enter number"))
if s < 2:
    print("Not a prime no.")
    exit()
elif (s > 2 and s % 2 == 0):
    print("Its not a prime no.")
        
elif (s == 2 or s == 3 or s == 5 or s == 7 or s == 11):
        print("Its a prime no.")
        exit()
else:
    import math
    s_sqrt = math.sqrt(s)
    converter = int(s_sqrt)
    for h in range(3,converter + 2,1):
        if s % h == 0:
            print("Its not a prime no")
            exit()
print("Its a prime no")            
    