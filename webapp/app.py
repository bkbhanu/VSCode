from flask import Flask, render_template, request, flash
# from flask_navigation import Navigation
import openai

global inputprompt

# Take care of OpenAI API Key
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('/home/bhanu12/Keys/openaiapi.txt')
# API Key handled

app = Flask(__name__)
app.secret_key = "testflaskpagenow"
# nav = Navigation(app)


# Basic page load initiation
@app.route("/home")
def index():
    return render_template("index.html")

# Load GPT response page and pass on variables
@app.route("/idearesp", methods=["POST", "GET"])
def idearesp():
    inputprompt = (request.form['name_input'])
    # flash(inputprompt)
    prompt = inputprompt
    # Invoke GPT3, input from text field
    gpt3response = gpt3_completion(prompt)
    # flash(gpt3response)
    # Render the webpage with the returned response
    return render_template("index.html", idearesp=prompt, gpt3responseOP=gpt3response)
    
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

@app.route("/history", methods=["POST", "GET"])
def history():
    # form = responsepage();
    # DateTime = datetime.now()
    # input = request.form.get
    # gptoutput = request.form.get("gptoutput")
    gptoutput = request.form.get("gpt3responseOPT")
    # request.
    return render_template("history.html", disoutput=gptoutput)
    # return render_template("history.html", dtime=DateTime, disoutput=gptoutput)