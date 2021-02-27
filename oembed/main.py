from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(
        version="1.0",
        type="video",
        provider_name="YouTube Transcript",
        width=425,
        height=644,
        title="Cureatr oEmbed Test",
        html='<iframe src="https://transcribe.rectalogic.com/" width="425" height="644"></iframe>',
    )

app.run(host='0.0.0.0', port=8080)
