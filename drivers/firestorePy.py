import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class firestorePy: 
  def __init__(self):
    firebaseSDK =  credentials.Certificate('codicebot-credentials.json')
    firebase_admin.initialize_app(firebaseSDK)
    db = firestore.client()
    self._db = db

  def get_firestore_instance(self):
    return self._db
