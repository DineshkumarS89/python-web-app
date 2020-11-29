from flask import Flask, request, render_template
import logging

app = Flask(__name__)
app.config['env'] = 'Development'

FORMAT = '%(asctime)-15s %(thread)d - %(message)s'
logging.basicConfig(format=FORMAT,filename='output.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    try:
        input1 = request.form['First']
        res = "Hello " + input1 + " !!!!"
        return res
    except ValueError as v:
        logger.error("Unable to handle the input form" + str(v))
        return "Incorrect input"
    except RuntimeError as r:
        logger.error("Run time exception while processing the request" + str(r))
        return "Runtime exception"
if __name__ == '__main__':
    app.run()