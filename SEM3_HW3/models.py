from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
import enum

sqlite_database = "sqlite:///SEM3_HW3/app.db"
engine = create_engine(sqlite_database)


class Base(DeclarativeBase): pass



class GenderEnum(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    age = Column(Integer)
    gender = Column(Enum(GenderEnum))
    group = Column(Integer)
    faq = Column(Integer, ForeignKey('faq.id'))

    def __repr__(self):
        return f'student ({self.name})'


class Faq(Base):
    __tablename__ = "faq"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    students = relationship('student', backref='faculty', lazy=True)


# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
class Estimate(Base):
    __tablename__ = "estimate"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship('student', backref='estimates', lazy=True)
    faculty = Column(String, ForeignKey('faq.title'))
    faq = relationship('faq', backref='estimates', lazy=True)
    value = Column(Integer)

    def __repr__(self):
        return f'{self.value}'


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    year = Column(Integer, nullable=False)
    count = Column(Integer)
    author = Column(Integer, ForeignKey('author.id'))

    def __repr__(self):
        return f'book ({self.title})'


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    books = relationship('book', backref='author_name', lazy=True)

    def __repr__(self):
        return f'author ({self.name} {self.surname})'


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    date_of_birth = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class User2(Base):
    __tablename__ = "user2"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    surname = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)