from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('site/index.html')

@app.route('/libros')
def libros():
    return render_template('site/libros.html')

@app.route('/nosotros')
def nosotros():
    return render_template('site/nosotros.html')

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

if __name__=='__main__':
    app.run(debug=True)