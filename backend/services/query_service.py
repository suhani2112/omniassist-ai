from backend.services.llm_service import LLMService
from backend.agent.planner import AgentPlanner
from backend.agent.executor import AgentExecutor


class QueryService:

    def __init__(self):

        self.llm = LLMService()

        self.planner = AgentPlanner(
            self.llm
        )

        self.executor = AgentExecutor()


    def process_query(self, query: str):

        # Step 1: Ask planner
        plan = self.planner.decide(query)


        tool_name = plan.get("tool")


        # Step 2: Tool execution
        if tool_name:

            tool_result = self.executor.execute(plan)


            final_prompt = f"""
You are OmniAssistAI, an intelligent AI assistant.

A tool has already solved the user's request.

User query:
{query}

Tool result:
{tool_result}

Give only the final answer.
Keep it short and clear.
Do not mention tools.
Do not mention internal processing.
"""


            response = self.llm.generate_response(
                final_prompt
            )


            return {
                "query": query,
                "response": response
            }



        # Step 3: Normal LLM response

        response = self.llm.generate_response(
            query
        )


        return {
            "query": query,
            "response": response
        }