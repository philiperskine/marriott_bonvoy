import random
import time

# QUESTION DICTIONARY
question_list = {
    # Member codes
    '1':"What is the member code for a Member? ",
    '2':"What is the member code for a Silver Elite member? ",
    '3':"What is the member code for a Gold Elite member? ",
    '4':"What is the member code for a Platinum Elite member? ",
    '5':"What is the member code for a Titanium Elite member? ",
    '6':"What is the member code for an Ambassador Elite member? ",
    # Minimum number of nights
    '7':"What is the minimum number of nights per year required for Silver Elite membership? ",
    '8':"What is the minimum number of nights per year required for Gold Elite membership? ",
    '9':"What is the minimum number of nights per year required for Platinum Elite membership? ",
    '10':"What is the minimum number of nights per year required for Titanium Elite membership? ",
    '11':"What is the minimum number of nights per year required for Ambassador Elite membership? ",
    # Minimum qualifying spend for Ambassador
    '12':"What number completes the sentence below?\n__k USD is the minimum qualifying spend per year to become an Ambassador Elite member. "
}

# ANSWER DICTIONARY
answer_list = {
    # Member codes
    '1':"Y1",
    '2':"M1",
    '3':"X1",
    '4':"P6",
    '5':"X4",
    '6':"X5",
    # Minimum number of nights
    '7':"10",
    '8':"25",
    '9':"50",
    '10':"75",
    '11':"100",
    # Minimum qualifying spend for Ambassador
    '12':"23"
}

# MAIN
while True:
    current_question_number = 1
    score = 0
        
    print("Welcome to the Marriott Bonvoy quiz!")
    time.sleep(1)        
    how_many_questions = ''

    # Input validation to ensure only a positive integer value    
    while True: 
        try:
            how_many_questions = int(input("How many questions would you like to answer today? "))
            if how_many_questions >= 1:
                break
            else:
                print("Error: Please enter a positive integer only.")
                time.sleep(1)
        except ValueError:
            print("Error: Please enter a positive integer only.")
            time.sleep(1)
    
    # Grammar correction if user only requests 1 question
    if how_many_questions == 1:
        print("OK. Here is " + str(how_many_questions) + " question to test your Marriott Bonvoy knowledge.")
    else:    
        print("OK. Here are " + str(how_many_questions) + " questions to test your Marriott Bonvoy knowledge.")
    time.sleep(2)
    print()

    # Quiz
    while current_question_number <= how_many_questions:
        # Random question key from question_list dictionary 
        current_random_key = str(random.randint(1,len(question_list)))
        current_question = (question_list[current_random_key])
        current_correct_answer = (answer_list[current_random_key])
        user_answer = input('Q' + str(current_question_number) + ": " + current_question)
        
        # Correct answer
        if current_correct_answer.lower() == user_answer.lower():
            score += 1
            print("Correct! + 1 point!")
        # Incorrect answer     
        else:
            print("Incorrect. The correct answer is " + current_correct_answer + '.')
        
        current_question_number += 1
        time.sleep(1)

    # Round over 
    print("\nYour final score is: " + str(score) + " out of " + str(how_many_questions))
    time.sleep(1)
    print("\nWould you like to play again?")
    play_again = input("Press 'Y' to play again or any other key to quit: ")

    if play_again.lower() == 'y':
        print("Here we go again, good luck!")
        time.sleep(2)
        print()
    else:
        print()
        print("Thanks for playing!")
        break

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