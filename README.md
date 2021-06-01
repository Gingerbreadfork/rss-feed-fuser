
# RSS Feed Fuser

Parse multiple RSS feeds, sort the contents by time of publish, and provide them for access via a simple API route in JSON format. RSS Feed Fuser is perfect for creating simple topical newsfeeds for your website.

The code is pretty simple, have some fun with it and make it your own!

## Acknowledgements

 - [Feedparser](https://github.com/kurtmckee/feedparser) - Makes it easy to wrangle RSS feeds
 - [FastAPI](https://github.com/tiangolo/fastapi) - Create awesome APIs fast with Python
 - [HTTPX](https://github.com/encode/httpx) - Great requests alternative check it out!
 - [Deta](https://www.deta.sh/) - The perfect way to test this project!

## Installation 

Use at least Python 3.7 to create virtual environment if desired, then install requirements like so...

```bash 
  pip3 install - r requirements.txt
```
Uvicorn makes local testing easy!
```bash
  pip3 install uvicorn
  uvicorn main:app
```
Don't forget to add your feeds to `feeds.txt` by adding just one per line, use the full URL.
[Learn how to Deploy Deta Micros and Test RSS Feed Fuser Yourself!](https://docs.deta.sh/docs/micros/getting_started)

## Like the Repo?

If you like this repo drop a star and let me know on Twitter! [@gingerbreadfork](https://twitter.com/gingerbreadfork)

