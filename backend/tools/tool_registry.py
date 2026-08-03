import importlib
import inspect
import pkgutil

from backend.tools.base_tool import BaseTool
from backend.tools.pdf.tool import PDFTool
import backend.tools


class ToolRegistry:

    def __init__(self):

        self.tools = {}

        self.load_tools()


    def load_tools(self):

        package = backend.tools

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):

            # Skip infrastructure files
            if module_name in [
                "base_tool",
                "tool_registry",
                "__init__"
            ]:
                continue

            module = importlib.import_module(
                f"backend.tools.{module_name}"
            )

            for _, obj in inspect.getmembers(module):

                if (
                    inspect.isclass(obj)
                    and issubclass(obj, BaseTool)
                    and obj is not BaseTool
                ):

                    tool = obj()

                    self.tools[
                        tool.name
                    ] = tool


    def get_tool(self, name):

        return self.tools.get(name)


    def get_available_tools(self):

        return [
            tool.get_metadata()
            for tool in self.tools.values()
        ]
    def list_tools(self):
        return self.get_available_tools()