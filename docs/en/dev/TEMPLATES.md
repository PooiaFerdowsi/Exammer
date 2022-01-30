This is an overview of defined templates.

Templates inside the directory `templates/errors` are for `errorer.py`.
I'll explain them precicely later.

Other templates have a unique but united role.
I'll explain them too!


# Templates inside directory `errors`
* `404.html`: for error 404
* `KeyError.html`: for Flask/Python KeyError
* `MultipleObjectsReturned`: If more than expected objects (1 object) were returned

# Inside the main
### `create.html`
Show the interface for creating a new question.

The interface has 5 text boxes which four of them are intended.
The text box which is not intended is at top of others.

There are some other things that I don't explain, so **See to Understand!**

### `index.html`
main page.

A list of all questions inside the DB.
Plus two buttons for create & delete question(s).

the latter button is hidden if there is no questions.

### `view.html`
Give ID of the question as its route.

Show the question with options, & a button to check the answer & show the result.