from flask import Flask, render_template, request
from summary import summarizer

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
        if request.method == 'POST':
                rawtext = request.form['rawtext']
                summary, originalText, lenOriginal, lenSummary = summarizer(rawtext)
        return render_template('summary.html', summary=summary, originalText=originalText, lenOriginal=lenOriginal, lenSummary=lenSummary)

if __name__ == "__main__":
    app.run(debug=True)