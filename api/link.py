from flask import Flask, request, jsonify, render_template_string
from pytubefix import YouTube

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Downloader</title>
</head>
<body>
    <h1>YouTube Downloader</h1>
    <input id="url" placeholder="Paste YouTube link">
    <button onclick="send()">Download</button>

    <pre id="out"></pre>

<script>
async function send(){
    const url = document.getElementById("url").value;

    const res = await fetch("/download", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({url})
    });

    const data = await res.json();
    document.getElementById("out").innerText = JSON.stringify(data, null, 2);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json()
    yt = YouTube(data["url"])
    stream = yt.streams.get_highest_resolution()

    return jsonify({
        "title": yt.title,
        "download_url": stream.url
    })

def handler(environ, start_response):
    return app(environ, start_response)
