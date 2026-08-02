from backend.tools.tool_registry import ToolRegistry


class AgentExecutor:


    def __init__(self):

        self.registry = ToolRegistry()



    def execute(self, plan):

        tool_name = plan.get("tool")

        tool_input = plan.get("input")


        # No tool required
        if not tool_name:

            return None



        try:

            tool = self.registry.get_tool(tool_name)


            if tool is None:

                return {
                    "success": False,
                    "error": f"Tool '{tool_name}' not found"
                }



            result = tool.run(
                tool_input
            )


            return {
                "success": True,
                "result": result
            }



        except Exception as e:


            return {
                "success": False,
                "error": str(e)
            }