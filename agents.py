from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CrewGeneratorAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def goal_breaker_agent(self):
        return Agent(
            role="Goal Breaker Agent",
            backstory=dedent(f"""An expert manager with decades of experience as an AI engineer,
             specializing in setting tasks for crew AI agents, 
             I take a specified goal and systematically break it down into a hierarchical structure 
             of smaller, actionable tasks.
             """
            ),
            goal=dedent(f"""Create a task list to achieve [Goal]. 
            Each task should have a unique name and 
            be a necessary step to accomplish the goal"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def task_assigning_agent(self):
        return Agent(
            role="Task Assigning Agent",
            backstory=dedent(f"""Highly accomplished crew AI developer and seasoned project manager with extensive experience in strategic planning, task optimization, and resource allocation.
            Proven track record of successfully leading cross-functional teams and assigning tasks to maximize productivity and efficiency."""),
            goal=dedent(f"""Map crew AI agents to the provided task list, defining each agent's responsibility, goal, and motivational context. Provide a concise agent profile, 
            including their professional history, relevant skills, and expertise, 
            to facilitate effective task execution."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )


    
    def tool_assigning_agent(self):
        return Agent(
            role="Tool Assigning Agent",
            backstory=dedent(f"""As an expert manager and crew AI developer with years of experience, I will assign the most suitable tools to each agent, ensuring they have the necessary resources to achieve their goals. I will utilize my expertise to pair each agent with the optimal tools, considering their unique strengths, task requirements, and desired outcomes."""),
            goal=dedent(f"""Allocate the necessary tools to each agent, 
            ensuring they have the required resources to complete their assigned tasks. Specify the tools needed for each agent to execute their task, 
            example calculators, web scrapers,
             statistical analysis software,."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

