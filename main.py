import os
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "index.html", mimetype="text/html")


@app.route("/video/<video_id>/<captions_id>")
def video(video_id, captions_id):
    return render_template("video.html", video_id=video_id, captions_id=captions_id)


@app.route("/oembed")
def oembed():
    width = int(request.args.get("maxwidth", 425))
    height = int(request.args.get("maxheight", width * 1.5))
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
