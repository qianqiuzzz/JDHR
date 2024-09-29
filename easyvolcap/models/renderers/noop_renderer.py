import jittor as jt
from jittor import nn
from typing import List
from easyvolcap.engine import RENDERERS
from easyvolcap.utils.base_utils import dotdict
from easyvolcap.utils.net_utils import VolumetricVideoModule


@RENDERERS.register_module()
class NoopRenderer(VolumetricVideoModule):  # should not contain optimizables
    def __init__(self,
                 network: nn.Module,
                 **kwargs,  # ignore other arguments
                 ):
        super().__init__(network)
        self.execute = self.render

    def render(self, rgb: jt.Var, occ: jt.Var, batch: dotdict):
        # raw: main renderable data
        # batch: other useful resources
        return None
