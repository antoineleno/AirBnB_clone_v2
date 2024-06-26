#!/usr/bin/python3
"""This module defines a class to manage database store for hbnb clone"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.city import City
from models.review import Review


class DBStorage:
    """DBStorage
    Class to manage objects storage to DB
    """
    __engine = None
    __session = None

    def __init__(self):
        """Contructor method
        """
        db_user = os.getenv("HBNB_MYSQL_USER")
        db_password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format(db_user, db_password,
                            db_name), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all to retrieve all records from DB

        Args:
            cls (string, optional): Object to return. Defaults to None.

        Returns:
            Dict: All records from a database
        """
        allclasses = {"User": User,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Place": Place,
                      "Review": Review}
        obj_result = {}
        cls = cls if not isinstance(cls, str) else allclasses.get(cls)
        if cls is None:
            for cls in allclasses:
                objs = self.__session.query(cls).all()
                for o in objs:
                    obj_result["{}.{}".format(o.name, o.id)] = o
        else:
            objs = self.__session.query(cls).all()
            for o in objs:
                obj_result["{}.{}".format(o.name, o.id)] = o
        return obj_result

    def new(self, obj):
        """new : to add an an obj to a session

        Args:
            obj (instance): Obj created to be addred
        """
        self.__session.add(obj)

    def save(self):
        """save: method to commit changes to a db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete an obj from a db

        Args:
            obj (string, optional): name of the obj. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)()

    def close(self):
        """close session
        """
        self.__session.close()
