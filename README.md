# CC_Project_LightRez
# App Usage
- Connect Arduino and upload Sketch code for enabling photoresistor to measure light intensity values per second.
- Write serial values to CSV and export to AWS S3 Bucket.
- AWS Lambda trigger event reads CSV file and calculates energy consumption of LED in watts-second.
- AWS QuickSight visualizes the trend of one month of light intensities and LED uptime.
# Team
- [@github/rakshandha16](https://github.com/rakshandha16)
- [@github/SreeTejaVarma](https://github.com/SreeTejaVarma)
# App Design
![alt text](https://github.com/surhud004/CC_Project_LightRez/blob/master/Picture1.png)
# App Screenshots
### AWS S3 Bucket
![alt text](https://github.com/surhud004/CC_Project_LightRez/blob/master/Picture2.png)
### AWS Lambda Output
![alt text](https://github.com/surhud004/CC_Project_LightRez/blob/master/Picture3.png)
### Arduino Simulation
![alt text](https://github.com/surhud004/CC_Project_LightRez/blob/master/Capture.PNG)
### AWS QuickSight
![alt text](https://github.com/surhud004/CC_Project_LightRez/blob/master/Picture4.png)
