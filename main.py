import os
from dotenv import load_dotenv

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

open_admin = input("do you want to open admin mode? yes/no: ")

if open_admin == "yes":
    entered_password = input("enter admin password: ")
    
    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")


name = input("Welcome. Please enter your name: ")
new_task = input("Please enter your new task: ")

tasks = []

tasks.append(f"""___
      -Title: {new_task}
      -Status: Pending...
___""")

new_task = input("Please enter your new task: ")

tasks.append(f"""___
      -Title: {new_task}
      -Status: Pending...
___""")

new_task = input("Please enter your new task: ")

tasks.append(f"""___
      -Title: {new_task}
      -Status: Pending...
___""")

with open("task.txt", "a") as file:
    file.write(f"Name: {name} | All tasks: {tasks}")