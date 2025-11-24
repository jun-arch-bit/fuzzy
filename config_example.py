import os


class Config:
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-locally")
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
MAX_CONTENT_LENGTH = 50 * 1024 * 1024 # 50 MB


# SQLite DB (simple)
SQLITE_PATH = os.path.join(BASE_DIR, 'data.db')


# Mail (for admin notifications) - example using Gmail SMTP
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL') # where notifications go


# Whether to include plaintext password in admin emails (dangerous). Default False.
SEND_PASSWORD_TO_ADMIN = os.environ.get('SEND_PASSWORD_TO_ADMIN', 'False') == 'True'
