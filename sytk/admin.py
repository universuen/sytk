import functools
import ctypes
import sys


def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()


class _Admin:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        if is_admin():
            self.func(*args, **kwargs)
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            self.func(*args, **kwargs)


admin = _Admin