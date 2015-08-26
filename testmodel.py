#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.append('/home/frank/dev/CosmoTransitions')
sys.path.append('/home/frank/dev/CosmoTransitions/cosmoTransitions')
sys.path.append('/home/frank/dev/CosmoTransitions/test')
print sys.path

# run testModel1 from CosmoTransitions
import testModel1
m = testModel1.model1()
m.findAllTransitions()
