from cryptography.fernet import Fernet
from firestorePy import firestorePy
from datetime import datetime
import base64

class Manager:
  def __init__(self):
    key = self._get_key()
    self.key = key if key is not False else self._create_key()
    self.pswCollection = 'passwords'
    self.db = firestorePy().get_firestore_instance()

  def _create_key(self):
    key = Fernet.generate_key()
    with open('password.key', 'wb') as passwordFile:
      passwordFile.write(key)
    return open('password.key', 'rb').read()

  def _get_key(self):
    try:
      return open('password.key', 'rb').read()
    except FileNotFoundError as e:
      return False

  def add_password(self, passwordStructure, bot):
    service = passwordStructure.split('::')[0]
    password = (passwordStructure.split('::')[1]).encode()

    f = Fernet(self.key)
    encryptedPsw = base64.b64encode(f.encrypt(password))
    self.db.collection(self.pswCollection).document(service).set({
      'password': encryptedPsw,
      'dateAdded': datetime.now(),
      'active': True
    })
    bot.send_message('psw-added')


  def edit_password(self, passwordStructure, bot):
    service = passwordStructure.split('::')[0]
    newPassword = (passwordStructure.split('::')[1]).encode()

    f = Fernet(self.key)
    encryptedPsw = base64.b64encode(f.encrypt(newPassword))
    doc_ref = self.db.collection(self.pswCollection).document(service)
    docData = doc_ref.get().to_dict()
    if doc_ref.get().exists:
      doc_ref.update({
        'active': True,
        'dateAdded': docData['dateAdded'],
        'password': encryptedPsw,
        'dateModified': datetime.now(),
      })
      bot.send_message('psw-modified')
    else:
      bot.send_message('psw-service-error')


  def get_password(self, service, bot):
    doc_ref = self.db.collection(self.pswCollection).document(service).get()
    if doc_ref.exists:
      passwordBlob = doc_ref.get(field_path= 'password')
      f = Fernet(self.key)
      password = f.decrypt(base64.b64decode(passwordBlob))
      bot.send_message(password)
    else:
      bot.send_message('psw-service-error')


  def delete_password(self, service, bot):
    doc_ref = self.db.collection(self.pswCollection).document(service)
    docData = doc_ref.get().to_dict()
    if doc_ref.get().exists:
      doc_ref.update({
        'active': False,
        'dateAdded': docData['dateAdded'],
        'password': docData['password'],
        'dateRemoved': datetime.now()
      })
      bot.send_message('psw-removed')
    else:
      bot.send_message('psw-service-error')


  def get_services(self, bot):
    collections = self.db.collection(self.pswCollection).get()
    bot.send_message('psw-all-service')
    for doc in collections:
      if doc.get(field_path='active') == True:
        bot.send_message(doc.id)

