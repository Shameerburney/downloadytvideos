from flask import Flask, request, jsonify
from pytubefix import YouTube

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the YouTube Video Download API!"})

@app.route("/download", methods=["POST"])
def download_video():
    data = request.get_json()
    video_url = data.get("url")
    
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        yt = YouTube(video_url)
        
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        
        # Get video info
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
        return jsonify({"error": str(e)}), 500

def handler(request):
    with app.request_context(request.environ):
        return app.full_dispatch_request()
