import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def ask_question(questions, variable_name):
    print(f'AI: "Welcome to MindBot"')
    print(f'AI: "Are you facing unusual behavior with your kid?"')
    response = input("You: ")
    while response.lower() != 'no':
        print(f'AI: "{questions}"')
        response = input("You: ")
        print("AI: Okay then, how can I help you?")
    print(f'AI: "I am going to ask you some questions, are you ready?"')
    response = input("You: ")
    print(" ")
    return {variable_name: response}

@app.route('/')
def home():
    # Read questions from CSV
    questions_list = []
    with open('General.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions_list.append({
                'Question': row['Questions'],
                'Response': row['Response']
            })

    return render_template('MindBot.html', questions=questions_list)

if __name__ == '__main__':
    app.run(debug=True)
