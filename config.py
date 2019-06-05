#Holds the configuration options

import os
import pymysql

# Limit what type of files can be sent to the database
ALLOWED_EXTENSIONS = set(['pdf', 'odt', 'txt'])

# Set up the database connection
def create_connection():
    connection = pymysql.connect(   host = 'localhost',
                                    user = 'root',
                                    password = '',
                                    db = 'flask-ajax',
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor)
    return connection

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'