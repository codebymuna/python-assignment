# Program inorder to take numbers from user and print as a list of decending numbers using sort(reverse=true).
numbers=[]
while True:
    num = (input("Enter a number: "))
    if num =="":
        break
    numbers.append(int (num))
numbers.sort(reverse=True)   # For decending order in list.
print(numbers)    