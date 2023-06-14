from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify, json

import os

from model import connect_to_db
import crud
import reminder_scheduler
from jinja2 import StrictUndefined


app = Flask(__name__)   
app.app_context().push()
app.secret_key = "secret"
app.jinja_env.undefined = StrictUndefined
spanish_key = os.environ['SPANISHAPIKEY']



@app.route("/")
def index():
    if "id" in session:
        return redirect(url_for("show_dashboards"))
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET"])
def signup_page():
    if "id" in session:
        flash("You are already signed up")
        return redirect(url_for("show_dashboards"))
    else:
        return render_template("signup.html")
    

@app.route("/signup", methods=["POST"])
def signup():
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        if first_name and last_name and email and password:
            user = crud.create_user(first_name, last_name, email, password)
            session["id"] = user.user_id
            flash("Account is created")
            return redirect(url_for("show_dashboards"))  
        else:
            flash("Something went wrong! Try again")
            return redirect(url_for("signup_page"))



@app.route("/login", methods=["GET"])
def login_page():
    if "id" in session:
        flash("You already logged in")
        return redirect(url_for("show_dashboards"))
    else:
        return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
        email = request.form.get("email")
        password = request.form.get("password")
        user = crud.get_user_by_email(email)
        if user and password:
            if user.password != password:
                flash("Wrong password! Try again")
                return redirect(url_for("login_page")) 
            else:
                session["id"] = user.user_id
                return redirect(url_for("show_dashboards"))
        else:
            flash("Something went wrong! Try again")
            return redirect(url_for("login_page"))


@app.route("/dashboards", methods=["GET"])
def show_dashboards():
    if "id" not in session:
        flash("Oops! You must sign in first")
        return redirect(url_for("login"))
    else:
        user_id = session["id"]
        dashboards = crud.get_all_user_dashboards(user_id)
        supported_languages=[
            {"label":"English", "value": "en"},
            {"label":"Spanish", "value": "es"},
            {"label":"Other", "value": "other"}
        ]
        return render_template("dashboards.html",dashboards=dashboards, supported_languages=supported_languages)
    
@app.route("/create-dashboard", methods=["POST"])
def create_dashboard():
        user_id = session["id"]    
        title = request.form.get("dashboard_name")
        language = request.form.get("selected_language")
        if title:
            crud.create_dashboard(title, user_id,language)
            return redirect(url_for("show_dashboards"))
        

@app.route("/dashboards/<dashboard_id>")
def show_dashboard(dashboard_id):
    dashboard = crud.get_dashboard_by_id(dashboard_id)
    words =  crud.get_all_words_from_dashboard(dashboard_id)
    language = dashboard.language
    return render_template("dashboard.html",dashboard=dashboard,words=words,language=language,spanish_key=spanish_key)


@app.route("/delete-dashboard", methods=["POST"])
def delete_dashboard():
        dashboard_id = request.form.get("dashboard_id")
        if dashboard_id:
            crud.delete_dashboard(dashboard_id)
            return redirect(url_for("show_dashboards"))


@app.route("/edit-dashboard", methods=["POST"])
def edit_dashboard():
     dashboard_id = request.form.get("dashboard_id")
     new_title = request.form.get("new_title")
     new_language = request.form.get("selected_language")
     if dashboard_id:
          crud.edit_dashboard(dashboard_id, new_title, new_language)
          return redirect(url_for("show_dashboards"))


@app.route("/edit-definition/<int:dashboard_id>", methods=["POST"])
def edit_word_definition(dashboard_id):
        word_id = request.form.get("word_id")
        new_definition = request.form.get("new_definition")

        if new_definition and word_id:
            crud.update_word_definition(word_id,new_definition)
            return redirect(url_for("show_dashboard", dashboard_id=dashboard_id))
        

@app.route("/add-word/<int:dashboard_id>", methods=["POST"])
def add_word(dashboard_id):
        user_id = session["id"]    
        word = request.form.get("word")
        definition = request.form.get("definition")
        audio = request.form.get("audio")
        if word and user_id:
            word = crud.create_word(word, definition, audio, dashboard_id)
            return redirect(url_for("show_dashboard", dashboard_id=dashboard_id))


@app.route("/delete-word/<int:dashboard_id>", methods=["POST"])
def delete_word(dashboard_id):
        word_id = request.form.get("word_id")
        if word_id:
            crud.delete_word(word_id)
            return redirect(url_for("show_dashboard", dashboard_id=dashboard_id))


@app.route("/api/flashcards")
def get_flashcards():
     if "id" not in session:
        return redirect(url_for("index"))
     else:
        user_id = session["id"]
        dashboards = crud.get_all_user_dashboards(user_id)
        all_dashboards = []
        all_words = []
        for board in dashboards:
            
            for word in board.words:
                all_words.append({
                    "term": word.term,
                    "definition": word.definition
                })
            all_dashboards.append({
                "title": board.dashboard_title,
                "id": board.dashboard_id,
                "words": all_words,
                "language": board.language
            })
            all_words = []
        return jsonify(all_dashboards)


@app.route("/flashcards")
def show_flashcards():
    if "id" not in session:
        flash("Oops! You must sign in first")
        return redirect(url_for("login"))
    else:
        return render_template("flashcards.html")
    

@app.route("/guessWordPage")
def guessing_page():
    if "id" not in session:
        # flash("Oops! You must sign in first")
        return redirect(url_for("login"))
    else:
        return render_template("guessWordPage.html")


@app.route("/profile", methods=["GET"])
def show_profile():
    if "id" not in session:
        flash("Oops! You must sign in first")
        return redirect(url_for("login"))
    else:
        user_id = session["id"]
        user = crud.get_user_by_id(user_id)
        return render_template("profile.html",user=user)

@app.route("/profile", methods=["POST"])
def cnange_reminding_settings():
    if "id" not in session:
        flash("Oops! You must sign in first")
        return redirect(url_for("login"))
    else:
        user_id = session["id"]
        user = crud.get_user_by_id(user_id)
        reminder_status = request.form.get("reminder_status")
        print('this is reminder status:', reminder_status)
        if reminder_status:
            crud.turn_on_reminder(user_id)
            print(crud.is_reminder_true(user_id))
            flash("Done! Now you will receive reminders to practise your vocabulary on your email")
        else: 
            crud.turn_off_reminder(user_id)
            flash("Done! No more reminders")
        print('this is value in model:', user.send_reminder)
        return render_template("profile.html",user=user)


@app.route("/logout")
def logout():
    session.pop("id", None)
    flash("You have been successfully logged out")
    return redirect(url_for("index"))


if __name__ == '__main__':
    connect_to_db(app)
    reminder_scheduler.start_shedule_thread(app)
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
    