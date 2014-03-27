try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os.path

def require(*modules):
    """Check if the given modules are already available; if not add them to
    the dependency list."""
    deplist = []
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            deplist.append(module)
    return deplist

def getversion(fname):
    "Get the __version__ without importing plac"
    for line in open(fname):
        if line.startswith('__version__'):
            return eval(line[13:])

if __name__ == '__main__':
    setup(name='plac_ini',
          version=getversion(
            os.path.join(os.path.dirname(__file__), 'plac_ini.py')),
          description=('Adds configuration file support to the smartest '
                       'command line arguments parser in the world'),
          long_description=open('README.txt').read(),
          author='Brent Woodruff',
          author_email='brent@fprimex.com',
          url='https://github.com/fprimex/plac_ini',
          license="BSD License",
          py_modules = ['plac_ini'],
          scripts = [],
          install_requires=require('plac'),
          use_2to3=True,
          keywords="command line arguments parser",
          platforms=["All"],
          classifiers=['Development Status :: 3 - Alpha',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: BSD License',
                       'Natural Language :: English',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3',
                       'Topic :: Software Development :: Libraries',
                       'Topic :: Utilities'],
          zip_safe=False)
