from flask import Flask, render_template

app = Flask(__name__)

volunteers = [
    {"name": "Renad", "team": "HR"},
    {"name": "Alex", "team": "Nutrition"},
    {"name": "Youssef", "team": "Media"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/volunteers')
def volunteer_page():
    return render_template('volunteers.html', volunteers=volunteers)

@app.route('/donations')
def donations():
    return render_template('donations.html')

@app.route('/events')
def events():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
