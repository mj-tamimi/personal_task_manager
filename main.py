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

while True:
    new_task = input("Enter a task (or 'q' to quit): ")
    if new_task.lower() == "q":
        break
    
    if True:
        q1 = input("Is the task done? (y/n)")
        delete = input("Do you want to delete the task? (y/n)")
        
        if delete == "y" or delete == "yes":
            print("Task deleted.")
            break
        else:
            if q1 == "y" or q1 == "yes":
                tasks.append(f"  -Title: {new_task}\n  -Status: Done\n Validation: Medium")
            else:
                tasks.append(f"  -Title: {new_task}\n  -Status: Pending...\n Validation: Medium")
        
        


with open("task.txt", "a") as file:
    file.write(f"Name: {name} | All tasks: {tasks}\n")