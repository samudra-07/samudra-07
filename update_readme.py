import json

# Load API response
with open("stats.json", "r") as f:
    data = json.load(f)

# Extract stats
if data["status"] == "OK":
    user_info = data["result"][0]
    handle = user_info["handle"]
    rating = user_info["rating"]
    max_rating = user_info["maxRating"]
    rank = user_info["rank"].capitalize()
    max_rank = user_info["maxRank"].capitalize()
    contribution = user_info["contribution"]
else:
    handle = "N/A"
    rating = "N/A"
    max_rating = "N/A"
    rank = "N/A"
    max_rank = "N/A"
    contribution = "N/A"

# Update README
readme_path = "README.md"
with open(readme_path, "r") as f:
    lines = f.readlines()

# Replace placeholders in README
for i, line in enumerate(lines):
    if "**Handle**:" in line:
        lines[i] = f"  **Handle**: [{handle}](https://codeforces.com/profile/{handle})\n"
    elif "**Rating**:" in line:
        lines[i] = f"  **Rating**: {rating} ({rank})\n"
    elif "**Max Rating**:" in line:
        lines[i] = f"  **Max Rating**: {max_rating} ({max_rank})\n"
    elif "**Contribution**:" in line:
        lines[i] = f"  **Contribution**: {contribution}\n"

# Write updated README
with open(readme_path, "w") as f:
    f.writelines(lines)
