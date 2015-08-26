# cosmotranstest

Python scripts to test [Cosmo Transitions](https://github.com/clwainwright/CosmoTransitions).

Ensure you have a clone of Cosmo Transitions and this repository:

```
[root]
    CosmoTransitions/
    ├── cosmoTransitions
    ├── doc
    └── test
    cosmotranstest/
```

## linux image

This was tested on [Linux Mint 17.2 “Rafaela” Xfce](http://blog.linuxmint.com/?p=2889)

## set path

Set the paths so Python knows where the code is

```
# replace [root] with your root path location
PYTHONPATH=[root]/CosmoTransitions/cosmoTransitions:[root]/cosmotranstest/
```

For example I have `[root]` path is `/home/graham/Documents/`. Under that directory I
have the `CosmoTransitions` and `cosmotranstest` directories.

## test model

From the `cosmotranstest/` directory call

```
python testmodel.py
```

## test full tunneling plot

```
python testplots.py
```
