# Serial-Sampling-Rate-Measurement
Sampling rate, also known as sampling frequency, is a fundamental concept in digital signal processing. It refers to the number of samples taken per second from a continuous signal to convert it into a discrete signal. A faster sampling rate will provide a better representation of the original signal.

# Note
Change to your actual port
```
SERIAL_PORT = 'COM16'
```
In Linux environment, change it accordingly to the specific port
```
SERIAL_PORT = '/dev/ttyUSB0'
```

#Change the baud rate according to the setting
```
BAUD_RATE = 115200
```

# Result for reference
```
Measuring sampling rate for 10 seconds...
Total samples received: 4432
Elapsed time: 10.00 seconds
Sampling rate: 443.07 samples/second
```

