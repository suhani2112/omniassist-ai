from backend.tools.tool_registry import ToolRegistry


class AgentExecutor:

    def __init__(self):
        self.registry = ToolRegistry()


    def execute(self, plan):

        tool_name = plan.get("tool")

        # No tool required
        if not tool_name:
            return None


        # Get tool from registry
        tool = self.registry.get_tool(tool_name)


        # Tool not available
        if not tool:
            return f"Tool '{tool_name}' not found"


        # Execute tool
        return tool.run(
            plan.get("input", "")
        )   