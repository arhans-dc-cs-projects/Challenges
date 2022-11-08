above49 = 0
below50 = 0
#this imports the random library
import random


#ouputs the literal string to the shell
print("Please generate between 1-10 numbers")


#ouputs the literal string to the shell
#Allows the user to ENTER a value
#Collects the data entered as a STRING
#int casts the value ENTERED into an integer
#= assigns the value to a variable
#times is the name of the place in memory the value will be stored
## i.e. the variable name
times = int(input("How many numbers do you want to generate? ")) #11


#loops/iterates if the number entered is not between 1 and 10
while times < 1 or times > 10: #INDEFINITE ITERATION
    #re-assign the value in times
    times = int(input("How many numbers do you want to generate? ")) #12 #0 #3


#loops/iteration if the value in times is greater than 0
while times > 0: #5 #4 #3 #2 #1 #DEFINITE ITERATION
    #using random library to generate number between 0 and 100
    #stores that random number in the variable rnum
    rnum = random.randint(0,100)
    #outputs the literal string followed by the random number generated
    print("the random number is: ", rnum)


    #checks if the random number generated which is stored in rnum
    ## is greater than 49
    if rnum > 49:
        #output that the number is 50 or higher
        print("that number is 50 or higher")
        above49 = above49 + 1
        
    #if the random number is ANYTHING other than a number greater
        ## than 49 do this....
    else:
        #output that the number is lower than 50
        print("that number is lower than 50")
        below50 = below50 + 1



    #This will deduct 1 from the times variable and then
    ##re-assign
    times = times - 1 #4 #3 #2 #1 #0

print(above49 + "are above 49")
print(below50 + "are below 50")


print("GAME OVER")
