import sys
sys.path[0] = "D:\Anaconda3\Lib\site-packages"
from cx_Freeze import setup
from cx_Freeze import Executable
setup(name="ReportTestResultToTestLink", version="1.0", description="the first release", executables=[Executable("C:\workspace\ReportTestResultToTestLink\ReportTestResultToTestLink.py")])