'''
Created on Mar 7, 2011

@author: johnsalvatier
'''
import numpy as np 
import core

class MultiStep(object):
        
    def init(self, model):
        self.model = model
        self.var_mapping = core.VariableMapping(model.free_vars)
        self.chain_state = core.ChainState()
        self.evaluator = core.ChainEvaluation(self.chain_state, model)