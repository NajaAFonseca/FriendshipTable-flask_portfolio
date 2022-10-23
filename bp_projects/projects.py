from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

@app_projects.route('/snakegame/')
def snakegame():
    return render_template('snakegame.html')
# connects /kangaroos path to render kangaroos.html
@app_projects.route('/kangaroos/')
def kangaroos():
    return render_template("https://lydia-c2.github.io/lyds.github.io/")

@app_projects.route('/walruses/')
def walruses():
    return render_template("https://github.com/linaawad1/lina.github.io.git")

@app_projects.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")