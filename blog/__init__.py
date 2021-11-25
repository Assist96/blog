import os
from flask import Flask
from blog.blueprints.blog import blog
from blog.blueprints.admin import admin
from blog.blueprints.auth import auth
from blog.settings import config
# app=Flask('blog')
# config_name=os.getenv('FLASK_ENV','development')
# app.config.from_object(config[config_name])

def create_app(config_name=None):
    if not config_name:
        config_name=os.getenv('FLASK_ENV','development')
    app=Flask('blog')
    app.config.from_object(config[config_name])
    app.register_blueprint(blog)
    app.register_blueprint(admin,url_prefix='/admin')
    app.register_blueprint(auth,url_prefix='/auth')
    return app