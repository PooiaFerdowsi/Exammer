"""Api for this application.
File separation is a good way for sorting files
Instead of putting whole the code into one file.
The file separation can make application more:
* readable
* predictable
* optimizitionable
"""

from flask import jsonify, request, Blueprint

from sqlite_api import DB_PATH, TABLE_NAME
from sqlite_api import get_all, get_eq
from sqlite_api import insert_all
from sqlite_api import delete_eq

import sqlite3

api = Blueprint("api", "Exammer")

from errors import DB

@api.route('/v1/questions')
def apiV1_questions():
    "Return a list of all the exist questions"
    return jsonify(get_all(sqlite3.connect(DB_PATH).cursor(), TABLE_NAME))

@api.route('/v1/create', methods=["POST"])
def apiV1_create():
    "Create an question with passed data through POST method"
    question = request.form['question']
    answers = [
        request.form['ans1'],
        request.form['ans2'],
        request.form['ans3'],
        request.form['ans4'],
    ]
    correct = request.form['correct']

    db = sqlite3.connect(DB_PATH)
    ##########################################
    command = f"(NULL, '{question}',\
    '{answers[0]}','{answers[1]}', \
    '{answers[2]}','{answers[3]}', {correct})"
    ##########################################
    insert_all(db.cursor(), TABLE_NAME, command)
    db.commit()
    return '', 200

@api.route('/v1/question/<int:id>/view')
def apiV1_question_view(id):
    "render the question wich question.id = <id> as a JSON object"
    questions = get_eq(sqlite3.connect(DB_PATH).cursor(), TABLE_NAME, id=id)
    if len(questions) > 1:
        raise DB.MultipleObjectsReturnedException()
    else:
        question = questions[0]
        del questions

    return jsonify(
        {
            'id': question[0],
            'question': question[1],
            'answers': [
                question[2],
                question[3],
                question[4],
                question[5],
            ],
            'correct': question[6],
        }
    )

@api.route('/v1/question/<int:id>/delete')
def apiV1_question_delete(id):
    "Delete the question wich question.id = <id>"
    db = sqlite3.connect(DB_PATH)
    delete_eq(db.cursor(), TABLE_NAME, **{'id': id})
    db.commit()
    return '', 200