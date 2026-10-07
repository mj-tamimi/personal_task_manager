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
    file.write(f"All tasks: {tasks}")