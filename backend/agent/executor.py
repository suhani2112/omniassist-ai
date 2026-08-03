from backend.tools.tool_registry import ToolRegistry


class AgentExecutor:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, plan: dict):

        # ----------------------------
        # Extract plan information
        # ----------------------------
        goal = plan.get("goal", "")

        tool_name = plan.get("tool")

        tool_input = plan.get("input", "")

        reason = plan.get("reason", "")

        # ----------------------------
        # No tool required
        # ----------------------------
        if tool_name is None:

            return {
                "goal": goal,
                "tool": None,
                "reason": reason,
                "success": True,
                "result": None
            }

        # ----------------------------
        # Find tool
        # ----------------------------
        tool = self.registry.get_tool(tool_name)

        if tool is None:

            return {
                "goal": goal,
                "tool": tool_name,
                "reason": reason,
                "success": False,
                "error": f"Tool '{tool_name}' not found."
            }

        # ----------------------------
        # Execute tool
        # ----------------------------
        result = tool.run(tool_input)

        # ----------------------------
        # Tool execution failed
        # ----------------------------
        if not result.get("success"):

            return {
                "goal": goal,
                "tool": tool_name,
                "reason": reason,
                "success": False,
                "error": result.get("error")
            }

        # ----------------------------
        # Tool execution successful
        # ----------------------------
        return {
            "goal": goal,
            "tool": tool_name,
            "reason": reason,
            "success": True,
            "result": result.get("result")
        }