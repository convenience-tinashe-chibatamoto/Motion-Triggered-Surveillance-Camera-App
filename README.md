# Motion-Triggered Surveillance Camera App

This is a motion-triggered surveillance camera application that captures images when motion is detected and sends an email notification with the captured image.

## Features
- Captures video from the webcam.
- Detects motion and highlights the detected area.
- Saves images when motion is detected.
- Sends an email with the captured image when motion is detected.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/convenience-tinashe-chibatamoto/Motion-Triggered-Surveillance-Camera-App.git
    cd Motion-Triggered-Surveillance-Camera-App
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for email:
    ```bash
    export PASSWORD='your_email_password'
    ```

## Usage

1. Run the main application:
    ```bash
    python main.py
    ```

2. Press `q` to quit the application.

## Files

- `main.py`: The main application file that handles video capture, motion detection, and image saving.
- `emailing.py`: Handles sending an email with the captured image.

## Code Overview

### main.py

- Captures video from the webcam.
- Converts frames to grayscale and applies Gaussian blur.
- Computes the difference between the current frame and the first frame to detect motion.
- Draws rectangles around detected motion areas and saves the frames as images.
- Sends an email with an image when motion is detected.
- Cleans up saved images periodically.

### emailing.py

- Sends an email with the middle image as an attachment.
- Uses SMTP to send the email via Gmail.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

---
