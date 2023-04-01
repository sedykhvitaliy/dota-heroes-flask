import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "fdsfnvudfvdnru"
    UPLOAD_FOLDER = 'C:\\dev\\github\\dota-heroes-flask\\app\\static\\img'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
