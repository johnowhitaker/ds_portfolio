# For running this on PythonAnywhere - ref: https://help.pythonanywhere.com/pages/DashWSGIConfig/
# Example Repo with more info on Dash w/ Pythonanywhere: https://github.com/conradho/dashingdemo

from index import app
application = app.server
