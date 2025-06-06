from agentpro.tools.base_tool import Tool
from agentpro.model import create_model  # Replace call_model with create_model

class SummarizerTool(Tool):
    name: str = "summarizer"
    description: str = "Summarizes academic text using GPT-4o"
    action_type: str = "summarizer"
    input_format: str = "A string of academic text to summarize"

    def run(self, text: str) -> str:
        # Shorten input if needed
        trimmed_text = text[:6000]  # roughly 1,500–2,000 tokens

        prompt = (
            "You are an expert academic assistant. Read the following paper content and generate a concise, well-structured summary. "
            "Focus on the main objectives, methods, and findings:\n\n"
            f"{trimmed_text}"
        )

        try:
            return create_model(prompt)
        except Exception as e:
            return f"Error during summarization: {str(e)}"
