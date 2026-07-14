from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class URL(db.Model):

    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    codigo_curto = db.Column(db.String(10), unique=True, nullable=False, index=True)
    url_original = db.Column(db.String(2048), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        return f"<URL {self.codigo_curto}>"