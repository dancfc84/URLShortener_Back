from app import db
from datetime import *

# * A class that has all the COMMON fields
# * that EVERY model will use the columns declared below

class BaseModel:

  id = db.Column(db.Integer, primary_key=True) #assigns a unique key 

  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

  #Add a method here to save my model to the database
  
  def save(self):
    db.session.add(self)
    db.session.commit()

  #This adds a method for remove

   # ! Add a method to remove
  def remove(self):
    db.session.delete(self)
    db.session.commit()
