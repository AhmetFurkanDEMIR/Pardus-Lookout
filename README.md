![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![](https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white) ![](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)

# Pardus Lookout

We protect the privacy of the data on your computer by using the camera of your [Debian](https://www.debian.org/) based [Pardus](https://www.pardus.org.tr/) operating system.

The application is written in Python programming language, the visual interface is written with the Qt framework, and the AI, that is, face detection, is provided with the [Google MediaPipe](https://mediapipe.dev/) framework.

If it is necessary to explain the general logic of the application, faces are searched with Google MediaPipe in the images taken from your camera, after these face detections, your computer will protect itself according to the mode you choose.


## Mods and Actions

**Mode 1 (Screen Privacy) :** If more faces are detected than the tolerable number of faces you selected in this mode, it means that your computer is in danger, that is, it is being watched. If your computer is being watched, it will react according to the action you choose.

**Mode 2 (Screen Sentry) :** In this mode, you can use it in situations where you have to leave your computer on and not be able to stand by (for example, updates or downloads), if a face is detected between the start and end dates, it means that someone other than you is at the computer. If you are not at your computer, it will react according to the action you choose.

**Mode 3 (Sleep Mode) :** In this mode, if no face can be detected at the computer within the specified time (minutes), your computer performs the selected action for power saving.

**Actions ->>** **Shut Down :** If one of the above three conditions occurs, the computer is shut down. **Suspend :** If one of the above three conditions occurs, the computer is Suspend. **Warn :** If one of the above three conditions occurs, the computer is Warn.


### Requirements, supported Operating Systems and executables

|Operating systems | Support status | 
|----------------- |--------------- |
|      [Pardus](https://www.pardus.org.tr/)     |         ✓      |
|      [Ubuntu](https://ubuntu.com/)      |        ○       | 
|    [Linux Mint](https://linuxmint.com/)    |        ○       |
|   [Windows 10-11](https://www.microsoft.com/tr-tr/windows)  |      X         |

If you want to run the application through Python scripts, you must install the necessary packages with the following commands.

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev
sudo apt-get install python3-pip
pip3 install PyQt5
pip3 install opencv-python
pip3 install mediapipe
pip3 install qdarkstyle
```

From the [Release]() section, you can access the executable ready files compiled for Pardus/Debian.


### Demo video of the app
 

