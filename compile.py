from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("res", ["src/res/__init__.py"]),

    Extension("Runtime", ["src/RunTime.py"]),

    Extension("src", ["src/__init__.py"]),

    Extension("shell",  ["src/shell/index.py"]),
    Extension("shell", ["src/shell/__init__.py"]),

    Extension("shell.builder", ["src/shell/builder/base.py"]),
    Extension("shell.builder", ["src/shell/builder/tree.py"]),
    Extension("shell.builder", ["src/shell/builder/__init__.py"]),

    Extension("shell.astar", ["src/shell/astar/base.py"]),
    Extension("shell.astar", ["src/shell/astar/__init__.py"]),

    Extension("shell.cleaner", ["src/shell/cleaner/base.py"]),
    Extension("shell.cleaner", ["src/shell/cleaner/__init__.py"]),

    Extension("shell.djikstra", ["src/shell/djikstra/base.py"]),
    Extension("shell.djikstra", ["src/shell/djikstra/__init__.py"]),

    Extension("shell.getvar", ["src/shell/getvar/base.py"]),
    Extension("shell.getvar", ["src/shell/getvar/__init__.py"]),

    Extension("shell.graph", ["src/shell/graph/base.py"]),
    Extension("shell.graph", ["src/shell/graph/__init__.py"]),

    Extension("shell.json", ["src/shell/json/base.py"]),
    Extension("shell.json", ["src/shell/json/__init__.py"]),

    Extension("shell.set", ["src/shell/set/base.py"]),
    Extension("shell.set", ["src/shell/set/__init__.py"]),
    #   ... all your modules that need be compiled ...
]

setup(
    name = 'PathFinder',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)