import os
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/oembed")
def oembed():
    width = int(request.args.get("maxwidth", 425))
    height = int(request.args.get("maxheight", width * 1.5))
    return jsonify(
        version="1.0",
        type="video",
        provider_name="YouTube Transcript",
        width=width,
        height=height,
        title="Cureatr oEmbed Test",
        html=f'<iframe src="https://transcribe.rectalogic.com/" frameborder="0" width="{width}" height="{height}"></iframe>',
    )


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/vnd.microsoft.icon")


app.run(host="0.0.0.0", port=8080)
