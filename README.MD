## Start App
### run bash command: "python3 app.py"
added postgreSQL db -mh

first install flask_migrate and flask_script then run:
python app.py db init
python app.py db migrate
python app.py db upgrade

to make database changes use:
"python app.py db migrate"
"python app.py db upgrade"
