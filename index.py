import random

# Alamu Enoch Ayomide 
# 2022009504

def generate_quiz():
    """Generates a quiz with 20 questions and options."""
    
    questions = [
        "What is the capital of Nigeria?",
        "Who was the first president of Nigeria?",
        "What is the largest state in Nigeria by land area?",
        "Which river is the longest in Nigeria?",
        "When did Nigeria gain independence from Britain?",
        "Who is the current president of Nigeria?",
        "What is the official language of Nigeria?",
        "Which religion is the most widely practiced in Nigeria?",
        "What is the highest mountain in Nigeria?",
        "Which Nigerian football club has won the most CAF Champions League titles?",
        "What is the currency of Nigeria?",
        "Who is the author of the novel 'Things Fall Apart'?",
        "Which Nigerian state is known for its oil production?",
        "What is the name of the traditional Nigerian attire worn by men?",
        "Which Nigerian musician is known as the 'King of Afrobeat'?",
        "What is the name of the Nigerian national dish?",
        "Which Nigerian city is known as the 'Entertainment Capital of Africa'?",
        "What is the name of the Nigerian national football team?",
        "Which Nigerian state is home to the Olumo Rock?",
        "What is the name of the Nigerian national anthem?"
    ]

    options = [
        ["Abuja", "Lagos", "Kano", "Port Harcourt"],
        ["Nnamdi Azikiwe", "Olusegun Obasanjo", "Yakubu Gowon", "Muhammadu Buhari"],
        ["Niger", "Kaduna", "Zamfara", "Borno"],
        ["Niger", "Benue", "Nile", "Congo"],
        ["1960", "1961", "1962", "1963"],
        ["Muhammadu Buhari", "Goodluck Jonathan", "Bola Tinubu", "Atiku Abubakar"],
        ["English", "Yoruba", "Hausa", "Igbo"],
        ["Christianity", "Islam", "Traditional Religions", "Hinduism"],
        ["Mount Kilimanjaro", "Mount Cameroon", "Mount Chappal", "Mount Sardauna"],
        ["Enugu Rangers", "Enyimba International", "Sunshine Stars", "Heartland"],
        ["Naira", "Kobo", "Cedis", "Rands"],
        ["Chinua Achebe", "Wole Soyinka", "Chimamanda Ngozi Adichie", "Ben Okri"],
        ["Delta", "Rivers", "Bayelsa", "Akwa Ibom"],
        ["Agbada", "Buba and wrapper", "Dashiki", "Senators"],
        ["Fela Kuti", "Wizkid", "Davido", "Burna Boy"],
        ["Jollof rice", "Egusi soup", "Amala and Ewedu", "Pounded yam and vegetable soup"],
        ["Lagos", "Abuja", "Port Harcourt", "Enugu"],
        ["Super Eagles", "Green Eagles", "Flying Eagles", "Golden Eagles"],
        ["Kwara", "Ogun", "Oyo", "Lagos"],
        ["Arise, O Compatriots", "Nigeria, Our Fatherland", "Hail, the Hero's", "Lift High the Banner"]
    ]

    correct_answers = [
        "Abuja", "Nnamdi Azikiwe", "Niger", "Niger", "1960", "Bola Tinubu", 
        "English", "Christianity", "Mount Chappal", "Enyimba International", 
        "Naira", "Chinua Achebe", "Delta", "Agbada", "Fela Kuti", 
        "Jollof rice", "Lagos", "Super Eagles", "Ogun", "Arise, O Compatriots"
    ]

    return questions, options, correct_answers

def take_quiz(questions, options, correct_answers):
    """Takes the quiz and returns the user's score."""

    score = 0
    for i in range(len(questions)):
        print(f"\nQuestion {i+1}: {questions[i]}")
        for j, option in enumerate(options[i]):
            print(f"{j+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        
        # Validate user input to ensure it's between 1-4
        while user_answer not in ['1', '2', '3', '4']:
            print("Invalid input. Please enter a number between 1 and 4.")
            user_answer = input("Enter your answer (1-4): ")
        
        # Convert user input to an integer and compare to the correct answer
        user_answer_index = int(user_answer) - 1
        if options[i][user_answer_index] == correct_answers[i]:
            score += 10
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answers[i]}")
    
    return score

def grade_quiz(score):
    """Grades the quiz and returns a letter grade."""
    if score >= 180:
        return "A"
    elif score >= 160:
        return "B"
    elif score >= 140:
        return "C"
    elif score >= 120:
        return "D"
    elif score >= 80:
        return "E"
    else:
        return "F"

def main():
    """Main function to run the quiz."""

    questions, options, correct_answers = generate_quiz()
    score = take_quiz(questions, options, correct_answers)
    print(f"\nYour final score is: {score} out of 200")
    grade = grade_quiz(score)
    print(f"Your grade is: {grade}")

if __name__ == "__main__":
    main()
