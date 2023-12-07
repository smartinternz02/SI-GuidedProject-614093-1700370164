from flask import Flask, render_template, request, jsonify
from gensim.summarization import summarize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarizer():
    if request.method == 'POST':
        text = request.form['text']  # Get the text input from the form

        # Perform text summarization
        summarized_text = summarize(text)

        return jsonify({'summary': summarized_text})

if __name__ == '__main__':
    app.run(debug=False)