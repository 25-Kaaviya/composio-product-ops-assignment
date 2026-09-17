import pandas as pd
import ast

df = pd.read_csv("results.csv")

rows = []

for _, row in df.iterrows():
    search_data = ast.literal_eval(row["Search Results"])

    first_result = ""
    evidence = ""

    if search_data.get("results"):
        first_result = search_data["results"][0].get("content", "")
        evidence = search_data["results"][0].get("url", "")

    rows.append({
        "App": row["App"],
        "Category": row["Category"],
        "Website": row["Website"],
        "Evidence": evidence,
        "Doc Snippet": first_result[:1000]
    })

pd.DataFrame(rows).to_csv("structured_results.csv", index=False)

print("structured_results.csv created.")