from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Slack webhook URL
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

@app.route('/order_notification', methods=['POST'])
def order_notification():
    data = request.json
    # Assuming the webhook data contains 'email' and 'total_price' fields
    message = f"New sale! Customer email: {data['email']}, Total Price: {data['total_price']}"
    
    # Send notification to Slack
    requests.post(SLACK_WEBHOOK_URL, json={'text': message})
    
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
