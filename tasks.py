# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent


class CustomTasks:
    
    def break_goal(self, agent, goal):
        return Task(
        description=dedent(
                f""" 
            ***Task***: Break goal into smaller manageable tasks***
          
            ***description***:Given a clear goal divide the goal into smaller manageable tasks 
               that crew ai agents can execute. 
               Use this variable: {goal}
               """
            ),
            
        expected_output=
          "The expected output of the task should be a list of task whereby each 
              """item in the list is an object that has task name, description and expected output e.g
            Task_Name* = Select City
            Description=dedent(f"""

               """ Analyze and select the best city for the trip based 
                on specific criteria such as weather patterns, seasonal
                events, and travel costs. This task involves comparing
                multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and
                overall travel expenses. 
                
                Your final answer must be a detailed
                report on the chosen city, and everything you found out
                about it, including the actual flight costs, weather 
                forecast and attractions. """
       
            """),
            expected_output="Detailed report on the chosen city including flight costs, weather forecast, and attractions" """

            ,
            agent=agent,
        )






    def assign_task(self, agent, tasks):
        return Task(
         
            description=dedent(
                f""" 
            ***Task***: Map crew AI agents to the provided task list***
          
            ***description***:Given the task list Map crew AI agents to the provided task list, defining each agent's responsibility, goal, and motivational context. Provide a concise agent profile, 
            including their professional history, relevant skills, and expertise

             Use this variable: {tasks}
            """
            ),
            
            expected_output=
            """The expected output of the task should be an array of 
            crewAi agent responsible for each of the task on the list
            an agent should like this.

            Agent(
                role='Local Expert at this city',
                goal='Provide the BEST insights about the selected city',
                backstory= A knowledgeable local guide with extensive information
                about the city, it's attractions and customs,)
            """
         ,
            agent=agent,
        )



    def assign_tool(self, agent, agentsList):
        return Task(
                  description=dedent(
                f""" 
            ***Task***: Assign necessary tools to agents***
          
            ***description***:Given the crewai agent list Allocate the necessary tools to each agent, 
            ensuring they have the required resources to complete their assigned tasks. 
            Specify the tools needed for each agent to execute their task

             Use this variable: {agentsList}
            """
            
            
            ),
               expected_output=
            """The expected output of the task should be an array of 
            crewAi agent responsible for each of the task on the list with 
            tools they might need to accomplish the task
            an agent should like this.

            Agent(
                role='Local Expert at this city',
                goal='Provide the BEST insights about the selected city',
                backstory= A knowledgeable local guide with extensive information
                about the city, it's attractions and customs,
                tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                ],
            """,
            agent=agent,
        )
 
