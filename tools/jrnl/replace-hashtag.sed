# replace-hashtag.sed

# Example usage,
# sed -i.bak -f replace-hashtag.sed yourfile.txt

# Convert all hashtags (starting with #) to @ symbols
s/#\([a-zA-Z0-9_]\+\)/@\1/g

