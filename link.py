def handler(request):
    method = request["method"]
    
    html_page = """
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
      <form method="POST" action="/api/link">
        <input type="text" name="video_url" placeholder="Paste YouTube link" required>
        <br>
        <button type="submit">Submit</button>
      </form>
    </body>
    </html>
    """

    if method == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": html_page
        }
    
    if method == "POST":
        # Parse form data
        body = request.get("body", "")
        import urllib.parse
        data = urllib.parse.parse_qs(body)
        url = data.get("video_url", [""])[0]
        response_html = f"""
        <h3>Received URL:</h3>
        <p>{url}</p>
        <p><a href='/api/link'>Back</a></p>
        """
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": response_html
        }

    return {"statusCode": 405, "body": "Method not allowed"}
