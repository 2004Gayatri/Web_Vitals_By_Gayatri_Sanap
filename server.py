from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST"
    return response

YOUR_API_KEY = 'AIzaSyDdlkrjl-oq4LPug1igsPCvJdhRZiRFGbg'  # Replace with your actual key

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    params = {
        'url': url,
        'key': YOUR_API_KEY,
        'strategy': 'desktop'
    }

    try:
        res = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed', params=params)
        print("Google API Response:", res.text)

        if res.status_code != 200:
            return jsonify({'error': 'Google API Error', 'details': res.text}), res.status_code

        psi_data = res.json()

        if 'lighthouseResult' not in psi_data:
            return jsonify({'error': 'Invalid response from PageSpeed API', 'raw': psi_data}), 500

        audits = psi_data['lighthouseResult'].get('audits', {})
        if not audits:
            return jsonify({'error': 'Missing audit data', 'raw': psi_data}), 500

        vitals = {
            'LCP': audits['largest-contentful-paint']['numericValue'],
            'FID': audits['max-potential-fid']['numericValue'],
            'CLS': audits['cumulative-layout-shift']['numericValue']
        }

        return jsonify(vitals)
    except Exception as e:
        print("Error while fetching vitals:", e)
        return jsonify({'error': 'Unable to retrieve vitals.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
