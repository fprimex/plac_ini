# Installation

Installation follows the same steps as [plac](https://pypi.python.org/pypi/plac/). If you are lazy, just perform

```
$ pip install plac_ini
```

which will install the module on your system (and possibly argparse
too, if it is not already installed).

If you prefer to install the full distribution from source, including
the documentation, download the [tarball](http://pypi.python.org/pypi/plac_ini), unpack it and run

```
$ python setup.py install
```

in the main directory, possibly as superuser.

# Testing

Still working on tests!

# Documentation

The plac\_ini module adds configuration file (INI) parsing to the plac module.
The plac module is a tool for building command line interfaces using Python.

As with plac, the approach is to define a function in Python, annotate it using
either the plac.annotations dectorator or Python 3's native annotations, then
use plac\_ini.call (rather than plac.call) to call your function. With
plac\_ini.call, you will also provide the path to a configuration file that can
be used to set options and optionally a default INI section.

Example:

```
#!/usr/bin/env python

import os
import plac
import plac_ini

# (help, kind, abbrev, type, choices, metavar)
@plac.annotations(
    user_name=('Git username', 'option', 'u', None, None, 'USER_NAME'),
    user_email=('Git email', 'option', 'e', None, None, 'EMAIL'),
    color_ui=('UI Color', 'option', 'c', None, None, 'COLOR_UI'),
    push_default=('push_default', 'option', 'p', None, None, 'PUSH')
    )
def main(user_name=None,
         user_email=None,
         color_ui='auto',
         push_default='upstream'
    ):
    print("user_name {}".format(user_name))
    print("user_email {}".format(user_email))
    print("color_ui {}".format(color_ui))
    print("push_default {}".format(push_default))

if __name__ == '__main__':
    gitconfig = os.path.join(os.path.expanduser('~'), '.gitconfig')
    plac_ini.call(main, config=gitconfig)
```

My ~/.gitconfig looks like the following.

```
[user]
    name = Brent Woodruff
    email = brent@fprimex.com
[push]
    default = simple
```

So here are the results of a few different kinds of runs.

```
$./gitstuff -h
usage: gitstuff [-h] [-u USER_NAME] [-e EMAIL] [-c COLOR_UI] [-p PUSH]

optional arguments:
  -h, --help            show this help message and exit
  -u USER_NAME, --user-name USER_NAME
                        Git username
  -e EMAIL, --user-email EMAIL
                        Git email
  -c COLOR_UI, --color-ui COLOR_UI
                        UI Color
  -p PUSH, --push-default PUSH
                        push_default
```

```
$./gitstuff 
user_name Brent Woodruff
user_email brent@fprimex.com
color_ui auto
push_default simple
```

```
$./gitstuff -c true --push-default nothing
user_name Brent Woodruff
user_email brent@fprimex.com
color_ui true
push_default nothing
```

A few items of note:

* Defaults are specified in the function specification.
* Defaults are overridden by entries in the config file.
* Defaults and config file entries are overridden by command line options.
* The config file will parse options into 'section\_item' style names. A default section can be given which will be parsed back without the 'section\_'.
* If the config file is not found, plac\_ini.call will try to proceed with defaults and command line options.
* Only items that are specified by the function definition will be provided. That is, if a config file has many more sections and items, they will not be provided in the argument list.
* All things that plac can do, hopefully plac\_ini works with, so reference that documentation and send me bug reports. I am going to work on tests.
* Speaking of plac features, plac\_ini supports the conversion of types as specified in the annotations. Boolean types are a special case, as those are converted using `ConfigParser._convert_to_boolean`, which supports things like `1`, `yes`, `true`, and more for True / False values.
* The code is written to be compatible with plac.call. If 'config=FILEPATH' is not given, then plac\_ini.call just calls plac.call. I've done this so the code would be easier to include in plac proper in the future.

The source code is hosted on Github.

https://github.com/fprimex/plac\_ini


