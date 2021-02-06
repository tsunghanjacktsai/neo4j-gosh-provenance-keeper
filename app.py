from flask import Flask
from models import db

POSTGRES = {
    'user': 'postgres',
    'password': 'root',
    'db': 'postgres',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)


@app.route('/api/v1/patients/', methods=['POST'])
def create_patient():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
