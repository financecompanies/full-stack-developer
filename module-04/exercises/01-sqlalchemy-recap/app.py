import os

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(''))
database_path = f"sqlite:///{os.path.join(project_dir, database_filename)}"

engine = create_engine(database_path)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    username = Column(String(80), unique=True)
    password = Column(String(180), nullable=False)

    def __repr__(self):
        return f"{self.username}: {self.password}"


User.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

new_user = User(username="filipebezerra", password="genpwd123456")
session.add(new_user)
session.commit()

first_user = session.query(User).filter_by(username="filipebezerra").first()
print(first_user)
