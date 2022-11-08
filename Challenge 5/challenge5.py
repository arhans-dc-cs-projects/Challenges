import time

import random
def count():
  c = int(input('Enter a number to count down from: ')) 
  while c > 0:
    print(c)
    time.sleep(1)
    c -= 1
count()

print("The countdown for your number has ended now, the computer's randomly generated number countdown will start now.")

rnum = random.randint(1,10)

def count():
  global rnum
  c = rnum 
  while c > 0:
    print(c)
    time.sleep(1)
    c -= 1
count()

x = int(input("Choose a number: "))
y = int(input("Choose a larger number: "))
print("The timer will countdown from your range of numbers")
rnumy = random.randint(x,y)
def count():
  global rnuy
  c = rnumy
  while c > 0:
    print(c)
    time.sleep(1)
    c -= 1
count()

print ("Program Completed, Hope you enjoyed!")
