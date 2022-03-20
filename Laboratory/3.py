#3)Write a program that calculates the sum 1 + 1/2 + 1/4 + 1/8 + ... where the user will give the number of terms of the sum.
Ensure with defensive programming that the value given by the user is a non-negative integer value, otherwise the value will be re-entered.
n=int(input("Enter the number of terms: "))
sum1=0
if n<0:
        n=int(input("Enter the number of terms: "))
        while n < 0:
            n=int(input("Enter the number of terms: "))


for i in range(1,n+1):
    sum1=sum1+(1/i)
    print("The sum of series is",round(sum1,2))
