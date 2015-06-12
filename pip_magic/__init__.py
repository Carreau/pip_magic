"""
import this in ipython and use pip magically without ! and correct version !
"""

__version__ ='0.1'


from IPython.core.magic import register_line_magic
import pip.commands as c

try:
    @register_line_magic
    def pip(line):
        c.install.InstallCommand().main([line.strip('install').strip()])
except Exception:
    pass # alow flit to import and get version number

# We delete these to avoid name conflicts for automagic to work
