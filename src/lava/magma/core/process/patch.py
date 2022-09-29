from abc import ABC, abstractmethod

from lava.magma.core.process.process import AbstractProcess


class AbstractPatch(ABC):

    @abstractmethod
    def register(self, process):
        pass

    def _register_in_ports(self,
                           process: AbstractProcess,
                           in_ports: dict):
        """Register all in ports to process"""

        for attr in in_ports.items():
            setattr(self, attr[0], attr[1])
        process._init_proc_member_obj(in_ports)
        process.in_ports.add_members(in_ports)

    def _register_out_ports(self,
                           process: AbstractProcess,
                           out_ports: dict):
        """Register all out ports to process"""

        for attr in out_ports.items():
            setattr(self, attr[0], attr[1])
        process._init_proc_member_obj(out_ports)
        process.out_ports.add_members(out_ports)

    def _register_vars(self,
                           process: AbstractProcess,
                           vars: dict):
        """Register all vars to process"""

        for attr in vars.items():
            setattr(self, attr[0], attr[1])
        process._init_proc_member_obj(vars)
        process.vars.add_members(vars)

