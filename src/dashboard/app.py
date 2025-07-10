from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/drafts', methods=['GET'])
def get_drafts():
    # Return list of drafts (placeholder)
    return jsonify([])

@app.route('/api/publish', methods=['POST'])
def publish():
    data = request.json
    # Trigger workflow (placeholder)
    return jsonify({"status": "published"})

if __name__ == "__main__":
    app.run(debug=True)
