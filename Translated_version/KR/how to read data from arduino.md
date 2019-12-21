```python
import serial
import csv
import re
import matplotlib.pyplot as plt
import pandas as pd
 
portPath = "/dev/ttyACM0"       # 아두이노 IDE에 표시된 값과 일치해야합니다
baud = 115200                     # 아두이노 전송 속도와 일치해야합니다
timeout = 5                       
filename = "data.csv"
max_num_readings = 16000
num_signals = 1
 
 
 
def create_serial_obj(portPath, baud_rate, tout):
    """
    포트 경로, 전송 속도 및 시간 초과 값이 주어지면 pyserial 개체를 만들고 반환합니다.

    """
    return serial.Serial(portPath, baud_rate, timeout = tout)
    
def read_serial_data(serial):
    """
    pyserial 객체(시리얼)가 주어졌습니다. 직렬포트에서 읽은 list라인들을 출력합니다
    """
    serial.flushInput()
    
    serial_data = []
    readings_left = True
    timeout_reached = False
    
    while readings_left and not timeout_reached:
        serial_line = serial.readline()
        if serial_line == '':
            timeout_reached = True
        else:
            serial_data.append(serial_line)
            if len(serial_data) == max_num_readings:
                readings_left = False
        
    return serial_data
 
def is_number(string):
    """
    주어진 문자열은 숫자를 나타내는 경우 True를 반환합니다. 그렇지 않으면 False를 반환합니다.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False
        
def clean_serial_data(data):
    """
    직렬 회선 (데이터) 목록이 제공됩니다. 모든 문자를 제거합니다.
    정리 된 자릿수 목록을 리턴합니다.
    다음과 같이 주어진 경우 : [ '0.5000,33 \ r \ n', '1.0000,283 \ r \ n']
    반환 값 : [[0.5,33.0], [1.0,283.0]]

    """
    clean_data = []
    
    for line in data:
        line_data = re.findall("\d*\.\d*|\d*",line) # Find all digits
        line_data = [float(element) for element in line_data if is_number(element)] # Convert strings to float
        if len(line_data) >= 2:
            clean_data.append(line_data)
 
    return clean_data           
 
def save_to_csv(data, filename):
    """
    list(데이터) 목록들을 파일이름으로 저장
    """
    with open(filename, 'wb') as csvfile:
        csvwrite = csv.writer(csvfile)
        csvwrite.writerows(data)
 
def gen_col_list(num_signals):
    """
    신호 수가 주어지면 데이터의 list의 열을 반환합니다.
     예 : 3 개의 신호가 리스트를 반환합니다 : [ 'Time', 'Signal1', 'Signal2', 'Signal3']
    """
    col_list = ['Time']
    for i in range(1,num_signals+1):
        col = 'Signal'+str(i)
        col_list.append(col)
        
    return col_list
    
def map_value(x, in_min, in_max, out_min, out_max):
    return (((x - in_min) * (out_max - out_min))/(in_max - in_min)) + out_min
 
    
def simple_plot(csv_file, columns, headers):
    plt.clf()
    plt.close()
    plt.plotfile(csv_file, columns, names=headers, newfig=True)
    plt.show()
 
def plot_csv(csv_file, cols):
    # CSV 데이터에서 Pandas DataFrame 만들기
    data_frame = pd.read_csv(csv_file)
    # 열의 이름을 설정하십시오
    data_frame.columns = cols
    # 첫번째 열(시간)을 index로 설정 
    data_frame = data_frame.set_index(cols[0])
    # 전압 값을 0-1023에서 0-5로 매핑
    data_frame = data_frame.apply(lambda x: map_value(x,0.,1023,0,5))
    # 시간열을 다시 가져 오기
    data_frame = data_frame.reset_index()
    plt.clf()
    plt.close()
    # 데이터 Plot
    data_frame.plot(x=cols[0],y=cols[1:])
    plt.show()
    
    
print "Creating serial object..."
serial_obj = create_serial_obj(portPath, baud, timeout)
 
print "Reading serial data..."
serial_data = read_serial_data(serial_obj)
print len(serial_data)
 
print "Cleaning data..."
clean_data =  clean_serial_data(serial_data)
 
print "Saving to csv..."
save_to_csv(clean_data, filename)
 
print "Plotting data..."
#simple_plot(filename, (0,1,2), ['time (s)', 'voltage1', 'voltage2'])
#simple_plot(filename, (0,1), ['time (s)', 'voltage1'])
plot_csv(filename, gen_col_list(num_signals))
```
