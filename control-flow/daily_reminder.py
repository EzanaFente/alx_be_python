task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match Priority:
        case "low":
            PriorityMsg = f"{task} is a low priority task. Consider completing it when you have free time."
        case "high":
            reminder = f"{task} is a high priority task that requires immediate attention today!"
            PriorityMsg = reminder
        case "medium":
            PriorityMsg = f"{task} is a medium priority task."
if time_bound == "yes" and Priority == "high":
        print("Reminder: ", reminder)
elif time_bound == "no" and Priority == "low":
        print(f"Note: {PriorityMsg}")
