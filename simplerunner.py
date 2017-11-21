
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
   MonkeyRunner.sleep(1.0)

    # move focus to the URL box
   device.touch(420, 150, MonkeyDevice.DOWN_AND_UP) 
   MonkeyRunner.sleep(1.5)

   # hit the clear button on the right hand side
   device.touch(1020, 150, MonkeyDevice.DOWN_AND_UP) 
   MonkeyRunner.sleep(1.5)

   #enter URL and hit 'enter' 
   device.type(u)
   MonkeyRunner.sleep(1.5)
   
   # hit the submit button on the keyboard
   device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
   MonkeyRunner.sleep(1.5)
   return


def scrollDownPages(n):
    device.touch(400, 1700, MonkeyDevice.MOVE) 
    while n >= 0:
      n -= 1
      device.drag ((400, 1600), (400, 350), steps=100, duration=0.5)
    return
   
def scrollUpPages(n):
    device.touch(400, 350, MonkeyDevice.MOVE) 
    while n >= 0:
      n -= 1
      device.drag ((400, 350), (400, 1600), steps=100, duration=0.5)
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

enterURL('https://www.w3.org/')
MonkeyRunner.sleep(5.0)

scrollDownPages(5)
scrollUpPages(5)


