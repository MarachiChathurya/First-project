#To find factorial of a number using recursive function
def factorial(a):
        if a==0:
                return 1
        else:
                return(a*factorial(a-1))
n=int(input("Enter the number"))
print("Factorial of {} is {}".format(n,factorial(n)))
