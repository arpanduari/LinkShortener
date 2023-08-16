# URL Shortener Project

Welcome to the URL Shortener project! This application allows users to create shortened links for long URLs. It's built using Python, Flask for the backend, and HTML, CSS, and Bootstrap for the frontend.

## Features

- Shorten URLs using different shortening services.
- Copy shortened links to the clipboard with a single click.
- Clean and responsive user interface.

## Demo

You can access the live demo of the URL Shortener at [https://linkshortener-29x6.onrender.com](https://linkshortener-29x6.onrender.com).

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/url-shortener.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the App

### Method 1: Directly

3. Run the Flask app directly:

```bash
python app.py
```

4. Access the app in your web browser at [http://localhost:5000](http://localhost:5000).

### Method 2: Using Gunicorn

3. Install Gunicorn (if not installed):

```bash
pip install gunicorn
```

4. Run the app using Gunicorn:

```bash
gunicorn app:app
```

5. Access the app in your web browser at [http://localhost:8000](http://localhost:8000).

## Usage

1. Open the app in your web browser.

2. Enter the URL you want to shorten in the input field.

3. Click the "Shorten" button to generate shortened links using various shortening services.

4. Copy the shortened link to the clipboard by clicking the "Copy" button next to the link.

## Deployed on Render

This project is deployed using Render, a cloud platform for deploying and scaling applications. You can access the live version of the URL shortener at [https://linkshortener-29x6.onrender.com](https://linkshortener-29x6.onrender.com).

## Credits

- Designed by [Arpan Duari](https://github.com/arpanduari).
- Powered by [Bootstrap](https://getbootstrap.com/).
