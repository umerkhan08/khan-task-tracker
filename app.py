tasks = [
    {"title": "Read lecture slides", "done": True},
    {"title": "Complete Python worksheet", "done": False},
    {"title": "Revise Git commands", "done": True}  
]
print("STUDENT TASK TRACKER")
for task in tasks:
    status = "Done" if task["done"] else "To do"
    print(f"- {task['title']}: {status}")
