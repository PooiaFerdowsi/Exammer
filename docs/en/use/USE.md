How to use the app?

# How To Run The App?
You must have Python installed. I'll not explain it.

Open Termina/CMD/PowerShell/etc.. & navigate to the correct - root - path.
Root path is where `build.py` or `app.py` placed.

Then try to execute below commands depend on your Shell & etc:
* `python build.py runapp`
* `py build.py runapp`
* `python3 build.py runapp`

You may face an error if you don't have necessary libraries.

## How to install the libraries
Open a shell & type `pip install -r requirements.txt`.
And Then, try again! (run the app again)

# How to work?
There are a number of pages I explained them one by one.

# Index - `/`
You see a list of all exist questions in the DB in a box.
You will see text `A beast ate the questions` if no question exists.

Alongside with them, There are two buttons which the latter will be hidden if no question exists.

* Former button: `New question`
* Latter button: `Delete selected questions`

# New question - `/new`
This page has 5 fields with the order like that.

* Question text
* * Option 1
* * Option 2
* * Option 3
* * Option 4

At end of each option, a checkbox is provided to mark the correct answer

# question `/$question_id`
If you click on a question in index page, the app redirects you to below route:
* `/$id_of_clicked_question`
In that page you see a box with four options to mark one.
To check your answer click on the below button '¿is it correct?'

If you answer is true both the button & your answer will be colored in green.
If you answer is false both the button & your answer will be colored in red & the correct answer will be colored in green