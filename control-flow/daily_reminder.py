task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound_input = input("Is it time-bound? (yes/no): ").strip().lower()
time_bound = time_bound_input

reminder = ""

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"
        
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print("Reminder:", reminder)
else:
    reminder += ". Consider completing it when you have free time"
    print("Note:", reminder)
    