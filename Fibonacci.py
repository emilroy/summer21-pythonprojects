#Author: Emil
#Description: prints Fibonacci sequence up to the chosen limit


def Fibonacci(n):  
   if n <= 1: 
       return n  
   else:  
       return(Fibonacci(n-1) + Fibonacci(n-2)) #takes the previous two previous terms and adds them to create next item in list

print("========Fibonacci Sequence========")

while True: 
    terms = int(input("Enter the number of terms you want to see: "))
    if terms <= 0:
       print("Please enter a positive integer")  
    else:  
       print("Fibonacci sequence:")  
       for i in range(terms):  #will print out each term of the sequence
           print(Fibonacci(i))
       break


   
