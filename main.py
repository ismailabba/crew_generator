import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI


from textwrap import dedent
from agents import CrewGeneratorAgents
from tasks import CrewTasks

from dotenv import load_dotenv


load_dotenv()


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CrewGenerator:
    def __init__(self, goal):
        self.goal= goal
        

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CrewGeneratorAgents()
        tasks = CrewTasks()

        # Define your custom agents and tasks here
        goal_breaker_agent= agents.goal_breaker_agent()
        task_assigning_agent = agents.task_assigning_agent()
        tool_assigning_agent = agents.tool_assigning_agent()
        # tool_building_agent = agents.tool_building_agent()

        # Custom tasks include agent name and variables as input
        break_goal = tasks.break_goal(
            goal_breaker_agent,
            self.goal
            
        )

        assign_task = tasks.assign_task(
            task_assigning_agent,
            
        )

        assign_tool = tasks.assign_tool(
            tool_assigning_agent,
            
        )

        
        # build_tool = tasks.build_tool(
        #     tool_building_agent,
            
        # )


        # Define your custom crew here
        crew = Crew(
            agents=[goal_breaker_agent, task_assigning_agent, tool_assigning_agent],
            tasks =[break_goal, assign_task, assign_tool],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    goal = input(dedent("""what is the goal of your crew: """))
    

    crew_generator = CrewGenerator(goal)
    result = crew_generator.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
