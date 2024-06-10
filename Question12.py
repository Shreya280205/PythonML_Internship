def sum_of_digits(number):
    sum=0
    strnum=str(number)
    for digit in strnum:
        sum+=int(digit)
    return sum

number=int(input("Enter a number: "))
result=sum_of_digits(number)
print("The sum of the digits of",number,"is:",result)