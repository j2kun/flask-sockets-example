# Rethink example

A demo app to learn to use rethinkdb behind a flask server, with socket.io for real time updates

# Complete stack #

* [Flask](http://flask.pocoo.org)
* [Backbone](http://backbonejs.org)
* [RethinkDB](http://www.rethinkdb.com)

# Installation #

```
git clone git://github.com/rethinkdb/rethinkdb-example-flask-backbone-todo.git
pip install Flask
pip install rethinkdb
```

# Start RethinkDB #

Make sure you have RethinkDB running.  
If you are not running RethinkDB on your local machine with the default settings,
update the `todo.py` file on lines 21 and 22.

_Note_: If you don't have RethinkDB installed, you can follow [these instructions to get it up and running](http://www.rethinkdb.com/docs/install/). 


# Running the application #


Firstly we'll need to create the database `todoapp` and the table used by this app: `todos`. You can
do this by running:

```
python todo.py --setup
```

Flask provides an easy way to run the app:

```
python todo.py
```

Then open a browser: <http://localhost:5000/>.
