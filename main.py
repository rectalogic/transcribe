import os
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "index.html", mimetype="text/html")


@app.route("/video/<video_id>")
def video(video_id):
    return render_template("video.html", video_id=video_id)


@app.route("/oembed")
def oembed():
    WIDTH = 560
    HEIGHT = 315
    width = int(request.args.get("maxwidth", WIDTH))
    height = int(request.args.get("maxheight", HEIGHT))
    if width != WIDTH or height != HEIGHT:
        meet_scale = min(width / WIDTH, height / HEIGHT)
        width = int(width * meet_scale)
        height = int(height * meet_scale)
    url = request.args["url"]
    return jsonify(
        version="1.0",
        type="video",
        provider_name="YouTube Transcript Player",
        width=width,
        height=height,
        title="YouTube Transcript Player",
        html=f'<iframe src="{url}" frameborder="0" width="{width}" height="{height}"></iframe>',
    )


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/vnd.microsoft.icon")


app.run(host="0.0.0.0", port=8080)
