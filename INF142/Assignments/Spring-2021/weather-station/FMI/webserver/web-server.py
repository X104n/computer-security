from flask import Flask, render_template, url_for, redirect, request
from station import reciever as r



app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    r.bergen()
    r.oslo()
    r.karmøy()
    return render_template('home.html', bergen=r.bergentemps, oslo=r.oslotemps, karmøy=r.karmøytemps, title='Home')


@app.route("/bergen")
def bergen():
    r.bergen()
    return render_template('bergen.html', weather=r.bergentemps, title='Bergen', style="/bergen.css")

@app.route("/oslo")
def oslo():
    r.oslo()
    return render_template('oslo.html', weather=r.oslotemps, title='Oslo', style="/oslo.css")

@app.route("/karmøy")
def karmøy():
    r.karmøy()
    return render_template('karmøy.html', weather=r.karmøytemps, title='Karmøy', style="/karmoy.css")



@app.route('/day')
def Day():
    req = request.args.get('day')
    day = int(req[:2])
    loc = req

    if 'Bergen' in loc:
        r.bergen(day)
        return render_template('day.html', weather=r.bergentemps, title="Bergen daily", style="/bergen.css")
    elif 'Karmøy' in loc:
        r.karmøy(day)   
        return render_template('day.html', weather=r.karmøytemps, title="Karmøy daily", style="/karmoy.css")
    elif 'Oslo' in loc:
        r.oslo(day)
        return render_template('day.html', weather=r.oslotemps, title="Oslo daily", style="/oslo.css")
    else:
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
    