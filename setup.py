# setup.py
from cx_Freeze import setup, Executable

setup(
    name="chdmandir",
    version="1.0",
    description="An attempt to run chdman recursively in a directory",
    executables=[Executable("main.py")]
)
