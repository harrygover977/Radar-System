# Ultrasonic Radar System

A real-time radar visualisation system built using an Arduino, ultrasonic sensor, and Python. This project scans the environment by rotating a sensor across 180°, measuring distances, and rendering the results in a radar-style interface using Pygame.

---

## 🎥 Demo

Demo Coming soon...

---

## 📌 Overview

This project combines embedded systems and software to simulate a radar system. An ultrasonic sensor mounted on a servo motor sweeps across a range of angles, collecting distance data which is transmitted to a Python application for real-time visualisation.

The goal was to explore sensor integration, real-time data handling, and graphical rendering.

---

## 🚀 Features

- 180° environmental scanning using a rotating ultrasonic sensor  
- Real-time distance detection and display  
- Radar-style visualisation using Pygame  
- Live serial communication between Arduino and Python  
- Angle-based object detection mapping  
- Threaded data handling for smooth performance  

---

## 🛠️ Tech Stack

### Hardware
- Arduino  
- HC-SR04 Ultrasonic Sensor  
- Servo Motor  

### Software
- Python 3.13.1  
- Pygame  
- PySerial  
- NumPy  
- Pandas  

---

## 🔌 Hardware Setup

The system consists of:
- An ultrasonic sensor mounted on a servo motor  
- Both components connected to an Arduino  

The servo rotates the sensor from 1° to 180°, while the ultrasonic sensor measures distance at each angle.

> 📄 A detailed wiring diagram is included in the (`Project Overview.docx`).

---

## 💻 System Architecture

Arduino ➡️ Serial Communication ➡️ Python Backend ➡️ Radar Visualisation

### Flow:
1. The Arduino rotates the servo motor incrementally  
2. At each angle, the ultrasonic sensor measures distance  
3. Data is sent via serial communication (baud rate: 9600)  
4. Python reads the incoming data stream  
5. The radar interface updates in real time  

---

## ⚙️ Installation & Usage

### 1. Upload Arduino Code
- Open `hardware_code.ino` in the Arduino IDE  
- Select the correct board and port  
- Upload to your Arduino  

### 2. Set Up Python Environment
```bash
pip install -r requirements.txt
```

### 3. Configure Serial Connection

- Set your COM port (default: COM6)
- Baude Rate: 9600

### 4. Run the Application
```bash
python radar.py
```

---

## 🧪 Challenges & Solutions

### Real-Time Data Handling

Problem: Reading serial data while rendering caused performance issues

Solution: Implemented threading to handle data input and visualisation concurrently

### Angle Synchronization

Problem: Mismatch between servo position and radar display angle

Solution: Shared a synchronized angle variable using a thread-safe lock (data_lock)

---

## 📈 Why This Project Matters

This project demonstrates:
- Integration of hardware and software systems
- Real-time data processing and visualisation
- Understanding of concurrency (threading)
- Practical use of sensors in robotics

It reflects core skills relevant to robotics and AI engineering, particularly in perception systems and sensor-driven applications.

## 📬 Contact

If you have any questions or suggestions, feel free to get in touch!

[Harry Gover - LinkedIn](https://linkedin.com/in/harry-gover-72344331b)
