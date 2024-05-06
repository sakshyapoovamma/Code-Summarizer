from flask import Flask, render_template, url_for, request
import openai

app = Flask(__name__)
query = ''
heading = ''


def gpt3(stext):
    openai.api_key = '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'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=stext,
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/second', methods=['POST', 'GET'])
def second():

    global query
    global heading
    output = request.form.to_dict()

    cond = output['sub1']
    query = output['name']

    if(cond == 'Summarize'):
        name = 'summarize my code - ' + query
        heading = "Here's your summary of code."
        result = gpt3(name)
    elif(cond == 'Explain'):
        name = 'Explain my code in detail - ' + query
        heading = "Let me explain the code to you."
        result = gpt3(name)
    elif(cond == 'Debug'):
        name = 'what all are the errors in my code including syntax and logical errors -  '+query
        heading = "These are the errors I've discovered."
        result = gpt3(name)

    return render_template("second.html", name=result)


@app.route('/third', methods=['POST', 'GET'])
def third():
    global query
    global heading
    return render_template("Third.html", name=query, head=heading)


if __name__ == '__main__':
    app.run()
