# Foundation

## [1. Course Intro](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/62b3047a-77bf-4334-9eab-dd988f95dd20/concepts/7e6aee90-126e-4016-b644-a12be47e55c7)

[![](https://img.youtube.com/vi/fDe1k499NNk/0.jpg)](https://youtu.be/fDe1k499NNk)

### This course will cover

- Authentication systems - design, implementation, and use of third party services.
- Common vulnerabilities while working with passwords and how to avoid these pitfalls.
- Authorization systems - design and implementation for backend and frontend.
- Basic security best practices and key principals to keep in mind.

### Prerequisite expectations

We expect that you have pre-existing knowledge in the following areas. We've included a few Recap concepts to help refresh your memory for this course.

- Basic frontend or backend implementation (e.g. Javascript/HTML/Python/Flask)
- Network communication (i.e., HTTP)
- Structured Query Language (SQL) using SQLAlchemy
- API Development (REST)

### This course will not cover

- Advanced security principals.
- Penetration testing, red teaming, vulnerability detection.
- "Hacking" and tools and systems to perform nefarious actions.
- DevOps, Deployments, Scaling or maintaining these systems in the cloud

## [2. Recap - HTTP, Flask, and Postman](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/62b3047a-77bf-4334-9eab-dd988f95dd20/concepts/d3073583-a757-4176-a0c4-93f45d25e60f)

### HTTP Request-Response Handling

[![](https://img.youtube.com/vi/bX7kKwoO4pc/0.jpg)](https://youtu.be/bX7kKwoO4pc)

### HTTP Status Codes

Two status codes which are important throughout this course are:

- 401 Unauthorized

    The client must pass authentication before access to this resource is granted. The server cannot validate the identity of the requested party.
- 403 Forbidden

    The client does not have permission to access the resource. Unlike 401, the server knows who is making the request, but that requesting party has no authorization to access the resource.

### Flask - A Python Framework for Server Development

[![](https://img.youtube.com/vi/vE1dF_bsiRw/0.jpg)](https://youtu.be/vE1dF_bsiRw)

### Postman - HTTP API Development GUI

[![](https://img.youtube.com/vi/AnPFYzLpRKE/0.jpg)](https://youtu.be/AnPFYzLpRKE)

## [3. Recap - SQLAlchemy](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/62b3047a-77bf-4334-9eab-dd988f95dd20/concepts/6f949cc1-43f9-4bf9-bce2-7b9f0358d6b8)

### Storing Persistent Data

[![](https://img.youtube.com/vi/zVZaKDSKH04/0.jpg)](https://youtu.be/zVZaKDSKH04)

### Try It Yourself

Use [this Jupyter notebook](https://r848940c859124xJUPYTERwm1h12hi.udacity-student-workspaces.com/notebooks/SQLAlchemy.ipynb) to practice

### Here is the result

```python
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
```

## [4. Recap - Python Decorators](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/62b3047a-77bf-4334-9eab-dd988f95dd20/concepts/07ba544e-8b01-454e-94e1-76f83a50b52b)

### Recap - Python Decorators

[![](https://img.youtube.com/vi/ghved6sS1hI/0.jpg)](https://youtu.be/ghved6sS1hI)

### Try It Yourself

Use [this Jupyter notebook](https://r848940c859124xJUPYTERwm1h12hi.udacity-student-workspaces.com/notebooks/Decorators.ipynb) to practice
