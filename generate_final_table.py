import pandas as pd

df = pd.read_csv("structured_results.csv").fillna("")

def detect_auth(text):
    text = text.lower()
    if "oauth" in text:
        return "OAuth2"
    if "api key" in text or "apikey" in text:
        return "API Key"
    if "bearer" in text or "token" in text:
        return "Bearer Token"
    if "basic auth" in text:
        return "Basic Auth"
    return "Unknown"

def detect_api(text):
    text = text.lower()
    if "graphql" in text and "rest" in text:
        return "REST + GraphQL"
    if "graphql" in text:
        return "GraphQL"
    if "rest" in text:
        return "REST"
    return "Unknown"

def detect_mcp(text):
    return "Yes" if "mcp" in text.lower() else "No"

rows = []

for row in df.itertuples(index=False):   # Faster than iterrows()
    snippet = str(row._4)   # Doc Snippet column

    rows.append({
        "App": row.App,
        "Category": row.Category,
        "Description": "From official developer docs",
        "Auth Method": detect_auth(snippet),
        "Self Serve / Gated": "Needs verification",
        "API Surface": detect_api(snippet),
        "API Breadth": "Needs verification",
        "Existing MCP": detect_mcp(snippet),
        "Buildability Verdict": "Likely Buildable",
        "Main Blocker": "Manual verification required",
        "Evidence": row.Evidence
    })

pd.DataFrame(rows).to_csv("final_results.csv", index=False)

print("final_results.csv created successfully!")