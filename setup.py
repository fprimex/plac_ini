from setuptools import setup
import os.path
import sys

should_2to3 = sys.version >= '3'

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

if __name__ == '__main__':
    setup(name='plac_ini',
          version='0.9.2',
          description=('Adds configuration file support to plac'),
          long_description=open('README.txt').read(),
          author='Brent Woodruff',
          author_email='brent@fprimex.com',
          url='https://github.com/fprimex/plac_ini',
          license="BSD License",
          py_modules = ['plac_ini'],
          scripts = [],
          install_requires=['plac'],
          use_2to3=should_2to3,
          keywords="command line arguments ini file parser",
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

