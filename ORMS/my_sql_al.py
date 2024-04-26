#!/usr/bin/python3

from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import declarative_base, sessionmaker
# create a mysql url
myurl = "mysql://root:Lucibel96@localhost:3306/JAKE"

# we use the create_engine() function to connect to a database
engine = create_engine(myurl, echo=False)
# create_engine function returns an Engine object, engine, a factory for db connections.

# Test our connection
#with engine.connect() as connection:
    #result = connection.execute("SHOW TABLES")
    #print(f"Connection successful: {result.fetchone()}")

# The declarative_base function from SQLAlchemy's sqlalchemy.ext.declarative module is used to create a base class for declarative class definitions.
Base = declarative_base()


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(50))
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Patient({}, {})".format(self.name, self.age)

print(Patient.__table__)

baker = Patient("Baker", 32)
print(baker)
print("{}, {}, {}".format(baker.name, baker.age, baker.id))

edward = Patient("Eddy", 40)
print("{}, {}, {}".format(baker.name, baker.age, baker.id))
print(edward)

print("{}, {}, {}".format(edward.name, edward.age, edward.id))

# create the table before creating session, objects and committing them.
Base.metadata.create_all(engine)


# let's create a session
# this is the intermediary btwn your application and the db
Session = sessionmaker(bind=engine)
session = Session()
session.add(baker)
session.add(edward)

session.commit()

patient_1 = session.query(Patient).filter_by(name="Baker").first()

print(patient_1)

print(patient_1 == baker)

# Querying
for obj in session.query(Patient).order_by(Patient.id):
    print(f"{obj.id}: {obj.name}: {obj.age}")
