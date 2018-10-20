```python
import serial
import csv
import re
import matplotlib.pyplot as plt
import pandas as pd
 
portPath = "/dev/ttyACM0"       # Must match value shown on Arduino IDE
baud = 115200                     # Must match Arduino baud rate
timeout = 5                       # Seconds
filename = "data.csv"
max_num_readings = 16000
num_signals = 1
 
 
 
def create_serial_obj(portPath, baud_rate, tout):
    """
    Given the port path, baud rate, and timeout value, creates
    and returns a pyserial object.
    """
    return serial.Serial(portPath, baud_rate, timeout = tout)
    
def read_serial_data(serial):
    """
    Given a pyserial object (serial). Outputs a list of lines read in
    from the serial port
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
    Given a string returns True if the string represents a number.
    Returns False otherwise.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False
        
def clean_serial_data(data):
    """
    Given a list of serial lines (data). Removes all characters.
    Returns the cleaned list of lists of digits.
    Given something like: ['0.5000,33\r\n', '1.0000,283\r\n']
    Returns: [[0.5,33.0], [1.0,283.0]]
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
    Saves a list of lists (data) to filename
    """
    with open(filename, 'wb') as csvfile:
        csvwrite = csv.writer(csvfile)
        csvwrite.writerows(data)
 
def gen_col_list(num_signals):
    """
    Given the number of signals returns
    a list of columns for the data.
    E.g. 3 signals returns the list: ['Time','Signal1','Signal2','Signal3']
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
    # Create Pandas DataFrame from csv data
    data_frame = pd.read_csv(csv_file)
    # Set the names of the columns
    data_frame.columns = cols
    # Set the first column (Time) as the index 
    data_frame = data_frame.set_index(cols[0])
    # Map the voltage values from 0-1023 to 0-5
    data_frame = data_frame.apply(lambda x: map_value(x,0.,1023,0,5))
    # Bring back the Time column
    data_frame = data_frame.reset_index()
    plt.clf()
    plt.close()
    # Plot the data
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
