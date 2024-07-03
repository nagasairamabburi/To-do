from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - todos stored in memory (in a real app, you'd use a database)
todos = [
    {'id': 1, 'title': 'Learn Flask', 'completed': False},
    {'id': 2, 'title': 'Build a CRUD App', 'completed': False},
]

# Home route - displays all todos
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# Add todo route
@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    new_todo = {'id': len(todos) + 1, 'title': title, 'completed': False}
    todos.append(new_todo)
    return redirect(url_for('index'))

# Update todo route
@app.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = request.form.get('title')
            todo['completed'] = True if request.form.get('completed') == 'on' else False
            break
    return redirect(url_for('index'))

# Delete todo route
@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
