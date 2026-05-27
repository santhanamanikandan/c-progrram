from cx_Freeze import setup, Executable

setup(
    name="GoldLoanApp",
    version="1.0",
    description="A Python application for gold loan processing",
    executables=[Executable("project.py")]
)
