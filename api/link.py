from flask import Flask, request, jsonify
from pytubefix import YouTube

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the YouTube Video Download API!"
    })

@app.route("/download", methods=["POST"])
def download_video():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No JSON data received"
            }), 400

        video_url = data.get("url")

        if not video_url:
            return jsonify({
                "error": "No URL provided"
            }), 400

        yt = YouTube(video_url)

        stream = yt.streams.get_highest_resolution()

        video_info = {
            "title": yt.title,
            "author": yt.author,
            "length": yt.length,
            "views": yt.views,
            "rating": yt.rating,
            "download_url": stream.url
        }

        return jsonify(video_info), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
