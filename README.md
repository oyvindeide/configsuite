# Config Suite #

[![Build Status](https://travis-ci.org/equinor/configsuite.svg?branch=master)](https://travis-ci.org/equinor/configsuite)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

## Introduction ##
_Config Suite_ is the result of recognizing the complexity of software configuration, both from a user and developer perspective. And our main goal is to be transparent about this complexity. In particular we aim at providing the user with confirmation when a valid configuration is given, concrete assistance when the configuration is not valid and up-to-date documentation to assist in this work. For a developer we aim at providing a suite that will handle configuration validity with multiple sources of data in a seamless manner, completely remove the burden of special casing and validity checking and automatically generate documentation that is up to date. We also believe that dealing with the complexity of formally verifying a configuration early in development leads to a better design of your configuration.

## Features ##
- Validate configurations.
- Provide an extensive list of errors when applicable.
- Output a single immutable configuration object where all values are provided.
- Support for multiple data sources, yielding the possibility of default values as well as user and workspace configurations on top of the current configuration.
- Generating documentation that adheres to the technical requirements.

## Examples ##

#### A first glance ####
For now we will just assume that we have a schema that describes the expected
input. Informally say that we have a very simple configuration where one can
specify ones name and hobby, i.e:

```yaml
name: Espen Askeladd
hobby: collecting stuff
```

You can then instantiate a suite as follows:

```python
import configsuite

# ... fetch input_config

suite = configsuite.ConfigSuite(input_config, schema)
```

You can now check whether data provided in `input_config` is valid by accessing
`suite.valid`.

```python
if suite.valid:
    print("Congratulations! The config is valid.")
else:
    print("Sorry, the configuration is invalid.")
```

Now, given that the configuration is indeed valid you would probably like to
access the data. This can be done via the `ConfigSuite` member named
`snapshot`. Hence, we could change our example above to:

```python
if suite.valid:
    msg = "Congratulations {name}! The config is valid. Go {hobby}."
    print(msg.format(name=suite.snapshot.name, hobby=suite.snapshot.hobby))
else:
    print("Sorry, the configuration is invalid.")
```

And if feed the example configuration above the output would be:

```
Congratulations Espen Askelad! The config is valid. Go collect stuff.
```

However, if we changed the value of `name` to `13` (or even worse `[My, name, is kind, of odd]`) we would expect the configuration to be invalid and hence that the output would be `Sorry, the configuration is invalid`. And as useful as this is it would be even better to gain more detailed information about the errors.

```
print(suite.errors)
(InvalidTypeError(msg=Is x a string is false on input 13, key_path=('hobby',), layer=None),)
```

```python
if suite.valid:
    msg = "Congratulations {name}! The config is valid. Go {hobby}."
    print(msg.format(name=suite.snapshot.name, hobby=suite.snapshot.hobby))
else:
    print("Sorry, the configuration is invalid.")
```


#### A first schema ####
TODO

```python
schema = {
    MK.Type: types.NamedDict,
    MK.Content: {
        "name": {MK.Type: types.String},
        "hobby": {MK.Type: types.String},
    }
}
```

#### Required values ####

#### Lists ####
TODO

#### Named Dicts ####
TODO

#### Dicts ####
TODO

#### Readable ####
TODO

#### Documentation generation ####
TODO

#### Element validators ####
TODO

#### Creating your own types ####
TODO

#### Layers ####
TODO

## Future ##
Have a look at the epics and issues in the _GitHub_ (repository)[https://github.com/equinor/configsuite/issues].

## Installation ##
The simplest way to fetch the newest version of _Config Suite_ is via [PyPI](https://pypi.python.org/pypi/configsuite/).

`pip install configsuite`

## Developer guidelines ##
Contributions to _Config Suite_ is very much welcome! Bug reports, feature requests and improvements to the documentation or code alike. However, if you are planning a bigger chunk of work or to introduce a concept, initiating a discussion in an issue is encouraged.

#### Running the tests ####
The tests can be executed with `python setup.py test`. Note that the code formatting tests will only be executed with Python `3.6` or higher.

#### Code formatting ####
The entire code base is formatted with [black](https://black.readthedocs.io/en/stable/).

#### Pull request expectations ####
We expect a well-written explanation for smaller PR's and a reference to an issue for larger contributions. In addition, we expect the tests to pass on all commits and the commit messages to be written in imperative style. For more on commit messages read [this](https://chris.beams.io/posts/git-commit/).
