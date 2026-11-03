tasks = [
    {"title": "Read lecture slides", "done": True},
    {"title": "Complete Python worksheet", "done": True},
    {"title": "Revise Git commands", "done": True}  
]
print("STUDENT TASK TRACKER")
for task in tasks:
    status = "Done" if task["done"] else "To do"
    print(f"- {task['title']}: {status}")
completed = sum(1 for task in tasks if task["done"])
print(f"Completed tasks: {completed}/{len(tasks)}")
 
