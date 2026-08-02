from backend.tools.calculator import CalculatorTool


class ToolRegistry:

    def __init__(self):

        self.tools = {}

        self.register_tool(
            CalculatorTool()
        )


    def register_tool(self, tool):

        self.tools[tool.name] = tool


    def get_tool(self, name):

        return self.tools.get(name)


    def list_tools(self):

        return {
            name: tool.description
            for name, tool in self.tools.items()
        }