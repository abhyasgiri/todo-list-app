from application import app, db
from application.models import Tasks

@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all()               #to view my tasks READ
    output = ""
    if len(all_tasks) == 0                          # or can also write 'if not all_tasks:' 
        return "No tasks have been created"
    else: 
        for task in all_tasks:
            output +=   task.description + " - Completed?" + str(task.completed) "<br>"     #lists all tasks in homepage
        return str(all_tasks)

@app.route("/create")                       #to add a new task CREATE
def create():
    new_todo = Tasks(description = "New Task")
    db.session.add(new_todo)
    db.session.commit()
    return "New task added" 

@app.route("/complete/<int:id>")            #to set a task to do as complete
def complete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return f"Task {id} is now complete"

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Tasks.query.filter_by(id=id),first()
    task.completed = False
    db.session.commit()
    return f"Task {id} is incomplete"

@app.route("/update/new_description>")              #to update something on the to do list
def update(new_description):
    task = Tasks.query.order_by(Tasks.id.desc()).first()
    task.description = new_description
    db.session.commit()
    return f"Most recent taks was updated with the decription: {new_description}"

@app.route("/delete/<int:id>")
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} was deleted."

