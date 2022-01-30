This file is made to explain the structure of Exammer. both folder & file structure.

# Principles
Principles are some rules to assist you to explore the structure.

1. All the Back-end files are in the root directory.
2. All the templates are in  `templates` folder.
3. All the static files are in `static` directory.
4. folder `sqls` have one file only.
5. Documentations are in `docs` directory.

## Directories
All the titles in this part are about *Directory structure* not *File structure*

Also, notice that docs are only available to `templates` & `sqls` directory.
Other directories don't need docs and docs would be redundant.

#### Directory `templates`
As most flask projects, this directory serves templates.

The directory have a nested directory inside itself called `errors` which serves the templates used for errror handling.

These error handling files inside directory `errors` are used in `errorer.py` only.

Other templates are as following:
* `create.html`
* `index.html`
* `view.html`
All the above templates are used in `main.py` only.

For a more precise look at templates, click [here](TEMPLATES.md)

#### Directory `sqls`
This directory is made to serve files related to DB.

Instaed of putting whole the code into a Python file I
decided to put whole the code into a `-.sql` file &
read the file to convert the file to string.

This helps us to develop a more clear code.
Also, it helps to change the DB without having too troubles.

Though, it's not efficient to put all the code into separate files and read them one by one.
so it's better to only put into the directory, files that are *long*, *inchangable*(means the files won't change very much), *a time used* (means they've used only once over the development period), and These files won't receive values & are constant.

## Files
In the chapter of a file, you'll see a brief summary only.

* -`;` means no description is needed

### In the main directory
* `api.py`: Application API
* `app.py`: Register blueprints & `Flask.flask()`
* `build.py`: a file to run the project simpler.
* `errorer.py`: error handler blueprint
* `errors.py`: Define customized errors
* `LICENSE`;
* `main.py`: main blueprint, importantest file
* `README.md`;
* `sqlite_api.py`: Define function to SQL manual value--
* `sqlite.db`: Where DB's informations are saved.
* `TODO`;


### in the directories inside the main directory

* [`templates`](TEMPLATES.md);
* `static`: `$.css` file is for `templates/$.html` file
* [`docs`](../../);