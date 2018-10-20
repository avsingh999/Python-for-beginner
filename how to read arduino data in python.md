# how to read arduino data in python

**PySerial** This module encapsulates the access for the serial port.

## Install

**Development Software**
* Install Arduino Software (IDE) on [Windows](https://www.arduino.cc/en/Guide/Windows)
* Install Arduino Software (IDE) on [Linux](https://www.arduino.cc/en/Guide/Linux) 
* Install Arduino Software (IDE) on [OS X](https://www.arduino.cc/en/Guide/MacOSX) 

## Requirements

Python 2.7 or Python 3.4 and newer
If running on Windows: Windows 7 or newer
If running on Jython: “Java Communications” (JavaComm) or compatible extension for Java

**From PyPI**

- Consider upgrading pip to pip version 18.1 is available:

```sh
   python -m pip install --upgrade pip
```

- Install PySerial to use Python with Arduino

```sh
   python -m pip install PySerial
```

**From Conda**

- pySerial can be installed from Conda:

```sh
conda install pyserial
```

or

```
conda install -c conda-forge pyserial
```

> Route in Windows:
```
   c:\users\name-user\appdata\local\programas\python\python36-32\lib\site-packages
```

## Script Python

-Import serial

```python
import serial
```

-Establish the port in which the arduino is connected

```python
PuertoSerie =serial.Serial('COM4', 9600)
```

-In a bucle wait for the response (data) sent from the arduino

```python
while True:
	sArduino = PuertoSerie.readline()
	print (sArduino)
```

-Script <code> .py </code>:

```python
import serial
PuertoSerie =serial.Serial('COM4', 9600)
while True:
	sArduino = PuertoSerie.readline()
	print (sArduino)
```

## Script Arduino

-Establish a variable that is sending the data:

```ardunio
int sensorValue = 0;
```

-In the setup () the serial port is initialized in this case in 9600 (same as in the Python script)

```ardunio
void setup(){
  Serial.begin(9600);
}
```

-In loop () the analog input is received (in this example) by port A0.

-The value of the sensor that will be sent to Python is written to the serial port

```ardunio
void loop(){
  sensorValue = analogRead(A0);
  Serial.println(sensorValue);
}
```

- Script `.ino`:

```ardunio
int sensorValue = 0;
void setup(){
  Serial.begin(9600);
}
void loop(){
  sensorValue = analogRead(A0);
  Serial.println(sensorValue);
}
```

## Steps to execute it
1. Make the connection of the sensors on the arduino board
2. Compile and upload arduino script to the Arduino card
3. Running the Python script in console

```shell
rute\python name-project.py
```
## Conexion with a example

In the next video show the implementig the example:
https://youtu.be/0e9yuELxgFU.

Thank you