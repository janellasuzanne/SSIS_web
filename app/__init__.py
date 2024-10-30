from flask import Flask
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL, CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
from flask_wtf.csrf import CSRFProtect

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_HOST=DB_HOST,
        MYSQL_DATABASE=DB_NAME
    )

    cloudinary.config(
        cloud_name = CLOUD_NAME,
        api_key = CLOUDINARY_API_KEY,
        api_secret = CLOUDINARY_API_SECRET,
        secure = True
    )

    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    from .controller.admin import user
    from .controller.college import college
    from .controller.course import course
    from .controller.student import student


    app.register_blueprint(user)
    app.register_blueprint(college)
    app.register_blueprint(course)
    app.register_blueprint(student)

    return app