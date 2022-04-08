from battleship import api
from battleship.models import db
from flask_migrate import Migrate

db.init_app(api.app)
migrate = Migrate(api.app, db)


api.app.run()