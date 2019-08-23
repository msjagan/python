import shutil
import os
from pathlib import Path, PureWindowsPath

dest_path = PureWindowsPath("\\10.30.0.68\\sft\\IT - Chennai\\JAGAN")
source_path = PureWindowsPath("D:\\")
file_name = "custom.css"

shutil.copyfile(source_path + file_name, dest_path + file_name)
inp = input("Enter ");
print(inp)

