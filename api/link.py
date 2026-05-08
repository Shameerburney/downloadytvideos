from flask import Flask, request, jsonify, render_template_string
from pytubefix import YouTube

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Downloader</title>
    <style>
        body {
            font-family: Arial;
            background: #111;
            color: white;
            text-align: center;
            padding-top: 100px;
        }

        input {
            width: 400px;
            padding: 12px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }

        button {
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            background: red;
            color: white;
            font-size: 16px;
            cursor: pointer;
            margin-left: 10px;
        }

        #result {
            margin-top: 30px;
        }

        a {
            color: cyan;
        }
    </style>
</head>
<body>

    <h1>YouTube Video Downloader</h1>

    <input type="text" id="url" placeholder="Paste YouTube URL">
    <button onclick="downloadVideo()">Get Video</button>

    <div id="result"></div>

    <script>
        async function downloadVideo() {
            const url = document.getElementById("url").value;

            const response = await fetch("/download", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ url })
            });

            const data = await response.json();

            if (data.error) {
                document.getElementById("result").innerHTML =
                    `<p>${data.error}</p>`;
            } else {
                document.getElementById("result").innerHTML = `
                    <h2>${data.title}</h2>
                    <p>Author: ${data.author}</p>
                    <p>Views: ${data.views}</p>
                    <a href="${data.download_url}" target="_blank">
                        Download Video
                    </a>
                `;
            }
        }
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/download", methods=["POST"])
def download_video():
    try:
        data = request.get_json()
        video_url = data.get("url")

        if not video_url:
            return jsonify({"error": "No URL provided"}), 400

        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()

        return jsonify({
            "title": yt.title,
            "author": yt.author,
            "views": yt.views,
            "download_url": stream.url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
