from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db/test.db'
db = SQLAlchemy(app)


# database modle
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %i>' % self.id

    
# get route
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        tasks = Todo.query.order_by(Todo.date_created)
        return render_template("index.html", tasks=tasks)
    else:
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:            
            return "Failed to insert new task.."

# delete route
@app.route('/delete/<int:id>')
def delete(id):
    delete_task = Todo.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
    except:
        return "Unable to delete task.."
    return redirect('/')


# update route
@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'GET':
        return render_template("update.html", task=task)

    elif request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:            
            return "Failed to insert new task.."
    
    else:
        return "Invalid Request"


# main 
if __name__ == "__main__":
    app.run(debug=True, host="sqlite3", port=5000)

