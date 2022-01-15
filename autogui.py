import pyautogui
import webbrowser
import win32gui
import re
import time
from config import chrome_path
from pyautogui import PyAutoGUIException
import win32api


def open_browser(url):
    switch_to_eng()
    webbrowser.get(chrome_path).open(url, new=3, autoraise=True)
    window = WindowMgr()
    window.find_window_wildcard(".*Chrome.*")
    window.set_foreground()


def wait_img(img):
    waiting = 1
    while waiting:
        try:
            res = pyautogui.locateCenterOnScreen(img)
            if res is not None:
                print("found..." + img)
                waiting = 0
                pyautogui.click(res[0], res[1])
        except PyAutoGUIException:
            print("waiting..." + img)
            time.sleep(1)
    return res


def switch_to_eng():
    win32api.LoadKeyboardLayout('00000409', 1)  # to switch to english


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)
