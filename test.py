#string for characters
#name = "Inaya"
#print(name.upper())
#input asks the uses a question and records the answer
#what we write in input argument is what user sees input ALWAYS outputs a string
#bill = input("How much was the bill")
#print(bill)

#if bill == 10:
#    print("match")
#else:
#    print("no match")

#""" #integer for whole number
#amt = 100
#Float uses decimal
#amt_two = 99.99 """

#Boolean
#x= True
#y= False



#integer
#x = 7
#String
#name= "Ellie"
#name.upper
#boolean
#isValid= True
#Float
#bill = 56.86


#students = ["Ellie", "Preston", "Ben", "Elyse"]
#students.append("Sofia")
#print (students [-1])
#for student in students:
#    if student == "Ben":
#        print(f'we found {student}')
#sting
#y = input("money?")
#z = y + 5



import random
e = random.randint(1,2)
tries = 1
while True:
    guess = int(input("Please type an number: "))
    if guess > e:
        print("The number is lower")
        tries += 1
    if guess < e:
        print("The number is higher")
        tries += 1
    if guess == e:
        print (f"You got the number in {tries} tries.")
    if guess == e and tries == 1:
        print (f"You got the number in 1 try. Good boy")

        break
    