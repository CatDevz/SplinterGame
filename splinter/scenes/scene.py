from abc import ABC, abstractmethod


_registered = []

class AbstractScene(ABC):
    @classmethod
    def __init_subclass__(cls, is_abstract=False, runtime_scene=False, **kwargs):
        super().__init_subclass__(**kwargs)
        if not is_abstract:
            _registered.append(cls)

    @abstractmethod
    def draw(self, window):
        raise NotImplementedError('subclasses must override draw')

    @abstractmethod
    def input(self, key):
        raise NotImplementedError('subclasses must override input')