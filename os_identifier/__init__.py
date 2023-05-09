import sys

LINUX = 'Linux'
WINDOWS = 'Windows'
MAC = 'Mac'

OS = MAC
NEW_LINE_SYMBOL = '\n'
if sys.platform == "linux" or sys.platform == "linux2":
    OS = LINUX
elif sys.platform == "darwin":
    OS = MAC
elif sys.platform == "win32":
    OS = WINDOWS
    NEW_LINE_SYMBOL = '¥¥'

is_linux = OS == LINUX
is_windows = OS == WINDOWS
is_mac = OS == MAC
