from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "mustafa"

class UserForm(FlaskForm):
    user_name = StringField("Type ur name please: ", validators=[DataRequired()])
    submit = SubmitField("Check Name")
    
@app.route("/", methods=["GET", "POST"])
def home():
    form = UserForm()
    if form.validate_on_submit():
        if form.user_name.data.lower() == "mustafa":
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("client"))
    return render_template("home.html", form=form)

@app.route("/admin/")
def admin():
    return render_template("admin.html")

@app.route("/client/")
def client():
    return render_template("client.html")

if __name__ == "__main__":
    app.run(debug=True)