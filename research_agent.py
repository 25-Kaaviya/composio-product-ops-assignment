import os
import pandas as pd
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

search = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

apps = pd.read_csv("apps.csv")

results = []

# Test with first 5 apps
for _, app in apps.iterrows():
    print(f"Researching: {app['App']}")

    docs = search.search(
        query=f"{app['App']} official developer API documentation authentication OAuth API key REST GraphQL MCP",
        max_results=3
    )

    results.append({
        "App": app["App"],
        "Category": app["Category"],
        "Website": app["Website"],
        "Search Results": str(docs)
    })

pd.DataFrame(results).to_csv("results.csv", index=False)

print("Done! results.csv created.")