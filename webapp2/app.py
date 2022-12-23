from flask import Flask, render_template, request, flash
from datetime import datetime
import openai

global inputprompt
global inputprompt2

# Take care of OpenAI API Key
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('/home/bhanu12/Keys/openaiapi.txt')
# API Key handled

app2 = Flask(__name__)
app2.debug = True
app2.secret_key = "testflaskpagenow2"


# Basic page load initiation
@app2.route("/")
def home():
    return render_template("home.html")

# History Page
@app2.route("/history")
def history():
    return render_template("history.html")

# About Page
@app2.route("/about")
def about():
    return render_template("about.html")


# Load GPT response page and pass on variables
@app2.route("/idearesp", methods=["POST", "GET"])
def idearesp():
    # inputprompt = str((request.form['name_input']))
    # inputprompt2 = request.args.get('input_data')
    # inputprompt = request.form.get('input_data')
    inputprompt = str((request.form["input_data"]))

    # # flash(inputprompt)
    # prompt = "Is it going to rain today?"
    prompt = inputprompt
    # # Invoke GPT3, input from text field
    # flash(inputprompt)
    flash(inputprompt)
    gpt3response = gpt3_completion(prompt)
    # flash(gpt3response)
    # Render the webpage with the returned response
    # return render_template("home.html")
    return render_template("home.html", idearesp=prompt, gpt3responseOP=gpt3response)
    
# Write a function for GPT3 Completion component
def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
            prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            return text
    