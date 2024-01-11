import random
from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()
notion_api_key = os.getenv("NOTION_API_KEY")
todo_view_id = os.getenv("TODO_VIEW_ID")

notion = Client(auth=notion_api_key)


def get_random_task(database_id, status):
    response = notion.databases.query(
        **{
            "database_id": database_id,
            "filter": {"property": "Status", "select": {"equals": status}},
        }
    )

    tasks = response.get("results", [])
    if tasks:
        return random.choice(tasks)
    else:
        return None


random_task = get_random_task(todo_view_id, "To Solve")
print(random_task)
