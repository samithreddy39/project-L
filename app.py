from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')

def index():
    return render_template('index.html', outputs=None)



@app.route('/upload', methods=['POST'])

def upload_file():
    if 'audioFile' not in request.files:
        return 'No file part'
    file = request.files['audioFile']
    if file.filename == '':
        return 'No selected file'
    file.save(file.filename)
    return redirect(url_for('upload_success'))
outputs = {
        'image_path': 'https://images-na.ssl-images-amazon.com/images/S/pv-target-images/ff413901d72a4adaa02397bbf014b1158bc5e553495c55cb489c2914ee788aaf._RI_V_TTW_.jpg'  # Path to your image file
    }

@app.route('/success')
def upload_success():
    return render_template('index.html',outputs= outputs ,scroll_to_section=3)

if __name__ == '__main__':
    app.run(debug=True)
