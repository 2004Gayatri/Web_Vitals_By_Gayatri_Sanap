Web Vitals Monitoring Project
This project is a simple web application that tracks and reports Core Web Vitals for any website using the PageSpeed Insights API.
It is built using Flask for the backend and provides a clean interface for analyzing website performance.

Features 🚀
Analyze any website’s Core Web Vitals (LCP, FID, CLS, etc.)

Real-time fetching of performance data using Google's PageSpeed Insights API

Simple and lightweight Flask backend

Clean, minimal frontend to enter URLs and view performance reports

Error handling for invalid URLs and API failures

Technologies Used 🛠️
Python (Flask framework)

HTML5, CSS3, JavaScript

PageSpeed Insights API (Google)

How It Works 🧠
User enters a website URL in the input form.

Flask backend sends a request to the PageSpeed Insights API with the provided URL.

The API returns Core Web Vitals and other performance metrics.

The frontend displays these metrics in an easy-to-read format.

Setup Instructions ⚙️
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Install required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Set your API key (if required) in the configuration.

Run the application:

bash
Copy
Edit
python app.py
Open http://localhost:5000 in your browser.

Future Improvements 🌟
Add graphical charts for vitals visualization.

Support for mobile and desktop device analysis separately.

Store previous analysis results in a database for historical tracking.
