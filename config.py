class Config:
    SECRET_KEY = 'secret-key'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///food_delivery_db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = 'smtp.sample.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'username@sample.com'
    MAIL_PASSWORD = 'mail_password'

    # STRIPE_API_KEY = 'stripe_api_key'