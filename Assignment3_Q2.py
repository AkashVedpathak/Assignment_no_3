user=input("Enter any word or sentence: ")
def str(word):
    rev=""
    for i in range(len(word)-1,-1,-1):
        rev+=word[i]
    return rev
result=str(user)
print(result)
