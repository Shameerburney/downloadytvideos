from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>YouTube Tool</title>
  <style>
    body { font-family: Arial; background:#f9fafb; text-align:center; padding-top:80px; }
    input { width:70%; padding:12px; margin-bottom:20px; }
    button { background:#4f46e5; color:white; border:none; padding:12px 30px; border-radius:8px; cursor:pointer; }
    button:hover { background:#3730a3; }
  </style>
</head>
<body>
  <h2>YouTube Tool</h2>
  <form method="POST" action="/submit">
    <input type="text" name="video_url" placeholder="Paste YouTube link" required>
    <br>
    <button type="submit">Submit</button>
  </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/submit', methods=['POST'])
def submit():
    url = request.form.get("video_url")
    return f"<h3>Received URL:</h3><p>{url}</p><p><a href='/'>Back</a></p>"

if __name__ == '__main__':
    app.run()
