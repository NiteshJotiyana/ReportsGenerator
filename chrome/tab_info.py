import subprocess

# Define the AppleScript command
applescript_cmd = '''
tell application "Google Chrome"
    set tabNames to {}
    repeat with theWindow in windows
        repeat with theTab in tabs of theWindow
            set tabName to name of theTab
            set end of tabNames to tabName
        end repeat
    end repeat
    return tabNames
end tell
'''

# Execute the AppleScript command using subprocess
result = subprocess.run(['osascript', '-e', applescript_cmd], capture_output=True, text=True).stdout.strip()
print(type(result))
print(result)


