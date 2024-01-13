import praw
import requests

# Reddit API credentials
reddit_client_id = 'your_client_id'
reddit_client_secret = 'your_client_secret'
reddit_user_agent = 'your_user_agent'
subreddit_name = 'your_subreddit'

# Authenticate with Reddit API
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

# Get the subreddit
subreddit = reddit.subreddit(subreddit_name)

# Get the top 10 hot posts in the subreddit
posts = subreddit.hot(limit=10)

# Download links from each post
for post in posts:
    # Check if post has a URL
    if post.url:
        # Download the content
        response = requests.get(post.url)
        
        # Save the content to a file (you can modify this part based on your needs)
        with open(f"{post.id}_{post.title}.html", "w", encoding="utf-8") as file:
            file.write(response.text)

print("Downloaded links from the subreddit.")
