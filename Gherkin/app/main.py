import os
from flask import Blueprint, request, jsonify, render_template
import openai
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

main = Blueprint('main', __name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Set the API key directly
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-proj-xQGTQXVJcNJaY964y0EfT3BlbkFJlubKy2h7jFA1aqrF8MUB")

# Load the data and train the model
data = pd.read_csv('C:\\Gherkin\\data\\gherkin_data.csv')
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['user_input'])

def match_user_input_to_gherkin(user_input):
    user_input_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_input_vector, X)
    most_similar_index = similarities.argmax()
    return data.iloc[most_similar_index]['gherkin_scenario']

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user_input = request.form['user_input']
            logging.debug(f"Received user input: {user_input}")
            gherkin = match_user_input_to_gherkin(user_input)

            # Check if the gherkin is similar enough or generate a new one
            user_input_vector = vectorizer.transform([user_input])
            similarities = cosine_similarity(user_input_vector, X)
            most_similar_index = similarities.argmax()
            if similarities[0][most_similar_index] < 0.5:  # similarity threshold
                logging.debug("Generating new Gherkin scenario using OpenAI API")
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an assistant that helps generate Gherkin scenarios for user stories."
                        },
                        {
                            "role": "user",
                            "content": f"Generate a Gherkin scenario for the user story: {user_input}"
                        }
                    ],
                    max_tokens=150
                )
                gherkin = response['choices'][0]['message']['content'].strip()
                logging.debug(f"Generated Gherkin scenario: {gherkin}")
            return render_template('index.html', user_input=user_input, gherkin=gherkin)
        except Exception as e:
            logging.error(f"Error processing user input: {e}")
            return render_template('index.html', user_input=user_input, gherkin="An error occurred. Please try again.")
    return render_template('index.html')

@main.route('/health', methods=['GET'])
def health_check():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that helps generate Gherkin scenarios for user stories."
                },
                {
                    "role": "user",
                    "content": "This is a test prompt to check if OpenAI API is working."
                }
            ],
            max_tokens=5
        )
        return jsonify({"status": "success", "message": "OpenAI API is working fine.", "response": response['choices'][0]['message']['content'].strip()})
    except openai.error.OpenAIError as e:
        if "You exceeded your current quota" in str(e):
            return jsonify({"status": "error", "message": "You exceeded your current quota. Please check your plan and billing details.", "details": str(e)}), 402
        else:
            return jsonify({"status": "error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
