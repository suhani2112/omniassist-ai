from backend.services.llm_service import LLMService
import json


class AgentPlanner:

    def __init__(self, llm: LLMService):

        self.llm = llm


    def decide(self, query: str):

        prompt = f"""
You are an AI agent planner.

Available tools:
1. calculator - for mathematical calculations

Decide if a tool is required.

User query:
{query}

Return ONLY JSON.

Format:

{{
    "tool": "calculator",
    "input": "mathematical expression"
}}

or

{{
    "tool": null,
    "input": "{query}"
}}
"""

        response = self.llm.generate_response(prompt)

        try:
            return json.loads(response)

        except Exception:
            return {
                "tool": None,
                "input": query
            }