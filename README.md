# Socket example

A demo app to learn to use flask with socket.io for real time updates

# Complete stack 

* [Flask](http://flask.pocoo.org) using [flask-socketio](https://flask-socketio.readthedocs.io/en/latest/)
* [WebSockets](http://socket.io/)
* [RethinkDB](http://www.rethinkdb.com) (ignore for now, haven't picked a database)

# Installation 

```
git clone git://github.com/j2kun/flask-sockets-example.git
cd rethink-example
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Project structure

```
.
├── README.md
├── app.py                 <--- main flask program
├── init_db.py
├── requirements.txt
├── static                 <--- third party javascript plugins
│   ├── jquery.js
│   └── socket.io.min.js
└── templates              <--- html pages that get rendered by Flask
    ├── blah.html
    └── index.html
```

# Running the application 

Run the flask servery with

```
python app.py
```

Then open a browser to <http://127.0.0.1:5000/blah/> to see the simple html page, 
and open <http://127.0.0.1:5000/> in multiple windows to see the chat app.
