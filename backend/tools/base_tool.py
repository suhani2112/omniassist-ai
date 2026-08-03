from abc import ABC, abstractmethod


class BaseTool(ABC):

    def __init__(self):

        self.name = ""

        self.description = ""

        self.category = ""

        self.version = "1.0"

        self.author = "OmniAssistAI"

        self.supported_inputs = []

        # NEW
        self.capabilities = []

    @abstractmethod
    def run(self, input_data):

        pass

    def get_metadata(self):

        return {

            "name": self.name,

            "description": self.description,

            "category": self.category,

            "version": self.version,

            "author": self.author,

            "supported_inputs": self.supported_inputs,

            "capabilities": self.capabilities
        }