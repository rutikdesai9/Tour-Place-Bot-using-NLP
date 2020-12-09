from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import Chatbot
import utilis
app = Flask(__name__)
ENV = 'prod'
if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/user-responses'
else:
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://negvtolbbjelqr:e4b4d8c810c381dc09621a6ee1c595a543998a133d8b98e677179091717b466f@ec2-54-243-67-199.compute-1.amazonaws.com:5432/d7hpd1p5ohe4i9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String(200), unique=True)

    def __init__(self, response):
        self.response = response
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def chat():
    flag = True
    while (flag == True):
        user_response = request.args.get('msg')
       
        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you' or 'thank' in user_response ):
                flag = False
                response = "You are welcome.."
                return response
            else:
                if (Chatbot.greeting(user_response) != None):
                    response = Chatbot.greeting(user_response)
                    return response
                else:

                    response = Chatbot.response(user_response)
                    Chatbot.sent_tokens.remove(user_response)
                    return response
        else:
            flag = False
            response = "Goodbye! Enjoy Travelling!!"
            return response
			
			
if __name__ == "__main__":
    app.run()
