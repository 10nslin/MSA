
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for odd in range(1,100,2): #setting variable to odd = the range of 1-100 skipping everyother number
    print(odd) #printing variable 

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

a = 5 # assigning the varible to 5 since we want from 5-1000000
while a <= 1000000: #creating loop that allows the numbers to be mulitplied by 5
    if a % 5 == 0: #checks to make sure the number assigned to a is divisble by 5
        print(a) #prints if it is
    a+=1 #changes a to 6 and so forth untill it reaches 1000000
    

# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a=[1, 2, 5, 10, 255, 3]
x= sum(a) #takes the sum of the numbers in the list
print(x)

#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
x= sum(a)/len(a) # adding the sum of all the numbers in the list and dividing it by the length of the list
print(x)