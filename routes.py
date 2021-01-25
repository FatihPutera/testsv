from blueprint_user import table

def route(app):
    app.register_blueprint(table)