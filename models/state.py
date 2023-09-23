#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """The State class, which has a relationship with the City class when
        using a database."""
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

        def __init__(self, *args, **kwargs):
            """initializes state"""
            super().__init__(*args, **kwargs)
else:
    class State(BaseModel, Base):
        """The State class, which has a list of related City instances when
        not using a database."""
        name = ""

        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
