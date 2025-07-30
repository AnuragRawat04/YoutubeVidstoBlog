from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from task import research_task,write_task

crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

## Start the task execution process
result=crew.kickoff(inputs={'topic':'Sidemen LAst to Fall Asleep Challenge'})
print(result)