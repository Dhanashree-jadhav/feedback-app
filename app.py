from flask import Flask, render_template, request

app = Flask(__name__)

feedback_list = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        feedback = request.form['feedback']
        feedback_list.append(feedback)
    return render_template('index.html', feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
