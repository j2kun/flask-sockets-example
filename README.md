# Rethink example

A demo app to learn to use rethinkdb behind a flask server, with socket.io for real time updates

# Complete stack 

* [Flask](http://flask.pocoo.org) using [flask-socketio](https://flask-socketio.readthedocs.io/en/latest/)
* [RethinkDB](http://www.rethinkdb.com)
* [WebSockets](http://socket.io/)

# Installation 

```
git clone git://github.com/j2kun/rethink-example.git
pip install -r requirements.txt
```

# Start RethinkDB 

Make sure you have RethinkDB running.  

_Note_: If you don't have RethinkDB installed, you can follow [these instructions to get it up and running](http://www.rethinkdb.com/docs/install/). 


# Running the application 

Firstly we'll need to create the database `example` and the table used by this app: `chat`. You can
do this by running:

```
python init_db.py
```

Flask provides an easy way to run the app:

```
python app.py
```

Then open a browser: <http://localhost:5000/>.
