import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],
                     "include_files":[("dict.txt","dict.txt"),("dict_model.txt","dict_model.txt"),("config.conf","config.conf")]
                     }
# GUI applications require a different base on Windows (the default is for a
# console application).

setup(  name = "wordmachine",
        version = "0.1",
        description = "看什么看，guna",
        options = {"build_exe": build_exe_options},
        executables = [Executable("wordmachine.py",icon="gwyndolin.ico")])