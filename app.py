from ensurepip import bootstrap
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from lr import LRModel 

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "super_secret_key"


class DataForm(FlaskForm):
    xdata = StringField("X values")
    ydata = StringField("Y values")
    submit = SubmitField("Make the model!") 

@app.route('/', methods=["GET", "POST"])
def index():
    x_val = []
    y_val = []
    if request.form:
        x_val.append(request.form["xdata"])
        y_val.append(request.form["ydata"])
        valid = None
        params = None
        try:
            model_lr = LRModel([float(i) for i in x_val[0].split(",")],[float(j) for j in y_val[0].split(",")])
            model_lr.add_const()
            model_lr.fit_data()
            params = model_lr.fit_data()
            model_lr.plot_data()
            valid = True
        except ValueError:
            valid = False
            params = [0]
        return render_template("simplelr.html",params=params, valid=valid)
    return render_template("base.html", template_form=DataForm())
    

@app.route("/poly")
def poly():
    return render_template("poly.html")