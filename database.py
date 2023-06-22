from asyncio.windows_events import NULL
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Links(db.Model):
    __tablename__ = 'urlshort'
    longURL = db.Column(db.String(128),nullable=False)
    shortURL = db.Column(db.String(128),nullable=False,primary_key=True)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return '<shortURL %r>' % self.shortURL

    def hasShortURL(short):
        long = Links.query.filter_by(shortURL=short).first()
        try:
            if(long.shortURL == short):
                return long.longURL
            else:
                return ""
        except Exception as e:
            print(e)
