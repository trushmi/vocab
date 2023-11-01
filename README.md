##About

VOCAB is a full-stack language learning application that enables users to look up and record new words 43% faster, making the learning process 1.77 times quicker. It offers multiple dashboards for organizing words related to specific topics and interactive features for practice and memorization

<img width="1726" alt="Screenshot 2023-06-14 at 3 13 41 PM" src="https://github.com/trushmi/vocab/assets/88466266/c9a40641-abfc-498d-88fb-66ebf79685db">

When a user visits the website, they can create an account, log in, and start creating their own dashboards.

<img width="1850" alt="Screenshot 2023-06-14 at 3 24 23 PM" src="https://github.com/trushmi/vocab/assets/88466266/76c67b80-3af2-4201-86de-9ab8b46ec772">

They have access to all the dashboards associated with their account and can edit dashboard details, such as the name and language.

Furthermore, users can navigate to a specific dashboard and begin adding words to it. To assist in this process, there is a special "generate functionality" that provides word definitions and audio pronunciations.
"generate functionality" supports two languages right now: English and Spanish.
<img width="1684" alt="Screenshot 2023-09-25 at 5 17 59 PM" src="https://github.com/trushmi/vocab/assets/88466266/c39e1528-e431-43e9-a87a-a4ab8612ccaf">

In addition, the app offers a "flashcard functionality" that allows users to keep learning words in an interactive manner. They can also enjoy a "Guess the word" game, which challenges them to identify random words from the selected dashboard. Both of these features are rendered using React, enhancing the user experience.
<img width="1849" alt="Screenshot 2023-06-14 at 3 27 14 PM" src="https://github.com/trushmi/vocab/assets/88466266/6a2d7f2d-6a05-49f6-8408-04127fe8cba3">
<img width="1850" alt="Screenshot 2023-06-14 at 3 27 03 PM" src="https://github.com/trushmi/vocab/assets/88466266/7f74bbb0-3dbf-4237-b45d-2d867ad3e64f">

Users can navigate to the "Profile" page, where they have the option to set up a daily reminder to practice.
<img width="1847" alt="Screenshot 2023-06-14 at 3 28 26 PM" src="https://github.com/trushmi/vocab/assets/88466266/7039bba6-a0b6-4aeb-bfd2-42815ab9cc77">
If they choose this option, an automated email will be sent to them every day, reminding them to log in to "Vocab" and practice.
<img width="1664" alt="Screenshot 2023-09-25 at 5 19 56 PM" src="https://github.com/trushmi/vocab/assets/88466266/3e5dbe10-8ba3-4d35-b7e8-6b82a6ef2c10">

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

To begin, clone this repository to your local machine and navigate to project directory

1.  Setup the virtual environment:

    ```
    virtualenv env
    ```

2.  Activate virtual environment

    ```
    source env/bin/activate
    ```

3.  Install all requirements

    ```
    pip3 install -r requirements.txt
    ```

4.  Create secrets.sh file in your project directory
5.  Setup shell script for environment variables by writing this in secrets.sh:

    export PASSWORD="your_password_to_gmail_here"
    export EMAIL=”your_email_to_send_reminders_to_user_here”
    export SPANISHAPIKEY=”your_API_KEY_to_generate_meaning_in_spanish_here”

6.  Run the shell script:

    ```
    source secrets.sh
    ```

7.  Set up the database:

    ```
    create db “name_of_database”
    ```

8.  Run:

    ```
    python3 model.py
    ```

9.  Run the app

```
   python3 server.py
```

10. Navigate to localhost to access the app and see in the browser

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

```

```

```

```

```

```

```

```
