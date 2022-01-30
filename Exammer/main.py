from flask import (
    url_for, request, redirect,
    render_template, Blueprint
)

import sqlite3
from sqlite_api import TABLE_NAME, DB_PATH, delete_eq
from sqlite_api import get_all, get_eq
from sqlite_api import insert_all
from sqlite_api import delete_eq
from errors import DB

main = Blueprint("main", "Exammer")

@main.route('/', methods=["GET"])
def index():
    r"""Show a list of created questions
    This function shows a list of created questions.
    With two button for `add` and `delete` at top.
    And edit button on each questtion. (future)
    """
    questions = get_all(sqlite3.connect(DB_PATH).cursor(), TABLE_NAME)
    return render_template('index.html', questions=questions, length=len(questions))

@main.route('/', methods=["POST"])
def delete_selected_questions():
    r"""Delete checked (blue) question
    In the box rendered when you visit
    index  page there are a number of
    questions shown with a square in
    their left side. (visitor eyes)
    
    This function executes when you click
    the 'Delete selected questions' button
    even if no question was selected! 
    """
    db = sqlite3.connect(DB_PATH)
    questions = get_all(db.cursor(), TABLE_NAME)
    selected_questions = []

    for question in questions:
        if request.form.get(str(question[0])) == 'on':
            selected_questions.append(question[0])

    for id in selected_questions: # delete selected questions
        delete_eq(db.cursor(), TABLE_NAME, id=id)
    db.commit()
    
    return redirect(url_for('main.index'))

@main.route('/new')
def new_question():
    r"""Render the question view
    This function renders a view contain the question form.
    So user can write new question and send it to $handler.
    """
    return render_template('create.html', handler=url_for('main.add_question'))

@main.route('/add', methods=["POST"])
def add_question():
    r"""Insert the /new view question to DB
    This function checks and verifies the
    data from /new view and if something be
    wrong it will render the 'create.html'
    template with an error-box. otherwise,
    It insert the question to the database
    """
    if request.method == "POST":
        try:
            question = request.form["question"]
            answer1 = request.form["one"]
            answer2 = request.form["two"]
            answer3 = request.form["three"]
            answer4 = request.form["four"]
            correct = request.form["correct"]
        except KeyError:
            error = "All the parameters are required.\n"+\
                "It looks you forgot one!\n"
            return render_template(
                'create.html',
                handler=url_for('main.add_question'),
                error=error
            )

        ##################################################
        # Improve quality of this part.                 #
        #################################################
        # initialize variable error
        error = ''
        # Check $question
        if len(question) < 5:
            error += "Question length is too short.\n"
        # Check $answer%n%
        if len(answer1) < 5:
            error += "First answer length is too short.\n"
        if len(answer2) < 5:
            error += "Second answer length is too short.\n"
        if len(answer3) < 5:
            error += "Third answer length is too short.\n"
        if len(answer4) < 5:
            error += "Fourth answer length is too short.\n"
        # Check $correct
        if correct == 1 or correct == 2 or correct == 3 or correct == 4:
            error += "You have chose an unknown correct answer.\n"
        
        if len(error) > 5:
            return render_template(
                'create.html',
                handler=url_for('main.add_question'),
                error=error.replace("\n","<br>")
            )
        ######################################################
        db = sqlite3.connect(DB_PATH)
        command = f"(NULL, '{question}', '{answer1}', '{answer2}', '{answer3}', '{answer4}', {correct})"
        insert_all(db.cursor(), TABLE_NAME, command)
        db.commit()          
    return redirect(url_for('main.index'))

@main.route('/<int:question_id>')
def question(question_id):
    r"""Returns question such as anyone can respond to.
    Returns to users for their response and mark correct answer
    """
    questions = get_eq(sqlite3.connect(DB_PATH).cursor(), TABLE_NAME, **{'id': question_id})
    if len(questions) > 1: raise DB.MultipleObjectsReturned()
    return render_template('view.html', question=questions[0])

#@app.route('/<int:question_id/edit')


