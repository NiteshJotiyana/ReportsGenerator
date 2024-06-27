import subprocess
import pyautogui
import time

def take_screenshot_active_window(position: tuple, size: tuple,screenshots_path:str):
    left, top = position
    width, height = size
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save(screenshots_path + '_screenshot.png')


def take_screenshot_chromeTabs(position: tuple, size: tuple,tab_count:int,screenshots_path:str):
    # activate chrome window
    applescript_cmd = '''
                        tell application "Google Chrome" 
                            if it is running then
                                activate
                            end if
                        end tell
                        '''

    left, top = position
    width, height = size
    subprocess.run(['osascript', '-e', applescript_cmd], capture_output=True, text=True)
    time.sleep(2)

    image_files=[]
    for i in range(tab_count):
        with pyautogui.hold(['shift', 'ctrl']):
            pyautogui.press(['tab'])
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        file_name=screenshots_path + "tab_" + str(i) + '_screenshot.png'
        screenshot.save(file_name)
        image_files.append(file_name)

    return image_files


