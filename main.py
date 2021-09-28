from flask import Flask, request, render_template, url_for
from dua_empat import *

app = Flask(__name__, template_folder='template')

@app.route('/')
def first_page():
    return render_template('index.html')

@app.route('/',methods = ['POST'])
def hasil():
    print(type(request.form))
    if request.method == 'POST':
        angka1 = request.form['nilai1']
        angka2 = request.form['nilai2']
        angka3 = request.form['nilai3']
        angka4 = request.form['nilai4']
        hasil, jumlah = menampilkanhasil(int(angka1), int(angka2), int(angka3), int(angka4))
        hasil = hasil.replace('\n', '<br/>')
        return render_template('tampil.html',hasil = hasil, jumlah = jumlah)
    

if __name__ == '__main__':
    app.run(debug=True)