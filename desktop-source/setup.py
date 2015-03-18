from distutils.core import setup
import py2exe

setup(
    windows=[{"script": "sha256app.py"}],
    options={"py2exe": {"includes": ["PySide", "os", "json", "hashlib"]}}
)