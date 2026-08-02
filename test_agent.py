from backend.services.llm_service import LLMService
from backend.agent.planner import AgentPlanner
from backend.agent.executor import AgentExecutor


# Create shared LLM
llm = LLMService()


# Pass LLM to planner
planner = AgentPlanner(llm)


executor = AgentExecutor()


query = "calculate 25 * 50"


plan = planner.decide(query)

print("PLAN:")
print(plan)


result = executor.execute(plan)

print("\nRESULT:")
print(result)