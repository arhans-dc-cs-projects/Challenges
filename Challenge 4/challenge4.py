import random 
firstname = input("What is your first name? ")
surname = input("What is your last name? ")



print(firstname + " " + surname)
firstnamecaps = firstname.upper()
surnamecaps = surname.upper()

firstname_initial = firstname[0]
surname_initial = surname[0]
print(firstname_initial + surname_initial)
print(firstname_initial + "." + surname_initial + ".")
print(firstname_initial + surname)

fullname = firstname + surname 

print(fullname[::-1])
print(fullname[::2])



age = int(input("What is your age? "))
print(str(age) + firstname + surname)

len_surname = len(surname)
print(firstname+surname+str(len_surname))

len_firstname = len(firstname)
len_fullname = len(fullname)

randfirst = random.randint(0,(len_firstname - 1))
print(firstname[randfirst])
randfull = random.randint(0,(len_fullname - 1))
print(fullname[randfull])

years = int(input("Choose a random number between 0-100: "))
years2 = age+years
print(str(years2)+firstname+surname)


