import csv
import time

def ask_question(questions, variable_name):
    print(f'AI: "HI! , welcome to MindBot"')
    input("You: ")
    print(f'AI: "Are you facing unusual behavior with your kid?"')
    input("You: ")
    print(f'AI: "I am going to ask you some questions, are you ready?"')
    input("You: ")
    print("")

    responses = {}
    for question in questions.split(';'):
        print(f'AI: "{question}"')
        response = input("You (yes/no): ").lower()
        while response not in ['yes', 'no']:
            print('AI: "Please answer with either yes or no."')
            response = input("You (yes/no): ").lower()
        responses[question] = response
    
    return {variable_name: responses}

# Read questions from CSV
with open('General.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Extract questions from CSV
    questions = [row['Questions'] for row in reader]

    # Ask questions and get user responses
    question_info = ask_question(';'.join(questions), 'ASD_Response')

    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")

    # Check the responses from the user
    yes_count = sum(response.lower() == 'yes' for response in question_info['ASD_Response'].values())
    if yes_count >= 5:
        print('AI: "Thank you for answering the questions. If you answered with 5 yes or more, then your kid may have ASD. Consulting a specialist will give you a more clear diagnosis."')
    else:
        print('AI: "Thank you for answering the questions. It seems unlikely that your kid has ASD, but consulting a specialist is always a good idea for confirmation."')
