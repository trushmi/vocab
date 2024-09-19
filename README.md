# In this ReadMe:
* About this project 
* Tech stack
* Features 
* Code samples 
* How to use the app 
* How to run the app

# About 
VOCAB is a full-stack language learning application that enables users to look up and record new words 43% faster, making the learning process 1.77 times quicker. It offers multiple dashboards for organizing words related to specific topics and interactive features for practice and memorization.
![Green and Black Modern Sales Marketing Presentation (2)](https://github.com/trushmi/vocab/assets/88466266/576ce556-45a6-42bb-a7d2-56f7dbff6cb7)

# Tech Stack

- Python
- Flask
- HTML
- CSS
- Jinja
- Javascript
- ReactJS
- PostgreSQL
- SQLAlchemy
    ### API used:
- https://dictionaryapi.dev/
- https://dictionaryapi.com/products/api-spanish-dictionary
- 
# Features

- User authentication
- Daily reminders to practice
- Flashcards
- Support 2 languages: English and Spanish
- Interactive game “Guess the word” by definition
- Multiple dashboards to keep words organized
- Generated definition and audio pronunciations for words

# How to use the app:
* Create account or log in:
<img width="1726" alt="Screenshot 2023-06-14 at 3 13 41 PM" src="https://github.com/trushmi/vocab/assets/88466266/c9a40641-abfc-498d-88fb-66ebf79685db">

* Navigate to the dashboards page and create a new dashboard, specifying the title and language:
<img width="1850" alt="Screenshot 2023-06-14 at 3 24 23 PM" src="https://github.com/trushmi/vocab/assets/88466266/76c67b80-3af2-4201-86de-9ab8b46ec772">

* Navigate to selected dashboard. Add words to the dashboard:

<img width="1684" alt="Screenshot 2023-09-25 at 5 17 59 PM" src="https://github.com/trushmi/vocab/assets/88466266/c39e1528-e431-43e9-a87a-a4ab8612ccaf">

* Practice words with flashcards:
<img width="1850" alt="Screenshot 2023-06-14 at 3 27 03 PM" src="https://github.com/trushmi/vocab/assets/88466266/7f74bbb0-3dbf-4237-b45d-2d867ad3e64f">

* Practice words with “Guess the word” game:
<img width="1849" alt="Screenshot 2023-06-14 at 3 27 14 PM" src="https://github.com/trushmi/vocab/assets/88466266/6a2d7f2d-6a05-49f6-8408-04127fe8cba3">

* Set up daily email reminder to practice:
<img width="1847" alt="Screenshot 2023-06-14 at 3 28 26 PM" src="https://github.com/trushmi/vocab/assets/88466266/7039bba6-a0b6-4aeb-bfd2-42815ab9cc77">
<img width="1664" alt="Screenshot 2023-09-25 at 5 19 56 PM" src="https://github.com/trushmi/vocab/assets/88466266/3e5dbe10-8ba3-4d35-b7e8-6b82a6ef2c10">


# How to Set Up and Run the Project

1.  ### Start by cloning the repository to your local machine:

    ```
    git clone https://github.com/trushmi/vocab.git
    cd your-project-directory-name
    ```

2.  ### Setup the virtual environment:

    Create a virtual environment to manage your project's dependencies separately:

    ```
    virtualenv env
    ```

3.  ### Activate virtual environment

    ```
    source env/bin/activate
    ```

4.  ### Install all requirements

    Install the project requirements:

    ```
    pip3 install -r requirements.txt
    ```

5.  ### Configure Environment Variables

    Create a secrets.sh file in your project directory to store sensitive information

6.  ### Edit secrets.sh to include the following environment variables:

    ```
    export PASSWORD="your_password_to_gmail_here"
    export EMAIL=”your_email_to_send_reminders_to_user_here”
    export SPANISHAPIKEY=”your_API_KEY_to_generate_meaning_in_spanish_here”
    ```

7.  ### Load the environment variables:

    ```
    source secrets.sh
    ```

8.  ### Set up the database:

   ```
   createdb "name_of_database"
   ```

If the database is created successfully, you should see the following message in your terminal: "You are connected to the database.

9.  ### Set up the database tables:

   ```
   python3 model.py
   ```

10. ### Run the Application

    Now, start the server:

    ```
    python3 server.py
    ```

11. ### Access the App

    Open your web browser and navigate to the following address to access the app:

    ```
    http://localhost:5000/
    ```

You should now see the application running. 

If you encounter any issues, please check that all previous steps have been followed correctly.



