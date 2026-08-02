import uuid

from backend.services.llm_service import LLMService
from backend.agent.planner import AgentPlanner
from backend.agent.executor import AgentExecutor
from backend.logs.logger_instance import logger



class QueryService:


    def __init__(self):

        self.llm = LLMService()

        self.planner = AgentPlanner(
            self.llm
        )

        self.executor = AgentExecutor()



    def process_query(self, query: str):


        # Unique ID for this request
        request_id = str(uuid.uuid4())


        # Step 1: Create plan
        plan = self.planner.decide(
            query
        )


        logger.log(
            request_id,
            "PLAN_CREATED",
            plan
        )



        # Step 2: Execute tool if required
        if plan.get("tool"):


            tool_response = self.executor.execute(
                plan
            )


            logger.log(
                request_id,
                "TOOL_EXECUTED",
                tool_response
            )



            # Tool failed
            if not tool_response["success"]:


                prompt = f"""
You are OmniAssistAI.

A tool failed while processing the user's request.

User query:
{query}

Error:
{tool_response["error"]}

Give a short helpful response.
"""


                response = self.llm.generate_response(
                    prompt
                )


                logger.log(
                    request_id,
                    "RESPONSE_GENERATED",
                    response
                )


                return {

                    "query": query,

                    "response": response

                }



            # Tool succeeded

            prompt = f"""
You are OmniAssistAI.

A tool has already solved the user's request.

User query:
{query}

Tool result:
{tool_response["result"]}

Give only the final answer.
Do not explain the calculation.
"""


            response = self.llm.generate_response(
                prompt
            )


            logger.log(
                request_id,
                "RESPONSE_GENERATED",
                response
            )


            return {

                "query": query,

                "response": response

            }



        # Step 3: Normal LLM response

        response = self.llm.generate_response(
            query
        )


        logger.log(
            request_id,
            "RESPONSE_GENERATED",
            response
        )


        return {

            "query": query,

            "response": response

        }