from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Khemraj Neupane',
        'title': 'My title 1',
        'content': 'Welcome to my first post',
        'date_posted': '17 March, 2020'
    },
    {
        'author': 'Babita Gartaula',
        'title': 'Gartaula title 2',
        'content': 'Here is Babita post',
        'date_posted': '19 March, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
