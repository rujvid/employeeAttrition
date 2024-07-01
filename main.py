from flask import Flask, render_template, request
from translate import *
from sentAnalysis import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method =='POST':
        phrase = request.form.get('inputPhrase')
        selLanguage = request.form.get('selected_language', None)

        if selLanguage is not None:
            lang = selLanguage
            change = do_translate(phrase, lang)
            sent = do_sentiment_analysis(phrase)
            
            negResult=sent[0]
            neuResult=sent[1]
            posResult=sent[2]

    return render_template('index.html', input=input, lang=lang, translate=change, sentiment=sent, neg=negResult, neu=neuResult, pos=posResult)

if __name__ == '__main__':
        app.run(debug=True)
        