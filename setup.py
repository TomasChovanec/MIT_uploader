import sys
import os
from cx_Freeze import setup, Executable 

build_exe_options =  \
{"includes": [ \
 "serial", \

 ]}

exe = Executable(
      script="MIT_uploader.py",
     )
setup(
      name="MIT_uploader.exe",
      author="Tomas Chovanec",
      description="Some description",
      options={"build_exe": build_exe_options},
      executables=[exe]
      )