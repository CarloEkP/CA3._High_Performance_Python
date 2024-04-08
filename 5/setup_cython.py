from distutils.core import setup
from Cython.Build import cythonize

filestocompile = ["Cython_version1.pyx", "Cython_version2.pyx", "Cython_version3.pyx", "Cython_version4.pyx"]
setup(ext_modules =cythonize(filestocompile))