from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators
    @validates('name')
    def validates_name(self, key, name):
        author = Author.query.filter_by(name = name).first()
        if name and not isinstance(author, Author):
            return name
        else: 
            raise ValueError('Name should be provided')
    @validates('phone_number')
    def validates_phone_number(self, key, phone_number):
        if len(phone_number) == 10 and phone_number.isdigit():
            return phone_number
        else:
            raise ValueError('Phone number should be 10 characters.')
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('title')
    def validates_title(self, key, title):
        if title:
            return title
        else:
            raise ValueError('Input a title')
        
    @validates('content')
    def validates_content(self, key, content):
        if len(content) >= 250:
            return content
        else:
            raise ValueError('Content should be atleast 250 characters long')

    @validates('summary')
    def validates_summary(self, key, summary):
        if len(summary) <= 250:
            return summary
        else: 
            raise ValueError('Summary should be less than 250 characters long')
    
    @validates('category')
    def validates_category(self, key, category):
        if category == 'Fiction' or category == 'Non-Fiction':
            return category
        else: 
            raise ValueError('Category is either "Fiction" or Non-Fiction"')
    
    @validates('title')
    def validates_title(self, key, title):
        clickbait = [
            "Won't Believe",
            "Secret",
            "Top",
            "Guess"
            ]
        for bait in clickbait:
            if bait in title:
                return title
        raise ValueError('Not enough click bait')
        
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
