### About project:

Vocab is a full stack application that helps to learn new words faster and easier while keeping them organized in
one place. When a user visits the website, they can create an account, log in, and start creating their own dashboards.
They have access to all the dashboards associated with their account and can edit dashboard details, such as the name and language. Furthermore, users can navigate to a specific dashboard and begin adding words to it. To assist in this process, there is a special "generate functionality" that provides word definitions and audio pronunciations.
"generate functionality" supports two languages right now: English and spanish.

In addition, the app offers a "flashcard functionality" that allows users to keep learning words in an interactive manner. They can also enjoy a "Guess the word" game, which challenges them to identify random words from the selected dashboard. Both of these features are rendered using React, enhancing the user experience.

Users can navigate to the "Profile" page, where they have the option to set up a daily reminder to practice. If they choose this option, an automated email will be sent to them every day, reminding them to log in to "Vocab" and practice.

### Tech Stack

- Python
- Flask
- HTML
- CSS
- Jinja
- Javascript
- ReactJS
- PostgreSQL
- SQLAlchemy

### API:

- https://dictionaryapi.dev/
- https://dictionaryapi.com/products/api-spanish-dictionary

### Features

- Create account
- Log in,Log out
- Create dashboards and select language of dashboard
- Edit dashboard title and language
- Delete dashboard
- Add word to selected dashboard
- Delete word from dashboard
- Daily reminder to practice vocabulary on the email
- Practice words with flashcards from the selected dashboard
- Game “Guess the word” to practice words from certain dashboard and to guess random word by provided definition

### How to Run

To begin, clone this repository to your local machine.

1.  Setup the virtual environment:
    $ virtualenv env

2.  Activate virtual environment
    $ source env/bin/activate

3.  Install all requirements
    $ pip3 install -r requirements.txt

4.  Setup shell script for environment variables by writing this in secrets.sh:

    export PASSWORD="your_password_to_gmail_here"
    export EMAIL=”your_email_to_send_reminders_to_user_here”
    export SPANISHAPIKEY=”your_API_KEY_to_generate_meaning_in_spanish_here”

5.  Run the shell script:
    $ source secrets.sh

6.  Set up the database:
    create db “name_of_database”
    python3 model.py

7.  Run the app
    python3 server.py

8.  Navigate to localhost to access the app and see in the browser

### How to navigate in the app:

1. Create account or log in
2. Create dashboard
3. Navigate to selected dashboard
4. Add words to dashboard
5. Practice words with flashcards
6. Practice words with game “Guess the word”
7. Set up daily reminder to your email to practise vocabulary

### Demo

[Click here](https://www.youtube.com/watch?v=iPlAV7c3YMI) to view the demo video

### Author

Iryna Trush, Software engineer with a strong background in the media industry and leadership.
[LinkedIn](https://www.linkedin.com/in/trushmi/), [email](trushmi415@gmail.com);
