user=input("Enter a string: ")
def upper_lower_case(str1):
    count_upper=0
    count_lower=0
    for  i in range(len(str1)):
        if str1[i].isupper():
            count_upper+=1
        elif str1[i].islower():
            count_lower+=1          
    print("No. of Upper case characters ",count_upper)
    print("No. of Lower case Characters ",count_lower)
upper_lower_case(user)

