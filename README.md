### In this ReadMe:
- [About this project](#about-this-project)
- [Tech stack](#tech-stack)
- [Features](#features)
- [Code samples](#code-samples)
- [How to use the app](#how-to-use-the-app)
- [How to run the app](#how-to-run-the-app)

# About this project 
VOCAB is a full-stack language learning application that enables users to look up and record new words 43% faster, making the learning process 1.77 times quicker. It offers multiple dashboards for organizing words related to specific topics and interactive features for practice and memorization.
![Screenshot of two pages of the app: sign in and dashboards page displayed on one slide](https://github.com/user-attachments/assets/a960fe96-fa66-4850-8aea-8029b78ece20)

# Tech Stack


### Frontend:
- HTML
- CSS
- JavaScript
- ReactJS

### Backend:
- Python
- Flask
- Jinja
- SQLAlchemy

### Database:
- PostgreSQL
  
### API:
- [Free Dictionary API](https://dictionaryapi.dev/)
- [Merriam-Webster Spanish Dictionary API](https://dictionaryapi.com/products/api-spanish-dictionary)

# Features

- User authentication
- Daily reminders to practice
- Flashcards
- Support 2 languages: English and Spanish
- Interactive game “Guess the word” by definition
- Multiple dashboards to keep words organized
- Generated definition and audio pronunciations for words

# How to use the app:
### 1. Create an account or log in
- On the sign-in page, enter your credentials to access the app.

<img width="1726" alt="The sign-in page where users enter their credentials to access the app." src="https://github.com/trushmi/vocab/assets/88466266/c9a40641-abfc-498d-88fb-66ebf79685db">

### 2. Navigate to the dashboards page
- Once logged in, go to the dashboards page.
- Click on the option to create a new dashboard, specifying the title and language for your dashboard.
- See your current list of dashboards.
<img width="1726" alt="The dashboards page displaying various categories of words organized by topic." src="https://github.com/trushmi/vocab/assets/88466266/76c67b80-3af2-4201-86de-9ab8b46ec772">

### 3. Navigate to the selected dashboard
- Add words to your dashboard by typing the word in the corresponding field and pressing the "Generate Meaning" button to get the description and audio pronunciation of the word. Then, press the "Add" button to include it in your dashboard.

<img width="1726" alt="A selected dashboard with fields to search for a word, its meaning, and a button to add the word. Below, a list of saved words is displayed with audio playback functionality." src="https://github.com/trushmi/vocab/assets/88466266/c39e1528-e431-43e9-a87a-a4ab8612ccaf">

### 4. Practice words with flashcards
- Use the flashcards feature to reinforce your vocabulary.
<img width="1726" alt="Flashcards page." src="https://github.com/trushmi/vocab/assets/88466266/7f74bbb0-3dbf-4237-b45d-2d867ad3e64f">

### 5. Play the “Guess the Word” game
- Test your knowledge with the "Guess the word" game.
<img width="1726" alt="Guess the word page." src="https://github.com/trushmi/vocab/assets/88466266/6a2d7f2d-6a05-49f6-8408-04127fe8cba3">

### 6. Set up daily email reminders to practice
- Navigate to your profile page to configure daily email reminders for practicing vocabulary.
<img width="1726" alt="Profile page where the user can toggle the button to set up or cancel a daily reminder to practice vocabulary." src="https://github.com/trushmi/vocab/assets/88466266/7039bba6-a0b6-4aeb-bfd2-42815ab9cc77">

<img width="1726" alt="Screenshot of a Gmail inbox where messages to practice vocabulary are displayed" src="https://github.com/trushmi/vocab/assets/88466266/3e5dbe10-8ba3-4d35-b7e8-6b82a6ef2c10">


# How to run the app:  
Follow the next 12 steps to set up and run the app on your local machine: 

1. ### Clone the repository to your local machine:
    ```
    git clone https://github.com/trushmi/vocab.git
    ```
2. ### Navigate to your project directory:
   ```
   cd your-project-directory-name
   ```
3. ### Setup the virtual environment to manage your project's dependencies separately:
    ```
    virtualenv env
    ```
4. ### Activate virtual environment:
    ```
    source env/bin/activate
    ```

5. ### Install the project requirements:
    ```
    pip3 install -r requirements.txt
    ```
6. ###  Create a secrets.sh file in your project directory to store sensitive information

7. ### Include the following environment variables into secrets.sh file:
    ```
    export PASSWORD="your_password_to_gmail_here"
    export EMAIL=”your_email_to_send_reminders_to_user_here”
    export SPANISHAPIKEY=”your_API_KEY_to_generate_meaning_in_spanish_here”
    ```
8. ### Load the environment variables:
    ```
    source secrets.sh
    ```
9. ### Set up the database:
   ```
   createdb "name_of_database"
   ```
9. ### Set up the database tables:
   ```
   python3 model.py
   ```
10. ### Run the Application
    ```
    python3 server.py
    ```

11. ### Open your web browser and navigate to the following address
    ```
    http://localhost:5000/
    ```


You should now see the application running. 
If you encounter any issues, please check that all previous steps have been followed correctly.



