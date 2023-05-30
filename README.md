# Face_Detection_Monitor_Energy_Saver
Webcam scans for faces. If face is found: initiates "caffeinate" on macOS and therefore delays the initiation of sleep.
Goal is to save energy. Therefore set your monitors sleep delay to one minute in the OS. If your face is not found: monitor will
go to sleep after one minute. If your face is found: your monitor will not go to sleep and you can read or whatever you do without 
interruption.
