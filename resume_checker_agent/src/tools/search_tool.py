from langchain_community.tools import DuckDuckGoSearchResults
from crewai.tools import BaseTool
class DuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGoSearch"
    description: str = "Useful for search-based queries."
    search: DuckDuckGoSearchResults = DuckDuckGoSearchResults()

    def _run(self, query: str) -> str:
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"