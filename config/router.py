import os
from app import app
from controllers import code_things

app.register_blueprint(code_things.api, url_Prefix='/api')

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#
#     if os.path.isfile('dist/' + path):
#         return app.send_static_file(path)
#
#     return app.send_static_file('index.html')
