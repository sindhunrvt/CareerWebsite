from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    #return render_template('index.html')
    return "Hello World from Flask API!"


'''@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
'''
if __name__ == '__main__':  #If the script is invoked directly (not imported as a module), run the Flask app
    # Configure for Replit environment
    app.run(host='0.0.0.0', port=5000, debug=True)
