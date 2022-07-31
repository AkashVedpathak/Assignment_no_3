def addition_list(): 
    num=int(input("Enter the amount of numbers : ")) 
    lst1=[]
    for i in range(num):
        num1=int(input("Enter the number : "))
        lst1.append(num1)
    add=sum(lst1)
    return add

data=addition_list()
print(data)

