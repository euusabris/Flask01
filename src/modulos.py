from flask_bootstrap import Bootstrap
from flask_minify import Minify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DeclarativeBase


class Base(DeclarativeBase):
    pass


bootstrap = Bootstrap()
minify = Minify()
db = SQLAlchemy(model_class=Base,
                disable_autonaming=True)



