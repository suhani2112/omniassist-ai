from backend.services.llm_service import LLMService
from backend.agent.planner import AgentPlanner
from backend.agent.executor import AgentExecutor
from backend.tools.tool_registry import ToolRegistry


# ----------------------------
# Load all available tools
# ----------------------------
registry = ToolRegistry()

print("\nLoaded Tools:")
for tool in registry.get_available_tools():
    print(tool)


# ----------------------------
# Create shared LLM
# ----------------------------
llm = LLMService()


# ----------------------------
# Create planner & executor
# ----------------------------
planner = AgentPlanner(llm)
executor = AgentExecutor()


# ----------------------------
# Test Query
# ----------------------------
query = "what is machine learning"

plan = planner.decide(query)

print("\nPLAN:")
print(plan)

result = executor.execute(plan)

print("\nRESULT:")
print(result)