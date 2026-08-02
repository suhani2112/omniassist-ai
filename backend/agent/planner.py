import json

from backend.services.llm_service import LLMService
from backend.tools.tool_registry import ToolRegistry


class AgentPlanner:


    def __init__(self, llm: LLMService):

        self.llm = llm

        self.registry = ToolRegistry()



    def decide(self, query: str):


        # -----------------------------------
        # Step 1: Rule-based tool detection
        # -----------------------------------

        math_keywords = [
            "calculate",
            "add",
            "subtract",
            "multiply",
            "divide",
            "plus",
            "minus",
            "times",
            "product",
            "sum"
        ]


        query_lower = query.lower()


        if any(
            word in query_lower
            for word in math_keywords
        ):


            expression = query_lower


            remove_words = [
                "calculate",
                "what is",
                "find",
                "the answer of",
                "please",
                "solve"
            ]


            for word in remove_words:

                expression = expression.replace(
                    word,
                    ""
                )


            return {

                "tool": "calculator",

                "input": expression.strip()

            }



        # -----------------------------------
        # Step 2: LLM based planning
        # -----------------------------------


        available_tools = self.registry.list_tools()


        prompt = f"""
You are an AI agent planner.

Your job is to decide whether a tool is needed.

Available tools:

{available_tools}


Rules:

1. Use calculator only for mathematical calculations.
2. For normal questions, return tool as null.
3. Return ONLY valid JSON.
4. Do not add explanations.


User query:

{query}


Return one of these formats:


{{
    "tool": "calculator",
    "input": "mathematical expression"
}}


OR


{{
    "tool": null,
    "input": "{query}"
}}
"""


        response = self.llm.generate_response(
            prompt,
            use_memory=False
        )


        try:

            return json.loads(
                response
            )


        except Exception:


            return {

                "tool": None,

                "input": query

            }