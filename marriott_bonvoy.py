import random
import time

""" Make a dictionary of questions
Assign a question to an answer as a key value pair
Every time a question is generated
eg. question 1:"""

# QUESTION DICTIONARY
question_list = {
    '1':"What is the name of the hotel?",
    '2':"What is question 2?"
}

# MAIN
how_many_questions = 3
current_question_number = 0
score = 0
# Random question key currently hardcoded for 2 questions 
random_question_key = str(random.randint(1,2))
question_1 = "Q1: What is the name of the hotel? "
correct_answer_1 = "Bankside"

print("Welcome to the Marriott Bonvoy quiz!")
time.sleep(2)
print("Here are " + str(how_many_questions) + " questions to test your Marriott Bonvoy knowledge.")
time.sleep(1)
while current_question_number < how_many_questions:
    user_answer = input(question_1)
    # Correct answer
    if correct_answer_1.lower() == user_answer.lower():
        score += 1
        print("Correct")
    # Incorrect answer     
    else:
        score -= 1
        print("Incorrect")
    print("Your score is now: " + str(score))
    current_question_number += 1
    time.sleep(1)

print("Thanks for playing!")
print("Your final score is: " + str(score))
print(question_list[random_question_key])

# MEMBER LEVEL DICTIONARIES
# No code! -> Non-member
# Y1 Member           (0-9 Nights/Year)
# member = {
    # "code": "Y1",
    # "min_nights": "0",
    # "max_nights": "9"
# }

# Y1 Member           (0-9 Nights/Year)
# M1 Silver Elite     (10-24 Nights/Year)
# X1 Gold Elite       (25-49 Nights/Year)
# P6 Platinum Elite   (50-74 Nights/Year)
# X4 Titanium Elite   (75+ Nights/Year)
# X5 Ambassador Elite (100+ Nights and 23k USD qualifying spend/Year)

# MAIN
# while True:
    # Member level list
    # member_level_list = ['Non-member', 'Member', 'Silver Elite', 'Gold Elite', 'Platinum Elite', 'Titanium Elite', 'Ambassador Elite']
    # Random member level
    # random_member_level = (member_level_list[random.randint(0,6)])
    # Member code question
    # if random_member_level == member_level_list[0]:
        # user_input = input("Does a non-member have a member code? ")
    # else:
        # user_input = input("What is the member code for " + random_member_level + " level?: ")

# Index 0 -> Non-member
    # while random_member_level == member_level_list[0]:
        # if user_input == "no":
            # print("CORRECT")
            # break
        # else:
            # print("INCORRECT")
            # break

# BENEFITS
# Member
# member = ["Mobile App Services", "Member-only Rates", "Free Wi-Fi"]
# member_length = len(member)


# Silver Elite
# silver_extras = ["Elite Reservation/Guest Service Line", "10% Gift Shop Discount", "Ultimate Reservation Guarantee", "10% Bonus on Loyalty Base Points", "Priority Late Check Out"]
# silver_elite = member + silver_extras
# silver_length = len(silver_elite)

# Gold Elite
# Platinum Elite
# Titanium Elite
# Ambassador Elite

# For selecting a random membership type to be quizzed on
# random_membership = random.randint(1,6)
# print(random_membership)
#1: member
#2: silver_elite
#3: gold_elite
#4: platinum_elite
#5: titanium_elite
#6: ambassador_elite

# i = 0
# while i < member_length:
    # print(member[i])
    # i += 1