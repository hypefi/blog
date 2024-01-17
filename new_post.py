from datetime import datetime

# Ask the user for the title and tags
title = input("Enter the title of the post: ")
tags = input("Enter the tags for the post (comma separated): ")

# Format the title to be URL friendly
formatted_title = title.lower().replace(" ", "-")

# Get the current date
date = datetime.now().strftime("%Y-%m-%d")

# Create the filename
filename = f"_drafts/{date}-{formatted_title}.markdown"

# Format the tags to be list friendly
formatted_tags = ' '.join(['[' + tag + ']' for tag in tags.split(',')])

# Create the content
content = f"""---
layout: post
title: {title}
tags: {formatted_tags}
---
"""

# Write the content to the file
with open(filename, 'w') as f:
    f.write(content)
