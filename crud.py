"""CRUD operations """

from model import db, User, Dashboard, Word, connect_to_db


def create_user (fname, lname, email, password):
    """ Create a new user """

    user = User(fname=fname, lname=lname, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def get_all_user_dashboards(user_id):
  """ Get all dashboards user have by user_id"""

  all_dashboards = Dashboard.query.filter(Dashboard.user_id == user_id).all()
  return all_dashboards

def turn_on_reminder(user_id):
  """ Set a reminder for user """

  user = User.query.get(user_id)
  user.send_reminder = True
  db.session.commit()


def get_users_list_and_data_to_send_reminder():
  """ Get all emails from users who has sen """

  users = User.query.filter(User.send_reminder  == True).all()
  user_info = []
  for user in users:
    user_info.append({'email': user.email, 'name': user.fname})
  return user_info

def turn_off_reminder (user_id):
  """ Turn off a users reminder """

  user = User.query.get(user_id)
  user.send_reminder = False
  db.session.commit()



def is_reminder_true (user_id):
  """ Check if user has reminder turned on  """


  user = User.query.get(user_id)
  return user.send_reminder 

def create_dashboard(dashboard_title,user_id,language):
  """ Create a new dashboard """

  dashboard = Dashboard(dashboard_title=dashboard_title,user_id=user_id,language=language)
  db.session.add(dashboard)
  db.session.commit()
  return dashboard


def create_word(term, definition, audio, dashboard_id):
  """ Create a new word """

  word = Word(term=term,definition=definition, audio=audio, dashboard_id=dashboard_id)
  db.session.add(word)
  db.session.commit()
  return word

def update_word_definition(word_id, new_definition):
  """ Update the word definition using word_id and new_definition provided by user"""

  word = Word.query.filter(Word.word_id == word_id).first()
  word.definition = new_definition
  db.session.commit() 

def delete_word(word_id):
  """ Delete a word """

  word = Word.query.filter(Word.word_id == word_id).first()
  db.session.delete(word)
  db.session.commit()
 
def delete_dashboard(dashboard_id):
  """ Delete a dashboard"""

  dashboard = Dashboard.query.filter(Dashboard.dashboard_id == dashboard_id).first()
  db.session.delete(dashboard)
  db.session.commit()
 


def edit_dashboard(dashboard_id, new_title, new_language):
  """ Edit a title of dashboard"""

  dashboard = Dashboard.query.filter(Dashboard.dashboard_id == dashboard_id).first()
  dashboard.dashboard_title = new_title
  dashboard.language = new_language
  db.session.commit() 

def get_user_by_id(user_id):
  """ Get user by id"""

  return User.query.get(user_id)

def get_user_by_email(email):
  """ Get user by email"""

  return User.query.filter(User.email == email).first()


def get_dashboard_by_id(dashboard_id):
  """ Get user dashboard by dashboard_id"""

  return Dashboard.query.filter(Dashboard.dashboard_id == dashboard_id).first()

def get_dashboard_by_title(title):
  """ Get user dashboard by title"""

  return Dashboard.query.filter(Dashboard.dashboard_title == title).first()


def get_all_words_from_dashboard(dashboard_id):
  """ Get all words from particular dashboard"""
  
  dashboard = Dashboard.query.filter(Dashboard.dashboard_id == dashboard_id).first()
  return dashboard.words



if __name__ == "__main__":
  from server import app
  connect_to_db(app)

