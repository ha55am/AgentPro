import os
from agentpro import ReactAgent
from agentpro import create_model
from agentpro.tools.semantic_scholar_tool import SemanticScholarTool
from agentpro.tools.summarizer_tool import SummarizerTool
from agentpro.tools.ppt_generator_tool import PowerPointGeneratorTool
from dotenv import load_dotenv

load_dotenv()

# Create a model with OpenAI
model = create_model(provider="openai", model_name="gpt-4o", api_key=os.getenv("OPENAI_API_KEY", None))

# Initialize tools
tools = [
    SemanticScholarTool(),
    SummarizerTool(),
    PowerPointGeneratorTool()
]

# Initialize agent
agent = ReactAgent(model=model, tools=tools)

# Prompt the user to enter a topic
topic = input("Enter the research topic you are interested in: ").strip()

# Build query dynamically
query = f"Find academic papers on {topic}. For each paper, summarize the abstract and generate a PowerPoint presentation slide with title, authors, and summary. The summary should be succinct."

# Run the query
response = agent.run(query)
