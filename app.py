from flask import Flask, render_template, request
from fuzzyLogic import evaluasi_fuzzy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fuzzy', methods=['GET', 'POST'])
def fuzzy():
    hasil = None
    if request.method == 'POST':
        try:
            hb       = float(request.form.get('hb', 0))
            sistolik = float(request.form.get('sistolik', 0))
            tidur    = float(request.form.get('tidur', 0))

            score, status, warna = evaluasi_fuzzy(hb, sistolik, tidur)

            hasil = {
                "score":  score,
                "status": status,
                "warna":  warna
            }
        except ValueError:
            pass

    return render_template('fuzzy.html', hasil=hasil)

app = app

if __name__ == '__main__':
    app.run(debug=True, port=5055) 