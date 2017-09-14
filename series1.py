no=int(input(print("Enter no.")))
sum=0
for i in range (1,no+1):
    sum=sum+(1/(i*i))
    p=(1/(i*i))
    print("1/",(i*i),"=",p)
print("sum of series= ",sum)