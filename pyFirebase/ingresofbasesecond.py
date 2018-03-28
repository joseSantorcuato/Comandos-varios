import pyrebase
import time
from time import gmtime, strftime


config = {
  "apiKey": "Tu4pikeyqueTEH4BRADADOGOOGL3",
  "authDomain": "tuproyecto-3e3ee3.firebaseapp.com",
  "databaseURL": "https://tuproyecto.firebaseio.com",
  "storageBucket": "tuproyecto-3e3ee3.appspot.com",

}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

user = auth.sign_in_with_email_and_password("tusuarios@sumail.com", "lapasswordsecreta")
db = firebase.database()
usuario=str(user['idToken'])

print (usuario)

while True:
    control = strftime("%S", gmtime())
    print (control)
    controlb = int(control)

    time.sleep( 1 )
    if controlb == 59:
        print ("llegue a 59")
        tutabla = {"campo1": "ok", "campo2": "ok", "campo3": "ok", "campo4": "ok"}
        db.child("campos").push(tutabla, user['idToken'])
