# Instructions

## Setup Development Environment First Time

1. Clone Github repository
2. Go to the dev subdirectory in the repo
3. (python > 3.6.8) Create a python virtual environment called venv 
4. Do source ./venv/bin/activate
5. Do pip install -r requirements.txt
6. ask groupchat for .env file and put it in dev folder

## Developing

1. Make sure to operate in python venv. Do `source ./venv/bin/activate` (Note: you can deactivate with `deactivate`)
2. To run the server: `export FLASK_ENV=development && flask run`
3. To run the shell: `export FLASK_ENV=development && flask shell`
3. If something didn't work make sure to do `pip install -r requirements.txt` or see how to add env variable

## Modified Database? 

1. `flask db migrate`
2. Review file and edit if needed
3. `flask db upgrade`
4. add to repo

For help run `flask db --help`

## Modified Dependencies? 

1. Tell group in FB
2. Do `pip freeze > requirements.txt`
3. add to repo

## Added environment variable? 

1. Say in groupchat. 
2. If someone says they did, add to .env file.
