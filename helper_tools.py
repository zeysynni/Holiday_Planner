# helper_tools.py
from datetime import datetime
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import StructuredTool
from serpapi import GoogleSearch

from config import (
    SERPAPI_KEY,
    PUSHOVER_TOKEN,
    PUSHOVER_USER,
    PUSHOVER_URL,
    SANDBOX_DIR,
    DEFAULT_CURRENCY,
)
from utils.request_utils import send_post_request


# === Tool: Flight Search ===
def search_flights(from_city: str, to_city: str, departure_date: str, return_date: str) -> dict:
    """Search for flights between two airports using SerpAPI."""
    params = {
        "engine": "google_flights",
        "departure_id": from_city,
        "arrival_id": to_city,
        "outbound_date": departure_date,
        "return_date": return_date,
        "currency": DEFAULT_CURRENCY,
        "api_key": SERPAPI_KEY,
    }

    search = GoogleSearch(params)
    return search.get_dict()


tool_flight_search = StructuredTool.from_function(
    name="search_for_flights",
    func=search_flights,
    description=f"""
    Use this tool to search for available flights between two airports.

    Inputs:
    - `from_city` (str): IATA code of the departure airport (e.g., "STR" for Stuttgart).
    - `to_city` (str): IATA code of the destination airport (e.g., "LHR" for London Heathrow).
    - `departure_date` (str): Date of outbound flight (YYYY-MM-DD).
    - `return_date` (str): Date of return flight (YYYY-MM-DD).

    Notes:
    - Use IATA codes, not city names.
    - Ask for clarification if needed.
    - Validate that departure date is not in the past.

    Current date: {datetime.now().strftime('%Y-%m-%d (%A)')}
    """
)

# === Tool: Push Notification ===
def push_notification(text: str):
    """Send a push notification using Pushover API."""
    data = {"token": PUSHOVER_TOKEN, "user": PUSHOVER_USER, "message": text}
    send_post_request(PUSHOVER_URL, data)
    return "push notification sent successfully"

tool_push = Tool(
    name="send_push_notification",
    func=push_notification,
    description="Send a push notification to the user.",
)

# === Tool: Wikipedia Search ===
wikipedia = WikipediaAPIWrapper()
tool_wikipedia = WikipediaQueryRun(api_wrapper=wikipedia)

# === Tool: Google Search ===
serper = GoogleSerperAPIWrapper()
tool_search = Tool(
    name="google_search",
    func=serper.run,
    description="Use this tool for performing online web searches."
)

# === Tool: File Management ===
def get_file_tools():
    toolkit = FileManagementToolkit(root_dir=SANDBOX_DIR)
    return toolkit.get_tools()

# === Tool: Python REPL ===
python_repl_tool = PythonREPLTool()

# === Combine all tools ===
async def init_tools():
    """Initialize and return all tools for the assistant."""
    file_tools = get_file_tools()
    return file_tools + [
        tool_flight_search,
        tool_push,
        tool_search,
        python_repl_tool,
        tool_wikipedia,
    ]

