import os
from datetime import datetime
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_API_KEY"))


# Function to create a new journal entry
def create_journal_entry(database_id, title):
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Name": {"title": [{"text": {"content": title}}]},
            # Add other properties here if needed
        },
        # You can add additional content to the page here
    )


# Get current date for the journal title
today = datetime.now().strftime("%Y-%m-%d")
journal_title = f"Journal Entry - {today}"

# Create a new journal entry
create_journal_entry(os.getenv("JOURNAL_VIEW_ID"), journal_title)
