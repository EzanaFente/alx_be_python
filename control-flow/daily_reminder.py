task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is low priority task"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
print(reminder)
    