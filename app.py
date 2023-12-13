from flask import Flask, render_template, request
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest

app = Flask(__name__)

@app.route("/")
def homes():
    return render_template('index.html', predictionText='')  # Initial rendering with an empty predictionText

@app.route("/summary", methods=['POST'])
def summary():
    stopWords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = request.form['text']
    print(doc)
    
    docs = nlp(doc)
    tokens = [i.text for i in docs]
    
    word_frequencies = {}
    
    for word in docs:
        if word.text.lower() not in stopWords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
    
    maxFrequency = max(word_frequencies.values())
    
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maxFrequency
    
    sent_tokenz = [sent for sent in docs.sents]
    sentence_score = {}
    
    for sent in sent_tokenz:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_score.keys():
                    sentence_score[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_score[sent] += word_frequencies[word.text.lower()]
    
    select_len = int(len(sent_tokenz) * 0.3)
    summary = nlargest(select_len, sentence_score, key=sentence_score.get)
    summary_text = ' '.join([word.text for word in summary])
    
    return render_template('index.html', predictionText=summary_text)

if __name__ == "__main__":
    app.run(debug=True)
