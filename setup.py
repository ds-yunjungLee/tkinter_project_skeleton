from distutils.core import setup
import py2exe, sys, os

includes = [
	"encodings",
	"encodings.utf_8",
]

options = {	
	"compressed":1,
	"optimize":2,
	"dll_excludes":["OLEAUT32.dll", "USER32.dll", "IMM32.dll", "SHELL32.dll", "KERNEL32.dll", "COMDLG32.dll", "COMCTL32.dll", "ADVAPI32.dll", "WS2_32.dll", "GDI32.dll", "ole32.dll"],
	"includes":includes,
}

setup(
	options = {"py2exe":options},
	console = [{'script':"main.py"}],
	zipfile = None,
)