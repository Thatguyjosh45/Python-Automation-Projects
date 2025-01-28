import os
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Function to show all tasks
def show_tasks():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour current tasks:")
            for task in tasks:
                print(task.strip())

# Function to add a task
def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(f"{len(open('todo.txt').readlines()) + 1}. {task}\n")
    print(f"Task '{task}' added!")

# Function to mark task as done
def mark_done(task_number):
    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    with open("todo.txt", "w") as file:
        for i, task in enumerate(tasks):
            if i + 1 != task_number:
                file.write(task)
            else:
                print(f"Task {task_number} marked as completed!")

# Function to send a reminder email
def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"  # Don't hardcode this in real scripts, use environment variables

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
    print("Reminder sent!")

# Function to check for reminders (every day, for example)
def daily_reminder():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        # Set reminder time
        reminder_time = "09:00"  # You can change this to any time you want

        if current_time == reminder_time:
            with open("todo.txt", "r") as file:
                tasks = file.readlines()
            if tasks:
                send_email("Daily To-Do Reminder", "\n".join(tasks), "your_email@example.com")
            else:
                send_email("Daily To-Do Reminder", "No tasks for today!", "your_email@example.com")
            time.sleep(60)  # Wait 60 seconds before checking time again
        time.sleep(1)

# Main Menu
def menu():
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as done: "))
            mark_done(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the main menu
menu()
