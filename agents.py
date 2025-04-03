from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools


# from crewai.tools import WebsiteSearchTool


# web_search_tool = WebsiteSearchTool()

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py



from crewai_tools import SerperDevTool, \
                         ScrapeWebsiteTool, \
                         WebsiteSearchTool

crew_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/introduction"
)


task_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/concepts/tasks"
)
docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)
tool_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/concepts/tools"
)

agent_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/concepts/agents"
)


agent_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/concepts/agents"
)
class CrewGeneratorAgents:
    



    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")
        # self.tool = WebsiteSearchTool(website='https://docs.crewai.com/concepts/tools')

    def goal_breaker_agent(self):
        return Agent(
            role="Goal Breaker Agent",
            backstory=dedent(f"""An expert manager with decades of experience as an AI engineer,
             specializing in setting tasks for crew AI agents. Based on my understanding of crew ai and tasks, 
             I take a specified goal and systematically break it down into a hierarchical structure 
             of smaller, actionable tasks that feeds into the bigger picture.
             """
            ),
            goal=dedent(f"""Create a task list to achieve [Goal]. 
            Each task should have a unique name and 
            be a necessary step to accomplish the goal"""),

            tools=[crew_scrape_tool, task_scrape_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
             
        )

    def task_assigning_agent(self):
        return Agent(
            role="Task Assigning Agent",
            backstory=dedent(f"""Highly accomplished crew AI developer  You work at crewAI (https://crewai.com) and 
                             are now working with your team and seasoned project manager with extensive experience in strategic planning, task optimization, and resource allocation.
            Proven track record of successfully leading cross-functional teams and assigning tasks to maximize productivity and efficiency."""),
            goal=dedent(f"""Map crew AI agents to the provided task list, defining each agent's responsibility, goal, and motivational context. Provide a concise agent profile, 
            including their professional history, relevant skills, and expertise, 
            to facilitate effective task execution."""),
            tools=[agent_scrape_tool, docs_scrape_tool, crew_scrape_tool, task_scrape_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
             
        )


    
    def tool_assigning_agent(self):
        return Agent(
            role="Tool Assigning Agent",
            backstory=dedent(f"""As an expert manager You work at crewAI (https://crewai.com) and 
                             are now working with your team and crew AI developer with years of experience, I will assign the most suitable tools to each agent, ensuring they have the necessary resources to achieve their goals. I will utilize my expertise to pair each agent with the optimal tools, considering their unique strengths, task requirements, and desired outcomes."""),
            goal=dedent(f"""Allocate the necessary tools to each agent search the internet for crewai tools for to understand how to assign tools, 
            ensuring they have the required resources to complete their assigned tasks. Specify the tools needed for each agent to execute their task, 
            example calculators, web scrapers,
             statistical analysis software,."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
           
            # tools=[web_search_tool],
            tools=[tool_scrape_tool]

        )
    


    def tool_building_agent(self):
        return Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)


