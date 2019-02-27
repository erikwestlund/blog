from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app
from commands.initial_seed import InitialSeed

manager = Manager(create_app)

manager.add_command("db", MigrateCommand)
manager.add_command("initial_seed", InitialSeed)


manager.run()
