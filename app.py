from src import create_app, db
from src.models.user import User


# @app.cli.command('reclean-db')
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

app = create_app("dev")
if __name__ == '__main__':
    app.run(debug=True)



@app.cli.command('init-db')
def init_db_command():
    db.create_all()




@app.cli.command('seed_db')
def seed_db():
    db.session.add(User(first_name='bura', email="bura@gmail.com", password="1234"))
    db.session.add(User(first_name='bura2', email="bura2@gmail.org", password="1234"))
    db.session.commit()
