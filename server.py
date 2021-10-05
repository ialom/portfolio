from flask import Flask, render_template, send_file, request, redirect
import csv

#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
#Scripts\activate
#$env:FLASK_APP = "server"
#$env:FLASK_ENV = "development"
#flask run

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods=['POST','GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('index.html', display_model="True")
        except:
            return 'Something went horribly horrible wrong!'
    else:
        #return 'Something went horribly horrible wrong!'
        return render_template('index.html', display_model="False")

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        file=database.write(f'\n{data["name"]}, {data["email"]}, {data["subject"]}, {data["message"]}')

def write_to_csv(data):
    with open('database.csv', mode='a') as csv_database:
        csv_writer=csv.writer(csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data.values())

# @app.route("/about")
# def about():
#     return render_template('index.html')\
#
# @app.route("/about#one")
# def about_one():
#     return render_template('index.html',page_name='about')
#
# @app.route("/work")
# def work():
#     return render_template('index.html')


@app.route("/favicon.ico")
def favicon():
    return send_file("static/dragon.jpeg", mimetype='image/jpeg')