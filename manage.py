from flask_script import Manager, Server
from app import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
import models 

manager = Manager(app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand) 

if __name__ == '__main__':
    manager.run()