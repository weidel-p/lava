from abc import ABC, abstractmethod

from lava.magma.core.model.model import AbstractProcessModel
from lava.magma.core.process.patch import AbstractPatch


class AbstractPatchImpl(ABC):

    def __init__(self,
                 patch: AbstractPatch,
                 builder,
                 proc_model: AbstractProcessModel):
        self.patch = patch
        self.builder = builder
        self.proc_model = proc_model

    @abstractmethod
    def register(self):
        pass

