At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
-----------

Why Python programming is awesome

How to connect to a MySQL database from a Python script

How to SELECT rows in a MySQL table from a Python script

How to INSERT rows in a MySQL table from a Python script

What ORM means

How to map a Python Class to a MySQL table

How to create a Python Virtual Environment



SQL INJECTIONS
--------------
Avoid directly interpolating user input into SQL QUeries using string formatting methods like str.format method.
Use parametized queries.
These allow you to safely pass user input to the SQL Queries as parameters without risking SQL Injection.


Relationships in SQLAlchemy
-----------------------------------
SQLAlchemy uses ORM (Object-Relational Mapping) to map Python classes to database tables
Relationships are established using the relationship function and are defined in classes representing tables.

Defining Relationships: In the model classes, relationships can be defined using relationship and ForeignKey. For example:

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state')

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')


Joins in SQLAlchemy
------------------------
Joins allow you to combine rows from two or more tables based on a related column between them. In SQLAlchemy, you use the join method to specify the join condition between tables.

Join Method: You can use the join method in a query to join two tables based on a specified condition. For example:

result = session.query(State, City).join(City, State.id == City.state_id).all()

This query joins the State and City tables based on the condition that State.id matches City.state_id.

