import threading
import time

import schedule
import crud
import email_utils

def run_continuously(interval=30):
    
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


def background_job(app):
    with app.app_context(): 
        user_info = crud.get_users_list_and_data_to_send_reminder()
        print(user_info)
        email_utils.send_email(user_info, "Your vocabulary")

def start_shedule_thread(app):
        schedule.every().day.at("15:20").do(background_job, app)
        run_continuously(1)