# 파이썬에서 아두이노 데이터를 읽는법

**PySerial** 이 모듈은 직렬포트에 대한 접근을 캡슐화합니다.

## 설치

**Development Software**
* [Windows](https://www.arduino.cc/en/Guide/Windows)에서 아두이노 소프트웨어(IDE) 설치
* [Linux](https://www.arduino.cc/en/Guide/Linux)에서 아두이노 소프트웨어(IDE) 설치
* [OS X](https://www.arduino.cc/en/Guide/MacOSX)에서 아두이노 소프트웨어(IDE) 설치

## 요구사항

Python 2.7 또는 Python 3.4 이상
Windows에서 실행중인 경우 : Windows 7 이상
Jython에서 실행중인 경우 : "Java Communications"(JavaComm) 또는 Java용 호환가능한 확장판

**From PyPI**

- pip를 pip 버전 18.1로 업그레이드하는 것이 좋습니다:

```sh
   python -m pip install --upgrade pip
```

- 파이썬에서 아두이노 사용하기위해 PySerial 설치

```sh
   python -m pip install PySerial
```

**From Conda**

- pySerial은 Conda에서 설치할 수 있습니다:

```sh
conda install pyserial
```

또는

```
conda install -c conda-forge pyserial
```

> Windows에서 경로:
```
   c:\users\name-user\appdata\local\programas\python\python36-32\lib\site-packages
```

## 파이썬 스크립트 작성

- serial 가져오기

```python
import serial
```

- 아두이노가 연결된 포트르 설정하십시오.

```python
PuertoSerie =serial.Serial('COM4', 9600)
```

- bucle에서 아두이노로 보낸 응답(데이터)을 기다립니다.

```python
while True:
	sArduino = PuertoSerie.readline()
	print (sArduino)
```

- <code> .py </code>를 스크립트합니다.:

```python
import serial
PuertoSerie =serial.Serial('COM4', 9600)
while True:
	sArduino = PuertoSerie.readline()
	print (sArduino)
```

## 아두이토 스크립트 작성

- 데이터를 전송하는 변수를 설정:

```ardunio
int sensorValue = 0;
```

- setup()에서 직렬포트는 이 경우엔 9600에서 초기화됩니다 (파이썬 스크립트와 동일)

```ardunio
void setup(){
  Serial.begin(9600);
}
```

- loop()에서 아날로그 입력은 (이 예시 에서는)포트A0에 의해 수신됩니다

- 파이썬으로 전송될 센서의 값은 직렬 포트에 기록됩니다

```ardunio
void loop(){
  sensorValue = analogRead(A0);
  Serial.println(sensorValue);
}
```

- `.ino` 스크립트를 작성하세요:

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

## 실행되는 단게
1. 아두이노 보드의 센서를 연결하십시오
2. 아두이노 스크립트를 컴파일하고 아두이노 카드에 업로드
3. 콘솔에서 파이썬 스크립트 실행

```shell
rute\python name-project.py
```
## Conexion 예시

다음 비디오에서는 예제 구현을 보여줍니다.:
https://youtu.be/0e9yuELxgFU.

감사합니다