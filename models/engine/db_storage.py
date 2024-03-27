#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.schema import MetaData
from os import getenv


class DBStorage:
    """Defines the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of class"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Method that returns a dictionnary of objects"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        objects = {}

        if cls is not None:
            data = self.__session.query(cls).all()
            for obj in data:
                key = "{}.{}".format(cls.__name__, obj.id)
                objects[key] = obj

        else:
            for cls_name, cls in classes.items():
                data = self.__session.query(cls) .all()
                for obj in data:
                    key = "{}.{}".format(cls.name, obj.id)
                    objects[key] = obj

        return objects

    def new(self, obj):
        """Method that add a new object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Method that save all changes in the current database session"""
        self.__session.commit()

    def delete(self, obj):
        """Method that delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Method that create the database session and the
        tables in the database"""
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
