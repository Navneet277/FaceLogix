from flask import Flask, render_template, jsonify
import subprocess
import threading
import csv
import os

app = Flask(__name__)

# Home page → loads the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Function to run facial recognition script
def start_recognition():
    subprocess.run(['python', 'AttendanceProject.py'])

# Start recognition via POST request from button
@app.route('/run', methods=['POST'])
def run_recognition():
    try:
        # Run recognition in background so Flask doesn't freeze
        thread = threading.Thread(target=start_recognition)
        thread.start()
        return jsonify({"status": "success", "message": "Facial recognition started. Webcam window will appear."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# API endpoint to fetch live attendance data
@app.route('/attendance')
def get_attendance():
    attendance_data = []
    if os.path.exists('Attendance.csv'):
        with open('Attendance.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header if exists
            for row in reader:
                if row:  # Avoid empty rows
                    attendance_data.append({"name": row[0], "datetime": row[1]})
    return jsonify(attendance_data)

if __name__ == '__main__':
    app.run(debug=True)
