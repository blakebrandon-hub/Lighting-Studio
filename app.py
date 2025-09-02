#!/usr/bin/env python3
"""
Lighting Studio - 3D Reference Tool for Artists
A lightweight Flask server to serve the 3D lighting reference application.
Built with help from Claude AI.
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main lighting studio application."""
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files (CSS, JS, etc.)."""
    return send_from_directory('static', filename)

@app.route('/about')
def about():
    """About page with information about the tool."""
    return render_template('about.html')

@app.errorhandler(404)
def not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Check if we're running in production (like Heroku)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print("🎨 Lighting Studio Server Starting...")
    print(f"📍 Running on http://localhost:{port}")
    print("🎯 Ready to help artists study lighting and form!")
    
    app.run(host='0.0.0.0', port=port, debug=debug)