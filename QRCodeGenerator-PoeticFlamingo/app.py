from flask import Flask, render_template, request, send_file
import pyqrcode
import os

app = Flask(__name__)

filename = 'qrcode.png'

def generate_qrcode(text):
    qr = pyqrcode.QRCode(text)
    if not os.path.exists('./static'):
        os.mkdir('static')
    qr.png(f'./static/{filename}', scale=8)

@app.route('/', methods=['GET', 'POST'])
def index():
    results={}
    if request.method == 'POST':
        text = request.form['qrcode-text']
        generate_qrcode(text)
        results['filename'] = filename
    return render_template('index.html', results=results)

@app.route('/download')
def download():
    path = 'static/qrcode.png'
    return send_file(path, as_attachment=True)

if __name__ =="__main__":
    app.run(debug=True)