"""
import this in ipython and use pip magically without ! and correct version !
"""

__version__ ='0.2'


from IPython.core.magic import register_line_magic
import pip.commands as c

try:
    @register_line_magic
    def pip(line):
        if line.startswith('install '):
            line=line[8:]
        c.install.InstallCommand().main([line.strip()])
except Exception:
    pass # alow flit to import and get version number

# We delete these to avoid name conflicts for automagic to work
