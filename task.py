from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# 🔹 Research Task
research_task = Task(
    description=(
        "Identify the YouTube video for the topic '{topic}'. "
        "Get detailed information and insights about the video from the channel."
    ),
    expected_output="A comprehensive, 3-paragraph-long report based on the '{topic}' video content.",
    tools=[yt_tool],
    agent=blog_researcher
)

# 🔹 Writing Task
write_task = Task(
    description=(
        "Use the researched information from the YouTube video on the topic '{topic}' "
        "to create a well-written blog post."
    ),
    expected_output="Summarize the content and craft an engaging blog post on the topic '{topic}'.",
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)
