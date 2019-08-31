import os

db_uri = os.getenv('DATABASE_URI', 'postgres://localhost:5432/things_i_should_know')
