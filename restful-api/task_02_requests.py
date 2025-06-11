#!/usr/bin/python3
"""
Module: task_02_requests
- Uses the requests library to interact with the JSONPlaceholder API.
- Prints post titles and saves posts to a CSV file.
"""

import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetches all posts from the API and prints their titles."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """Fetches all posts and saves them to a CSV file called posts.csv"""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        # Extract required fields: id, title, body
        simplified_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Save to CSV
        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(simplified_posts)
    else:
        print("Failed to fetch posts")
