from flask import Flask, render_template, request

app = Flask(__name__)

# Load questions and answers from the text file
def load_questions(filename='questions.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip().split('|') for line in lines]
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found

questions_and_answers = load_questions()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Chatbot endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']

    # Search for the user's question in the loaded questions
    response = get_answer(user_input)
    
    return response  # Only return the text content, not the entire HTML document

def get_answer(user_input):
    for question, answer in questions_and_answers:
        if question.lower() in user_input.lower():
            return answer
    return "I'm sorry, I don't have an answer for that question."

if __name__ == '__main__':
    app.run(debug=True)
