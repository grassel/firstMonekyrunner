
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice





# launches the browser, if it is not running, yet
# raises browser to foreground if it is running already
def launchChrome():
    # info from https://stackoverflow.com/questions/28150650/open-chrome-with-adb
    device.startActivity(component='com.android.chrome/com.google.android.apps.chrome.Main')
    MonkeyRunner.sleep(3.0)
    return

# launches the browser, if it is not running, yet
# raises browser to foreground if it is running already
def launchHWBrowser():
    device.startActivity(component='com.huawei.browser/com.google.android.apps.chrome.Main')
    MonkeyRunner.sleep(3.0)
    return


# enters given URL to the URL bar and hits enter key
def enterURL(u):
   device.wake()

   # we might be in the middle of the page and URL bar not visible
   # scroll the page just enough to make sure URL bar is visible
   device.drag ((400, 600), (400, 590), steps=5, duration=0.2)
   MonkeyRunner.sleep(0.5)

    # move focus to the URL box
   device.touch(250, 157, MonkeyDevice.DOWN_AND_UP) 

   # all text in the URL bar will be selected
   # hit DEL to clear URL bar
   device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)

   #enter URL and hit 'enter' 
   device.type(u + '\n')
   return



   
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
#device.installPackage('myproject/bin/MyApplication.apk')


launchHWBrowser()


# Presses the Menu button
#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
#result = device.takeSnapshot()

# Writes the screenshot to a file
#result.writeToFile('./shot1.png','png')

enterURL('https://www.grassel.org/')
MonkeyRunner.sleep(3.0)

#device.drag ((400, 900), (200, 100), steps=400, duration=3.0)
#device.drag ((200, 100), (200, 900), steps=400, duration=2.0)


