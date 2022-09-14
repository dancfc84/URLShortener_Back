
from app import app, db
from models.data import link_data

with app.app_context():
    
  try:
    print("Recreating DB")
    db.drop_all() #removing eberything from the db
    db.create_all() #This will create the tables in the db

    print("seeding our database")

    db.session.add_all(link_data) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit


  except Exception as e:
    print(e)