import requests
from bs4 import BeautifulSoup
from collections import deque
import time


def bfs_crawler(start_url, max_pages=10):
    visited = set()
    queue = deque([start_url])

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url not in visited:
            visited.add(url)
            print("Visited Site:", url)
            time.sleep(1)  # Be nice to the server

            # Find all links in the current page
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
            links = [a.get("href") for a in soup.find_all("a", href=True)]

            # Add the new links to the queue
            queue.extend(link for link in links if link.startswith("http"))

    return visited


if __name__ == "__main__":
    bfs_crawler("https://londonbuildingcontractors.co.uk", 15)
