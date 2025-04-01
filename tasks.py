# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent


class CrewTasks:
    
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
          """The expected output of the task should be a list of task whereby each 
              item in the list is an object that has task name, description and expected output e.g
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
            expected_output="Detailed report on the chosen city including flight costs, weather forecast, and attractions """

            ,
            agent=agent,
        )

    def assign_task(self, agent):
        return Task(
         
            description=dedent(
                f""" 
            ***Task***: Map crew AI agents to the provided task list***
          
            ***description***:Given the task list Map crew AI agents to the provided task list, defining each agent's responsibility, goal, and motivational context. Provide a concise agent profile, 
            including their professional history, relevant skills, and expertise

            
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

    def assign_tool(self, agent):

        return Task(
                  description=dedent(
                f""" 
            ***Task***: Assign necessary tools to agents***
          
            ***description***:Given the crewai agent list Allocate the necessary tools to each agent, 
            ensuring they have the required resources to complete their assigned tasks.search the internet for crewai tools for to understand how to assign tools
            Specify the tools needed for each agent to execute their task. the task should be soemething than a computer can execute. if a tool is not neccessary to execute
              the task leave it as blank, 

            
            """
            
            
            ),
               expected_output=
            """The expected output of the task should be an array of 
            crewAi agent responsible for each of the task on the list with 
            tools they might need to accomplish the task
            an agent should like this and it should also include a 
            detailed information on what you know about building crewai agents the logic. below is an example. 

            Agent(
                role='Local Expert at this city',
                goal='Provide the BEST insights about the selected city',
                backstory= A knowledgeable local guide with extensive information
                about the city, it's attractions and customs,
                tools=[
                SearchTools.search_internet: full detail description of the tool,
                BrowserTools.scrape_and_summarize_website: full detail description description of tool,
                ],
            """,
            agent=agent
         
        )
    
    def build_tool(self, agent):

        return Task(
                  description=dedent(
                f""" 
            ***Task***:  You will build tools using python***
          
            ***description***:Given the crewai agent list understand the 
              required tools for each and write the full python code

            """
            
            
            ),
               expected_output=
            """The expected output of the task should be an array of 
            crewAi agent responsible for each of the task on the list with 
            tools and the full python code for the tools example
            Agent(
                role='Local Expert at this city',
                goal='Provide the BEST insights about the selected city',
                backstory= A knowledgeable local guide with extensive information
                about the city, it's attractions and customs,
                tools=[
                SearchTools.search_internet: description of tool,
                BrowserTools.scrape_and_summarize_website:description of tool,
                ],
                SearchTools.search_internet:{
                   codeExplanation: details about the code
                   code: the full python code of the tools
                }


            """,
            agent=agent
         
        )
    
