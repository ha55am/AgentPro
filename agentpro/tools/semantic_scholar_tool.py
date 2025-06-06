import requests
from agentpro.tools.base_tool import Tool

class SemanticScholarTool(Tool):
    name: str = "semantic_scholar"
    description: str = "Searches academic papers using Semantic Scholar"
    action_type: str = "semantic_scholar"
    input_format: str = "A search query string for academic papers"

    def run(self, query: str) -> str:
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            "query": query,
            "limit": 5,
            "fields": "title,abstract,url,authors"
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"

        data = response.json().get("data", [])
        if not data:
            return "No results found."

        result = ""
        for i, paper in enumerate(data, 1):
            authors = ", ".join([a['name'] for a in paper.get("authors", [])])
            result += (
                f"Paper {i}:\n"
                f"Title: {paper.get('title')}\n"
                f"Authors: {authors}\n"
                f"Abstract: {paper.get('abstract')}\n"
                f"Link: {paper.get('url')}\n\n"
            )
        return result
