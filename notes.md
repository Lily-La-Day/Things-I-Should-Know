@channel steps for homework tonight:

0 - Follow the steps along in the textbook!

1. Use pipenv to install flask
2. Create an `app.py` file
3. Create a `.env` file
4. In `.env`
 - Set FLASK_ENV to development
 - Set FLASK_SKIP_DOTENV to 1

5. In `app.py` - set up a basic ‘Hello World’ flask app to test that it is running correctly
- Import flask
- Start app
- Set up a route for ‘/’
- Write a function that returns ‘Hello World’ and a status of 200
- Test this by running flask in terminal and making a request to ‘/’ in insomnia

-------------------------- Continue from here for homework -------------------------

6. Install flask-sqlalchemy psycopg2-binary
7. In terminal, create a database (`createdb db_name`)
8. In `app.py`
- Import flask sqlalchemy to `app.py`
- Set up config (‘SQLALCHEMY_DATABASE_URI’ and ‘SQLALCHEMY_TRACK_MODIFICATIONS’)
- attach SQLAlchemy functionality to variable called db

9. Create a directory called models and a file for the model
 - Import db from app
 - Build a class using db.Model
 - Remember to set the __tablename__
 - Define the shape of the model (the fields) - you MUST have an id that is the primary key

10. Make a `seeds.py` file
 - Import app and db
 - Import the Cat model
 - Use flask’s app_context() function to:
    - Drop all tables in the db
    - Create all tables in the db
 - Create some entries for your database
 - Remember to add each model to the db
 - Finally commit to the db
- _This step was left out before:_ Then seed your database
 - At this point you can use TablePlus to check that your entries exist in the table in the db

*11. Ask Gae to bring you some ice cream during your homework break*

12. Install marshmallow-sqlalchemy and flask-marshmallow
13. In `app.py`
 - Import marshmallow-sqlalchemy and flask-marshmallow
 - attach Marshmallow functionality to variable called ma
14. In your model file
 - Add ‘ma’ to your import from app
 - Create a schema for your model using ma.
15. In `app.py`
 - Import your resource model (Cat) and resource schema (CatSchema)
 - Invoke schema so it is ready to be used
 - Set up a route for your resource (‘/cats’)
 - Write an index function that queries the database for all cats and returns jsonified cats using the schema
 - Test with insomnia (edited)




1. Set up the environment
 - Make config directory
 - Create an `environment.py` file inside config
 - Refactor `app.py` to import environment and update database uri


2. Create the base model
 - Remember your imports - don’t forget marshmallow fields
 - Build the base model and schema
 - Go to the model for your resource (e.g. cats) and import the base model and schema and ‘mix’ them into your resource model and schema


3. SEED and TEST!!!


4. Refactor into controllers
 - Delete the index route from `app.py`
 - Make a controllers directory
 - Make a file for your resource (e.g. `cats.py`)
 - Import Blueprint from flask
 - Register Blueprint
 - Import your resource model and schema
 - Replicate the index route (from `app.py`) and hook it up to the api.route

5. Router
 - In the config directory, make a `router.py` file
 - Import app and your controllers
 - Register the blueprint

6. Import router from config into `app.py`

7. TEST!!!


8. Do the rest of the routes - show, create, update, delete
 - Remember to import jsonify, request from flask

-------------- OPTIONAL ------------------

1. In `models/cat.py`
 - Create a new class for the comment model and schema
 - Specify new fields on the Comment model

2. In `seeds.py`
 - Add Comment into your import from your resource
 - Create some comments, add and commit them
 - SEED and TEST!!

3. In `models/cat.py`
 - Import fields from marshmallow
 - Add comment fields to your resource schema (e.g. CatSchema)

4. In the controllers
 - Make create and delete routes for the comments
