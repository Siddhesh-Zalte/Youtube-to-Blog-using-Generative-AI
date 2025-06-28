from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

research_task=Task(
    description=("Identify the video{topic}"
    "Get detailed information about the video from the channel"
    ),
    expected_output=("A coprehensive 3 pragarphs long report based on the {topic}video from the channel"
    ),
    agents=[blog_researcher],
    tools=[yt_tool]
)

write_task=Task(
    description=("get the info from the youtube channel on the topic{topic}"
    ),
    expected_output="Summarize the information from the youtube channel video on the {topic} and ceate a blog post",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)
                     
