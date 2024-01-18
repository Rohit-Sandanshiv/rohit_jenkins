def my_func(x):
    sum=0
    for i in x:
        sum+=i
    return sum
x=input()
x=map(int,x.split())
print(my_func(x))
      
