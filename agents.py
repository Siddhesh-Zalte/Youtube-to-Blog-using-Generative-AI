from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
load_dotenv()
from crewai import Agent
from langchain.chat_models import ChatOpenAI  # or appropriate import

# Define your LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.7)
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

blog_researcher=Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevant video content for the topic from topic {topic} from the youtube channel",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in Understanding youtube Videos"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

blog_writer=Agent(
     role="Blog Writer ",
    goal="Narrate compelliong tech stories about video {topic} from YT channel",
    verboe=True,
    memory=True,
    backstory=(
        "With a flare for simplyfying topics, youi craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    allow_delegation=True
)
