
def values(numbers_int):
    refined=[]
    for n in numbers_int:
        if n%2 ==0:
            refined.append(n)
    return refined

# main 
orginal=[2,7,8,67,53,0,24,68,-34]
even_list= values(orginal)
print(" The orginal list was:", orginal)
print("The list after removing uneven numbers is: ",even_list)

