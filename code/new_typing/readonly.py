# readonly.py
from typing import ReadOnly, TypedDict

class PythonVersion(TypedDict):
    version: ReadOnly[str]

py313 = PythonVersion(version="3.13")
py313['version'] = "3.12"
print(py313['version'])
