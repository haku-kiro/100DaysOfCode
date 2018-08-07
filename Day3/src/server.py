## NOTE, after you have created the swagger.yml file, and defined your api
## The <apiendpoint>/ui page becomes available. Which defines your api (assuming you have created the doc correctly)


from flask import (
    Flask,
    render_template
)
import connexion

# Creating the application instance
#app = Flask(__name__, template_folder="./Templates")

app = connexion.App(__name__, specification_dir='./')

# read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

#Create a url route in our application for '/' - the index of the endpoint
@app.route('/')
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:    the rendered template 'home.html'
    """
    return render_template("home.html")
# Side note, we call the index page the home page on purpose as this would conflict with connexion later

# if we are running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)