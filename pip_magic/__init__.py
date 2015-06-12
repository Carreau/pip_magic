"""
import this in ipython and use pip magically without ! and correct version !
"""

__version__ ='0.2.1'


from IPython.core.magic import register_line_magic
import pip as _pip

try:
    @register_line_magic
    def pip(line):
        args = [s for s in line.split(' ') if s]
        _pip.main(args)
except Exception:
    pass # alow flit to import and get version number

# We delete these to avoid name conflicts for automagic to work
