🖱️ AI Virtual Mouse

A computer vision project that allows users to control the mouse cursor using hand gestures detected through a webcam.

This project uses Python, OpenCV, MediaPipe, NumPy, and Autopy to detect hand movements and convert them into mouse actions like cursor movement, left click, and right click.

The system works in real time and demonstrates how Artificial Intelligence and Computer Vision can create touchless human-computer interaction systems.

📚 Table of Contents

Project Overview

Features

Technologies Used

Project Structure

System Requirements

Installation

How the System Works

Gesture Controls

Code Explanation

Hand Tracking Module

Cursor Movement Logic

Click Detection Logic

FPS Calculation

Future Improvements

Applications

Limitations

Author

📌 Project Overview

The AI Virtual Mouse is designed to replace the traditional mouse with hand gestures.

Instead of using a physical mouse, the user moves their fingers in front of a webcam.

The program detects the hand using MediaPipe and tracks the position of finger landmarks.

Using this information, the program interprets gestures and performs mouse actions.

This project demonstrates several important computer vision concepts:

Real-time hand detection

Finger tracking

Gesture recognition

Screen coordinate mapping

Hardware automation

The project is useful for beginners who want to learn about AI, computer vision, and gesture-based interfaces.

✨ Features

The AI Virtual Mouse includes the following features:

Real-time hand tracking

Cursor movement using index finger

Left click gesture

Right click gesture

Smooth cursor movement

Webcam-based interaction

Frame rate (FPS) display

Simple and lightweight system

Beginner friendly project

🧰 Technologies Used

This project uses the following technologies:

Python

Python is the main programming language used in this project.

It is widely used in AI and machine learning applications.

Python allows easy integration of multiple libraries.

OpenCV

OpenCV is used for:

Capturing webcam video

Processing frames

Drawing shapes on the screen

Displaying the output window

OpenCV allows real-time image processing.

MediaPipe

MediaPipe is a machine learning framework developed by Google.

It provides pre-trained models for detecting body landmarks.

In this project, the MediaPipe Hands model is used.

It detects 21 landmarks on the hand.

These landmarks allow accurate finger tracking.

NumPy

NumPy is used for numerical calculations.

In this project it is mainly used for:

Coordinate mapping

Mathematical interpolation

Autopy

Autopy is used to control the computer mouse.

It allows the program to:

Move the mouse cursor

Perform left click

Perform right click

📂 Project Structure
AI-Virtual-Mouse
│
├── AIVirtualMouse.py
├── HandTrackingModule.py
└── README.md
AIVirtualMouse.py

This is the main program.

It performs:

Webcam capture

Gesture detection

Mouse control

HandTrackingModule.py

This module handles:

Hand detection

Landmark detection

Finger tracking

Distance calculation

Separating the code into modules makes the project easier to manage.

💻 System Requirements

Minimum requirements:

Python 3.8 or higher

Webcam

Windows / Linux / MacOS

Recommended:

Python 3.10+

Good lighting

HD webcam

⚙️ Installation

Follow the steps below to run the project.

1 Clone the Repository
git clone https://github.com/yourusername/AI-Virtual-Mouse.git
2 Go to the Project Folder
cd AI-Virtual-Mouse
3 Install Required Libraries

Install the required packages:

pip install opencv-python
pip install mediapipe
pip install numpy
pip install autopy

or install using requirements file:

pip install -r requirements.txt
🚀 Running the Project

Run the main program:

python AIVirtualMouse.py

The webcam will start and the virtual mouse system will begin.

Press ESC to exit the program.

🧠 How the System Works

The system works in several steps.

The webcam captures video frames.

Each frame is processed using OpenCV.

MediaPipe detects the hand and identifies landmarks.

Landmark coordinates are extracted.

The system checks which fingers are raised.

Gestures are recognized.

Mouse actions are executed.

This process repeats continuously for real-time interaction.

✋ Gesture Controls

The system recognizes different gestures.

Cursor Movement

Gesture:

Index finger raised.

Action:

Moves the mouse cursor across the screen.

The cursor follows the movement of the index finger.

Left Click

Gesture:

Index finger and middle finger brought close together.

Action:

Performs a left mouse click.

The system measures the distance between the fingertips.

If the distance is small enough, a click is triggered.

Right Click

Gesture:

Thumb and index finger pinch.

Action:

Performs a right mouse click.

This gesture is detected by measuring the distance between thumb and index finger.

🧩 Code Explanation

The project contains two main components:

Hand tracking system

Mouse control system

🤖 Hand Tracking Module

The HandTrackingModule.py file handles hand detection.

It uses MediaPipe Hands.

First, the image is converted from BGR to RGB.

MediaPipe processes the RGB image.

If a hand is detected, it returns landmark coordinates.

These coordinates represent positions on the hand.

The module then draws the landmarks and connections.

This helps visualize the hand skeleton.

📍 Landmark Detection

MediaPipe detects 21 landmarks on the hand.

Each landmark has a specific ID.

Important landmarks:

Landmark ID	Finger
4	Thumb Tip
8	Index Finger Tip
12	Middle Finger Tip
16	Ring Finger Tip
20	Pinky Tip

These landmarks are used to detect gestures.

✌️ Finger Detection

The program determines which fingers are raised.

This is done by comparing the position of finger tips and joints.

If the fingertip is above the joint, the finger is considered raised.

If it is below, the finger is folded.

The system stores this information in a list.

Example:

[0,1,0,0,0]

This means only the index finger is raised.

🖱️ Cursor Movement Logic

Cursor movement is based on the index finger position.

The index finger coordinates from the webcam are mapped to screen coordinates.

However, camera resolution and screen resolution are different.

Therefore, interpolation is used.

Example:

x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))

This converts camera coordinates to screen coordinates.

🎯 Smooth Cursor Movement

Direct cursor mapping can cause jitter.

To fix this, the program uses smoothing.

Formula used:

clocX = plocX + (x3 - plocX) / smoothening

This reduces sudden cursor jumps.

It makes the cursor movement smoother.

🖱️ Click Detection Logic

Click detection is based on the distance between fingers.

The program calculates the distance between two landmarks.

Example:

length = distance(index,middle)

If the distance is less than a threshold value, a click is triggered.

This method ensures accurate gesture detection.

📊 FPS Calculation

The program calculates Frames Per Second (FPS).

This helps measure performance.

FPS is calculated using time difference between frames.

Example:

fps = 1/(cTime - pTime)

Higher FPS means smoother performance.

🚀 Future Improvements

The project can be expanded with additional features.

Possible improvements include:

Scroll gesture

Drag and drop gesture

Multi-hand tracking

Gesture customization

Voice commands

GUI interface

Mobile camera support

Machine learning gesture recognition

🌍 Applications

AI Virtual Mouse can be used in many fields.

Examples include:

Touchless computer interaction

Smart home control

Accessibility tools

Gesture based gaming

Interactive presentations

AR/VR interfaces
