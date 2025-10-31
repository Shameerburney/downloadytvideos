from flask import Flask, request, render_template_string
import yt_dlp

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Video Info Preview</title>
  <style>
    body { font-family: Arial; background: #f9fafb; text-align: center; padding-top: 80px; }
    input { width: 70%; padding: 12px; font-size: 1rem; margin-bottom: 20px; }
    button { padding: 12px 30px; font-size: 1rem; background: #4f46e5; color: white; border: none; border-radius: 8px; cursor: pointer; }
    button:hover { background: #3730a3; }
  </style>
</head>
<body>
  <h2>YouTube Video Info Preview</h2>
  <form method="POST" action="/download">
    <input name="video_url" placeholder="Paste YouTube link..." required>
    <br>
    <button type="submit">Fetch Info</button>
  </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get("video_url")
    if not url:
        return "Missing URL", 400

    ydl_opts = {"quiet": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        title = info.get("title", "No title")
        thumb = info.get("thumbnail", "")
        return f"""
        <h3>🎬 {title}</h3>
        <img src="{thumb}" width="480"><br><br>
        <p>Channel: {info.get('uploader')}</p>
        <p>Duration: {info.get('duration_string', 'N/A')}</p>
        <p><a href="/">⬅ Back</a></p>
        """
    except Exception as e:
        return f"<p>Error: {e}</p>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
