from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """ Data model for user"""
    
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False,unique=True)
    password = db.Column(db.String, nullable=False)
    send_reminder = db.Column(db.Boolean,default=False)    
    dashboards = db.relationship("Dashboard", back_populates="user")

    def __repr__(self):
        return f"User id: {self.user_id}; User email: {self.email}; User lname: {self.lname}"
    
class Dashboard(db.Model):
    """ Data model for dashboard """
    
    __tablename__ = "dashboards"

    dashboard_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dashboard_title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship("User", back_populates="dashboards")
    words = db.relationship("Word", back_populates="dashboard")
    language= db.Column(db.String)

    def __repr__(self):
        return f"Dashboard id: {self.dashboard_id}, title: {self.dashboard_title};"
    

class Word(db.Model):
    """ Data model for word """

    __tablename__ = "words"

    word_id = db.Column(db.Integer,primary_key=True)
    term = db.Column(db.Text)
    definition = db.Column(db.Text)
    audio = db.Column(db.Text)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboards.dashboard_id'))
    dashboard = db.relationship("Dashboard", back_populates="words")

    def __repr__(self):
        return f"Id of the word: {self.word_id}, term: {self.term}" 


def connect_to_db(flask_app, db_uri="postgresql:///vocab_app",echo=True):
    """Connect to database"""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.app = flask_app
    db.init_app(flask_app)
    print("You connect to database")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)

