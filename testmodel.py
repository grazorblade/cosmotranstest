#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.append('/home/graham/Documents/CosmoTransitions')
sys.path.append('/home/graham/Documents/CosmoTransitions/cosmoTransitions')
sys.path.append('/home/graham/Documents/CosmoTransitions/test')
print sys.path

# run testModel1 from CosmoTransitions
import testModel1
m = testModel1.model1()
m.findAllTransitions()
