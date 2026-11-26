import yaml
from flask import Flask
from app import db  # Імпортуємо db з нашого пакету app

app = Flask(__name__)

# Зчитування конфігурації
with open('app/config/app.yml', 'r') as file:
    config = yaml.safe_load(file)
    db_config = config['database']

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db_name']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Прив'язуємо ініціалізовану db до нашого Flask-додатка
db.init_app(app)

# Імпортуємо домени ПІСЛЯ ініціалізації db
from app.my_project.auth.domain.user import User
from app.my_project.auth.domain.address import Address
from app.my_project.auth.domain.watch import Watch
from app.my_project.auth.domain.feature import Feature
from app.my_project.auth.domain.watch_model import WatchModel
from app.my_project.auth.domain.watch_model_feature import WatchModelFeature

# Реєстрація Blueprint
from app.my_project.auth.route.user_route import user_bp
app.register_blueprint(user_bp)

from app.my_project.auth.route.address_route import address_bp

from app.my_project.auth.route.watch_model_route import watch_model_bp
app.register_blueprint(watch_model_bp)

app.register_blueprint(address_bp)

# Створення таблиць
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)