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

## set path

Set the paths so Python knows where the code is

```
# replace [root] with your root path location
PYTHONPATH=[root]/CosmoTransitions/cosmoTransitions:[root]/cosmotranstest/
```

For example I have `[root]` path is `/home/frank/dev/`. Under that directory I
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
