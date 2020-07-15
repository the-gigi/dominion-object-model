# Dominion object model

[
![PyPI](https://img.shields.io/pypi/v/dominion-object-model.svg)
![PyPI](https://img.shields.io/github/license/the-gigi/dominion-object-model.svg)
](https://pypi.org/project/dominion-object-model/)


This package contains two abstract base classes for implementing players 
and client libraries for the [dominion](https://github.com/the-gigi/dominion) project.

You can implement a GUI client for humans to play the game or an AI computer
player.

# Usage

A dominion player must implement the Player interface. The dominion game engine
will keep a reference to the player object and call its methods at the right time.

```
class Player(metaclass=ABCMeta):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def respond(self, action, *args):
        pass

    @abstractmethod
    def on_game_event(self, event):
        pass

    @abstractmethod
    def on_state_change(self, state):
        pass
```

A client library will implement the GameClient interface and a reference
to it will be passed to concrete player implementations. When the concrete
player who implements the Player interface receives the play() command 
from the game engine it will invoke various GameClient methods until
it finally calls done() and their turn ends.

```
class GameClient(metaclass=ABCMeta):
    @abstractmethod
    def play_action_card(self, card_type: str):
        pass

    @abstractmethod
    def buy(self, card_type: str):
        pass

    @abstractmethod
    def done(self):
        pass
```

# Examples

The dominion project itself contains several [computer players](https://github.com/the-gigi/dominion/tree/master/computer_players).

The [dominion-pygame](https://github.com/Bloblblobl/dominion-pygame) project is an implementation of a GUI client that lets humans play against each other and or bots.


# Build and publish

This section is for the Dominion developers. 
If you just want to implement a player or a client library you can stop reading.


## Pre-requisites

- Install [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win)
- Install [poetry](https://python-poetry.org/docs/#installation)

Create a Python 3.8.2 environment

```
$ pyenv install 3.8.2
$ pyenv local
$ poetry init
$ poetry env use 3.8.2
$ poetry install
```


## Building the package

Here is the command to build the package:

```
(🐙)/dominion-object-model
$ poetry run python setup.py bdist_wheel
``` 

The result is tar-gzipped file in the dist subdirectory:

```
(🐙)/dominion-object-model
$ ls dist
dominion_object_model-1.0.1-py3-none-any.whl
```

Save the following to ~/.pypirc

```
[distutils]
index-servers=
    pypi
    pypitest

[pypitest]
repository = https://test.pypi.org/legacy/
username = <your user name>

[pypi]
repository = https://pypi.org/legacy/
username = <your user name>
```

Next, we can upload the package using twine to PyPI.

```
(🐙)/dominion/dominion/object_model/
$ poetry run twine upload -p <redacted> dist/*.whl

Uploading distributions to https://upload.pypi.org/legacy/
Uploading dominion_object_model-1.0.2-py3-none-any.whl
100%|██████████████████████████████| 10.2k/10.2k [00:01<00:00, 7.20kB/s]

View at:
https://pypi.org/project/dominion-object-model/1.0.2/
```
