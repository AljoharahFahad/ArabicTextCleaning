from flask import Flask, render_template, request

app = Flask(__name__)

def clean_text(text):
    cleaned_text = text.lower()
    return cleaned_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clean', methods=['POST'])
def clean():
    text = request.form['text']
    cleaned_text = clean_text(text)
    return render_template('result.html', cleaned_text=cleaned_text)

if __name__ == '__main__':
    app.run()
