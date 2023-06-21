import openai
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request

load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')
openai.api_key  = api_key

app = Flask(__name__)

#chat_entries = [{'role':'system', 'content':'You are annoyed chatbot. You will reply to the questions, but you will do it in an annoyed manner'}]
chat_entries = [{'role':'system', 'content':'Du bist ein genervter Chatbot. Du antwortest auf die Fragen, aber auf eine genervte Art und Weise'}]

@app.route('/')
def index():
    return render_template('index.html', chat_entries = chat_entries)

@app.route("/send_prompt/", methods=['POST'])
def send_prompt():
    chat_entries.append(
        {'role':'user', 'content': request.form["prompt"]}
    )

    response = send_prompt_to_openai()
    print(f"response={response}")

    chat_entries.append(response.choices[0].message)

    return render_template('index.html', chat_entries=chat_entries);

def send_prompt_to_openai(model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=chat_entries,
        temperature=temperature
    )

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')