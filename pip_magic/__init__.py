"""
import this in ipython and use pip magically without ! and correct version !
"""

__version__ ='0.2.3'


from IPython.core.magic import register_line_magic
import pip as _pip
import shlex

try:
    @register_line_magic
    def pip(line):
        args = [s for s in shlex.split(line) if s]
        _pip.main(args)
except Exception:
    pass # allow flit to import and get version number
