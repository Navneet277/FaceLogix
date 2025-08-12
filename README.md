# Facial Recognition Attendance System


A **Python + Flask** based application that uses your **webcam** to recognize known faces and automatically mark attendance in a CSV file.  
The project runs **locally** on your computer and cannot be hosted online because webcam access is required.

---

## 📌 Key Points

- **Runs Locally**: This is not an online/deployed project — it is meant to run on your personal computer with a webcam.

- **Known Faces Folder**: You must create a folder named **`ImagesAttendance`** and place images of the people whose faces should be recognized.

- **Automatic Attendance Logging**: Once a face is recognized, it is logged in `Attendance.csv` along with date and time.

- **Uses OpenCV & face_recognition**: OpenCV handles image processing and webcam capture, while the `face_recognition` library performs face encoding and matching.

---

## 🛠 How It Works
1. **Prepare Known Faces**  
   - Create a folder in the project directory named:
     ```
     ImagesAttendance
     ```
   - Add images of people to be recognized.

   - File names should represent the person's name.  
     Example:
     ```
     ImagesAttendance/
       John.jpg
       Alice.png
     ```

3. **Encoding Known Faces**  

   - The program reads each image from `ImagesAttendance`.

   - Converts the image from **BGR (OpenCV format)** to **RGB** (required for `face_recognition`).

    - Generates a **face encoding** — a unique numerical vector representing each face.

4. **Real-Time Recognition**  

   - The webcam feed is captured in real-time.

   - Each frame is resized for faster processing.

   - Faces in the current frame are encoded and compared with the stored known encodings.

   - If a match is found, the person's name is displayed on the video feed.

6. **Attendance Marking**  

   - Matches are checked against `Attendance.csv`.

    - If the person hasn’t been marked for today, a new entry is added:

     ```
     Name, Date/Time
     JOHN, 12/08/2025 14:23:11
     ```

---

## 📂 Project Structure

FacialRecognitionAttendanceSystem/
│
├── AttendanceProject.py # Main facial recognition logic

├── app.py # Flask backend to provide simple UI

├── Attendance.csv # Stores attendance logs

├── ImagesAttendance/ # Your folder with known faces

├── templates/

│ └── index.html # Minimal UI (Start Recognition + Attendance Table)

├── static/

│ └── style.css # Basic styling

├── requirements.txt # Python dependencies

└── README.md # This file


---


---

## ⚙️ Installation & Running the Project Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/face-recognition-attendance.git
   cd face-recognition-attendance

2. **Create Images Folder for Known Faces**

   ```bash
   mkdir ImagesAttendance

4. **Install Dependencies**

    ```bash
     pip install -r requirements.txt

6. **Run the Application**

    ```bash
    python app.py

8. **Access the Web Interface**

   Open your browser and go to:

    ```cpp
   http://127.0.0.1:5000

📊 Technologies Used

Python — Core programming language

Flask — To serve a simple UI

OpenCV (cv2) — For video capture, image resizing, and drawing rectangles/text

face_recognition — For generating face encodings and matching

NumPy — For numerical array operations

CSV File Handling — To store and check attendance records

💡 Example Workflow

You add John.jpg and Alice.png to ImagesAttendance/.

1. Start the app → Click Start Recognition in the browser.

2. The webcam opens → Faces detected and matched.

3. Matches are marked present in Attendance.csv.

4. The web page displays a Live Attendance Table from the CSV file.

📜 Notes

1. Works best with clear, front-facing images for known faces.

2. Each person should have only one image for faster encoding.

3. Multiple faces in a frame are supported.

📄 License

1. This project is open-source and free to use for educational purposes.

2. This project is local only — cloud deployment will not work due to lack of webcam access.
