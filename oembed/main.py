from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/oembed')
def index():
    width = int(request.args.get("maxwidth", 425))
    height = int(request..args.get("maxheight", width * 1.5))
    return jsonify(
        version="1.0",
        type="video",
        provider_name="YouTube Transcript",
        width=width,
        height=height,
        title="Cureatr oEmbed Test",
        html=f'<iframe src="https://transcribe.rectalogic.com/" width="{width}" height="{height}"></iframe>',
    )

app.run(host='0.0.0.0', port=8080)
