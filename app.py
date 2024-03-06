from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/abicmtem')
def abicmtem():
  return render_template('abicmtem.html')

@app.route('/ababtech')
def ababtech():
  return render_template('ababtech.html')

@app.route('/abstella')
def abstella():
  return render_template('abstella.html')


@app.route('/callforpaper')
def callforpaper():
  return render_template('callforpaper.html')

@app.route('/scientific')
def scientific():
  return render_template('scientific.html')

@app.route('/wca')
def wca():
  return render_template('wca.html')

@app.route('/nta')
def nta():
  return render_template('nta.html')


@app.route('/papersub')
def papersub():
  return render_template('papersub.html')


@app.route('/presentationguide')
def presentationguide():
  return render_template('presentationguide.html')

@app.route('/registration')
def registration():
  return render_template('registration.html')

@app.route('/journals')
def journals():
  return render_template('journals.html')


@app.route('/awards')
def awards():
  return render_template('awards.html')






if __name__ == "__main__":
  app.run(debug=True)