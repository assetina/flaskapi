from flask import Flask
from flask_mail import Mail, Message
from flask import request



app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'brightlembo91@gmail.com',
    "MAIL_PASSWORD": 'bmofksqydkstdlea',
    "MAIL_SUPPRESS_SEND": False,
    'MAIL_DEFAULT_SENDER': 'brightlembo91@gmail.com'
    
}

tableau=["haine", "hair","hais","haissent"]
#app.config['TESTING'] = False
app.config.update(mail_settings)
mail = Mail(app)
app.debug= True
@app.route("/envoyermail", methods=['POST'])
def index():
    data = request.form
    sujet= data["sujet"]
    nom= data["nom"]
    email= data["email"]
    corps= data["corps"]
    liste= corps.split(" ")
    s=0
    n=0
    moyenne=0
    for l in liste:
        for t in tableau:
            if l==t:
                s+=50
                n+=1
                if n==0:
                    moyenne=s
                else:
                    moyenne=s/n
    if moyenne <50:
            
        msg = Message(subject=sujet,
            recipients=["consultmary0@gmail.com"], # use your email for testing
            body="DE: "+email+" \n Nom complet: "+nom+" \n Message: "+corps+"`\n",
            sender=app.config.get("brightlembo91@gmail.com"))
        mail.send(msg)
        
        return "email envoyé"
    else:
        return "impossible"

#app.run(debug = True, port = 5000)