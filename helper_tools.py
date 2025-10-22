#from playwright.async_api import async_playwright
#from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
import os
from datetime import datetime
import requests
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import StructuredTool

from serpapi import GoogleSearch


load_dotenv(override=True)
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"
serpapi_key = os.getenv('SERP_API_KEY')

# Flight search tool
def search_flights(from_city: str, to_city: str, departure_date: str, return_date: str) -> str:
    """Search for the best flight given the departure airport, arrival airport, departure date and return date."""
    params = {
        "engine": "google_flights",
        "departure_id": from_city,
        "arrival_id": to_city,
        "outbound_date": departure_date,
        "return_date": return_date,
        #"type": 2,
        "currency": "EUR",
        "api_key": serpapi_key
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
        - `departure_date` (str): Date of outbound flight in YYYY-MM-DD format.
        - `return_date` (str): Date of return flight in YYYY-MM-DD format.

        Behavior:
        - Always use IATA codes, not city names.
        - If the user provides only a city (e.g., "London"), ask which airport they mean.
        - If only one date is provided, ask whether it's a one-way or round trip.
        - Validate that `departure_date` is today or later.
        - Provide short summaries of flight options (e.g., airline, duration, price).

        For context, the current date is {datetime.now().strftime('%Y-%m-%d (%A)')}.
        """,
        )

# Push notification tool
def push(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})

tool_push = Tool(
        name="send_push_notification",
        func=push,
        description="useful for when you want to send a push notification"
    )

# Wikipedia tool
wikipedia = WikipediaAPIWrapper()
wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)

# Google search tool
serper = GoogleSerperAPIWrapper()
tool_search = Tool(
    name="search",
    func=serper.run,
    description="Use this tool when you want toget the results of an online web search"
    )

# File management tool
def get_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()

file_tools = get_file_tools()

# Python tool
python_repl = PythonREPLTool()

# Playwright tool
#async def playwright_tools():
#    playwright = await async_playwright().start()
#    browser = await playwright.chromium.launch(headless=True)
#    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
#    return toolkit.get_tools(), browser, playwright

# Set of other tools
async def other_tools():
    return file_tools + [tool_flight_search, tool_push, tool_search, python_repl, wiki_tool]