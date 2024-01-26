from flask import Flask, render_template, request, jsonify
import csv
import time

app = Flask(__name__)

@app.route('/questions')
def index():
    return render_template('MindBot.html')

def ask_question(questions, variable_name):
    print(f'AI: "{questions}"')
    response = input("You: ")
    print(" ")
    return {variable_name: response}

@app.route('/questions', methods=['POST'])
def process_questions():
    with open('General.csv', 'r') as file:
        reader = csv.DictReader(file)
        question_info_list = []
        for row in reader:
            question_info = ask_question(row['Questions'], row['Response'])
            question_info_list.append(question_info)
            # You can use question_info dictionary as needed (e.g., saving to a database)

    return render_template('result.html', question_info_list=question_info_list)

if __name__ == '__main__':
    app.run(debug=True)
