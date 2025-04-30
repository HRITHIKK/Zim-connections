from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Webhook Receiver Running"})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)

    # Check for the word "Hospital" (case-insensitive)
    if 'hospital' in data.get('message', '').lower():
        group_id = data.get('groupId', 'N/A')
        message_text = data.get('message', '')
        print(f"🚨 Hospital Alert! Message: {message_text}, Group ID: {group_id}")
        # NOTE: Sending email may not work in Vercel. Consider using an external email API service here.

    return jsonify({"message": "Webhook triggered"})

# Vercel requires this handler function for serverless deployment
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
