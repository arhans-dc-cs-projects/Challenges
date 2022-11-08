name = input("What is your name? ")
gender = input("What is your gender? (male/female) ")
age = int(input("What is your age? "))
#school = input("Which school do you go to? ")
best_friend = input("Who is your best friend? ")

if age < 21 and gender == "female": 
  print(name + " woke up one morning. She walked to school with her best friend, " + best_friend)

elif age < 21 and gender == "male": 
  print(name + " woke up one morning. He walked to school with his  best friend, " + best_friend)

elif age > 20 and gender == "female":
  print(name + " woke up one morning. She walked to work with her best friend, " + best_friend)

elif age > 20 and gender == "male": 
  print(name + " woke up one morning. He walked to work with his best friend, " + best_friend)

