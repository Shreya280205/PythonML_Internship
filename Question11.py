def fibonacci(n):
    temp=[0,1]
    for i in range(2,n):
      temp.append(temp[i-1]+temp[i-2])
    return temp[0:n]



n = int(input("Enter the number of Fibonacci numbers to generate: "))
ans=fibonacci(n)
print("The first", n,"Fibonacci number are: ",ans)