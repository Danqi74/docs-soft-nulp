from abc import ABC, abstractmethod


class IPresentation(ABC):

    @abstractmethod
    def run(self):
        pass