import random
import time

# QUESTION DICTIONARY
question_list = {
    '1':"What is the member code for a Member (0-9 Nights/Year)? ",
    '2':"What is the member code for a Silver Elite member (10-24 Nights/Year)? ",
    '3':"What is the member code for a Gold Elite member (25-49 Nights/Year)? ",
    '4':"What is the member code for a Platinum Elite member (50-74 Nights/Year)? ",
    '5':"What is the member code for a Titanium Elite member (75+ Nights/Year)? ",
    '6':"What is the member code for an Ambassador Elite member (100+ Nights and 23k USD qualifying spend/Year)? "
}

# ANSWER DICTIONARY
answer_list = {
    '1':"Y1",
    '2':"M1",
    '3':"X1",
    '4':"P6",
    '5':"X4",
    '6':"X5"
}

# MAIN
# Quiz length currently hardcoded to 3 questions

current_question_number = 0
score = 0

print("Welcome to the Marriott Bonvoy quiz!")
time.sleep(1)
how_many_questions = int(input("How many questions would you like to answer today? "))
print("OK. Here are " + str(how_many_questions) + " questions to test your Marriott Bonvoy knowledge.")
time.sleep(1)
while current_question_number < how_many_questions:
    # Random question key from question_list dictionary 
    current_random_key = str(random.randint(1,len(question_list)))
    current_question = (question_list[current_random_key])
    current_correct_answer = (answer_list[current_random_key])
        
    user_answer = input(current_question)
    # Correct answer
    if current_correct_answer.lower() == user_answer.lower():
        score += 1
        print("Correct! + 1 point!")
    # Incorrect answer     
    else:
        print("Incorrect")
    current_question_number += 1
    time.sleep(1)

# Game over 
print("Thanks for playing!")
time.sleep(1)
print("Your final score is: " + str(score) + " out of " + str(how_many_questions))

# MEMBER LEVEL DICTIONARIES
# No code! -> Non-member
# Y1 Member           (0-9 Nights/Year)
# member = {
    # "code": "Y1",
    # "min_nights": "0",
    # "max_nights": "9"
# }

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

# BENEFITS
# Member
# member = ["Mobile App Services", "Member-only Rates", "Free Wi-Fi"]
# member_length = len(member)

# Silver Elite
# silver_extras = ["Elite Reservation/Guest Service Line", "10% Gift Shop Discount", "Ultimate Reservation Guarantee", "10% Bonus on Loyalty Base Points", "Priority Late Check Out"]
# silver_elite = member + silver_extras
# silver_length = len(silver_elite)