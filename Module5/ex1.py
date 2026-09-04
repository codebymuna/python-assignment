# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
number=1
while  number <= 1000:
    if number% 3 == 0:
        print ("The number is",number)
    number= number+1

