x = int(input("enter a number"))
if x % 3 == 0 and x % 5 == 0 :
    print ("Fizz buzz")
elif x % 3 == 0:
    print ("Fizz")
elif x % 5 == 0:
    print ("Buzz")
else:
    print (x)
    