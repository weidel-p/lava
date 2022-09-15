from lava.magma.core.model.py.model import PyLoihiProcessModel
from lava.magma.core.model.py.ports import PyOutPort
from lava.magma.core.model.py.type import LavaPyType
import numpy as np

class NeuronModel(PyLoihiProcessModel):

    def __init__(self, proc_params: dict) -> None:
        super().__init__(proc_params)

        self._shape = self.proc_params["shape"]
        self._enable_learning = self.proc_params["enable_learning"]
        self._update_traces = self.proc_params['update_traces']


class NeuronModelFixed(NeuronModel):
    # Learning Ports
    s_out_bap: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, bool, precision=1)
    s_out_y2: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, np.int32, precision=7)
    s_out_y3: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, np.int32, precision=7)

    def __init__(self, proc_params: dict) -> None:
         super().__init__(proc_params)

    def run_spk(self):
        if self._enable_learning and self._update_traces is not None:
            y2, y3 = self._update_traces(self)
            self.s_out_y2.send(y2)
            self.s_out_y3.send(y3)


class NeuronModelFloat(NeuronModel):

    # Learning Ports
    s_out_bap: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, bool)
    s_out_y2: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, float)
    s_out_y3: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, float)

    def __init__(self, proc_params: dict) -> None:
        super().__init__(proc_params)

    def run_spk(self):
        if self._enable_learning:
            if self._update_traces is not None:
                y2, y3 = self._update_traces(self)
                self.s_out_y2.send(y2)
                self.s_out_y3.send(y3)
            else:
                self.s_out_y2.send(np.array([0]))
                self.s_out_y3.send(np.array([0]))



