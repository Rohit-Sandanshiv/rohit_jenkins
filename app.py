def my_func(x):
    sum=0
    for i in x:
        sum+=i
    return sum
string1=input()
lst=map(int,string1.split())
print(my_func(lst))
      
