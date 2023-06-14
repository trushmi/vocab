"""Script to seed database"""

import os 
import crud, model, server

os.system("dropdb vocab.app")
os.system("createdb vocab.app")

model.connect_to_db(server.app)
model.db.create_all()



"""Create user data """
andrew = crud.create_user(fname="Andrew", lname="Monaco", email="andrew@monaco.com", password="andrewinmonaco")
edward = crud.create_user(fname="Edward", lname="Paris", email="edward@paris.com", password="edwardinparis")
monica = crud.create_user(fname="Monica", lname="Colorado", email="monica@colorado.com", password="monicacolorado")


model.db.session.commit()