# simplify pip from with IPython


```python
$ ipython2

In [1]: import pip_magic

In [2]: pip install pip_magic --upgrade
['pip_magic', '--upgrade']
You are using pip version 7.0.1, however version 7.0.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
Collecting pip-magic
  Downloading pip_magic-0.2.1-py2.py3-none-any.whl
Installing collected packages: pip-magic
  Found existing installation: pip-magic 0.2
    Uninstalling pip-magic-0.2:
      Successfully uninstalled pip-magic-0.2
Successfully installed pip-magic-0.2.1

In [3]: ## so recursive !
```

# Why ?

See [this twitter thread](https://twitter.com/amuellerml/status/932671416150962176), the package pre-date this thread but it's a good example:

Andreas Mueller

> Is there a good succinct guide to how to figure out which Python environment you're in and how to install stuff in the right environment that's suitable for beginners? cc @jakevdp (also if there's not Jake, can you write one ;)

Me:

> pip_magic: pypi.python.org/pypi/pip_magic use pip from within IPython/Notebook and it install in same env you're in.

AM:

> That looks great, but also lacks a write-up explaining the problem ;)

Me: 

> Can I embed your tweet in the readme ?

AM:

> Lol sure. Though it does expose me as the naysayer that I am ;) (and my tendency to complain on Twitter but not do anything productive lol)



