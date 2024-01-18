import os
from datetime import datetime, timedelta
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_API_KEY"))


# Function to search the database and find upcoming due dates
def find_upcoming_due_dates(database_id, days_ahead=3):
    now = datetime.now()
    upcoming_date = now + timedelta(days=days_ahead)
    formatted_date = upcoming_date.strftime("%Y-%m-%d")

    try:
        response = notion.databases.query(
            **{
                "database_id": database_id,
                "filter": {
                    "and": [
                        {
                            "property": "Due date",
                            "date": {"on_or_before": formatted_date},
                        }
                    ]
                },
            }
        )

        tasks = response.get("results", [])
        for task in tasks:
            due_date = task["properties"]["Due date"]["date"]["start"]
            task_name = task["properties"]["Name"]["title"][0]["plain_text"]
            print(f"Task '{task_name}' is due by {due_date}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'your_database_id' with your actual database ID
find_upcoming_due_dates(os.getenv("SCHOOL_VIEW_ID"))
