# sensorstreamer
Python sensor data receiver from the [Sensor fusion app](http://users.isy.liu.se/en/rt/fredrik/app/) by Fredrik Gustafsson, Linköping University

## Usage 

~~~~
python sensorstreamer.py > output.csv
~~~~

Don't forget to start streaming in the app. The default port is tcp/3400.


## Example output

### Accelerometer

~~~~
122130049   ACC 0.38068968  2.7175019   9.308941
~~~~

Columns are 
 - time [ms]
 - sensor
 - x-value
 - y-value
 - z-value
 