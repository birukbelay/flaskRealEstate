from packages import app, db


if __name__ == '__main__':
    app.run(debug=True)


@app.cli.command('init-db')
def init_db_command():
    db.create_all()


@app.cli.command('reclean-db')
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
