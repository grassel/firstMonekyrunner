import time    

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
#device.installPackage('myproject/bin/MyApplication.apk')

# info from https://stackoverflow.com/questions/28150650/open-chrome-with-adb

# sets a variable with the package's internal name
package = 'com.android.chrome'

# sets a variable with the name of an Activity in the package
activity = 'com.google.android.apps.chrome.Main'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)
time.sleep(3.0)

# Presses the Menu button
#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
#result = device.takeSnapshot()

# Writes the screenshot to a file
#result.writeToFile('./shot1.png','png')


device.drag ((400, 900), (200, 100), steps=400, duration=3.0)
device.drag ((200, 100), (200, 900), steps=400, duration=2.0)

# from https://gist.github.com/sjp38/6202539

# Touch down screen                                                                               
device.touch(100, 500, MonkeyDevice.DOWN)                                           

# Move from 100, 500 to 300, 500
for i in range(1, 11):                                                              
    device.touch(100, 800-50*i, MonkeyDevice.MOVE)                              
    print "move ", 100 + 20 * i, 500                                                
    time.sleep(0.1)             

# Move from (300, 500 to 200, 500)                                                    
for i in range(1, 11):                                                              
    device.touch(300, 500 - 10 * i, MonkeyDevice.MOVE)                              
    print "move ", 300, 500 - 10 * i                                                
    time.sleep(0.1)                                                                 

# Remove finger from screen
device.touch(300, 400, MonkeyDevice.UP) 


