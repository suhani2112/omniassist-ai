import json

from backend.services.llm_service import LLMService
from backend.tools.tool_registry import ToolRegistry


class AgentPlanner:

    def __init__(self, llm: LLMService):

        self.llm = llm
        self.registry = ToolRegistry()

    def decide(self, query: str):

        # Dynamically load available tools
        available_tools = self.registry.get_available_tools()

        tool_catalog = []

        for tool in available_tools:

            tool_catalog.append(
                {
                    "name": tool["name"],
                    "description": tool["description"],
                    "capabilities": tool["capabilities"]
        }
    )

        prompt = f"""
You are the planning engine of OmniAssistAI.

Your responsibility is to understand the user's GOAL and decide whether one of the available tools should be used.

Available tools:

{json.dumps(tool_catalog, indent=2)}

Instructions:

1. Read the user's request carefully.
2. Identify the user's overall goal.
3. Decide whether one of the available tools can help.
4. If no tool is required, return tool as null.
5. Return ONLY valid JSON.
6. Do NOT include markdown or explanations.

Return exactly in this format:

{{
    "goal": "...",
    "tool": "...",
    "input": "...",
    "reason": "..."
}}

Examples:

User:
calculate 25*40

Response:
{{
    "goal": "Calculate a mathematical expression",
    "tool": "calculator",
    "input": "25*40",
    "reason": "Mathematical calculation is required."
}}

User:
What is machine learning?

Response:
{{
    "goal": "Learn about machine learning",
    "tool": null,
    "input": "What is machine learning?",
    "reason": "General knowledge question."
}}

User:

{query}
"""

        response = self.llm.generate_response(
            prompt,
            use_memory=False
        )

        try:

            response = self.llm.generate_response(
            prompt,
            use_memory=False
)

            print("\n========== RAW LLM RESPONSE ==========")
            print(response)
            print("======================================")

            plan = json.loads(response)

            # Ensure required keys exist
            return {
                "goal": plan.get("goal", ""),
                "tool": plan.get("tool"),
                "input": plan.get("input", query),
                "reason": plan.get("reason", "")
            }

        except Exception:

            return {
                "goal": "Answer the user's question",
                "tool": None,
                "input": query,
                "reason": "Planner could not generate a valid plan."
            }