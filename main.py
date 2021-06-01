import feedparser
from operator import itemgetter
import time
import httpx
from io import BytesIO
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Modify to Suit - List of Allowed Origins
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Used to Test for Slow Feeds Locally
check_feed_performance = False

feedlist = []
parsedfeeds = []
posts = []
list_of_post_dicts = []

with open("feeds.txt", "r") as feed_file:
    feed_lines = feed_file.readlines()
    for line in feed_lines:
        feedlist.append(line.strip())

async def get_feed(feedurl):
    if check_feed_performance:
        start_request = time.perf_counter()
    try:
        async with httpx.AsyncClient() as client:
            feed_response = await client.get(feedurl, timeout=5.0)
            content = BytesIO(feed_response.content)
            feed = feedparser.parse(content)
            parsedfeeds.append(feed)
        if check_feed_performance:
            end_request = time.perf_counter()
            print(f"{end_request - start_request} - {feedurl}")
    except Exception:
        pass

async def process_feeds():
    parsedfeeds.clear()
    posts.clear()
    list_of_post_dicts.clear()

    feed_responses = await asyncio.gather(*map(get_feed, feedlist))
    for parsedfeed in parsedfeeds:
        for entries in parsedfeed.entries:
            posts.append((entries.title, entries.published_parsed, entries.description))

    # Fresher the Better
    posts.sort(key=itemgetter(1))
    posts.reverse()

    # Convert the Whole Mess to JSON
    for post in posts:
        post_time = time.strftime('%H:%M:%S %d-%m-%Y ', post[1])

        post_dict = {
            'time': post_time,
            'title': post[0],
            'link': post[2],
            'description': post[3]
            }

        list_of_post_dicts.append(post_dict)

    return list_of_post_dicts

# Only Using a Single Route - Can Be Freely Changed
@app.get("/rss")
async def rss():
    json = await process_feeds()

    return JSONResponse(content=json)
