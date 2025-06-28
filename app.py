from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

crew=Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    Process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,

)

#start with enhanced feedback

result=crew.kickoff(inputs={"topic":"Longest Sedan in India😱 | VCCCI Pune 2025"})
print(result)
