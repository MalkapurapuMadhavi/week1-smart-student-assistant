from datetime import datetime
import random

name = input("Enter your name: ")

study_tips = [
    "Study for 25 minutes and take a 5-minute break.",
    "Revise your notes daily.",
    "Practice coding every day.",
    "Make a timetable and follow it."
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself.",
    "Never stop learning.",
    "Dream big and work hard."
]

print("\nWelcome,", name)
print("Current Date and Time:", datetime.now())

print("\nStudy Tip:")
print(random.choice(study_tips))

print("\nMotivational Quote:")
print(random.choice(quotes))

with open("session_log.txt", "a") as file:
    file.write(f"{name} logged in at {datetime.now()}\n")

print("\nSession saved successfully.")