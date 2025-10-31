from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '''
    <h2>Send file</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return f"File {file.filename} uploaded successfully!"

from pyngrok import ngrok
ngrok.connect(5000)
app.run(port=5000)
