# Todo 
- Include a Rust server with sync and aysnc writes to sqlite database. 
- Include fastapi in server comparison 
- See how many requests it take to break each API (flask ~50), catch exception and write number from while loop
- Make charts with altair for write speeds. 

# Async write rates
A python library for saving and tumbling timestamps 

`hashtag.py` contains a dictionary, timestamps. The items in timestamps are lists of timestamps, where the names define a user defined hashtag category. 

# With straight sqlite3
- About 11,000 rows/s can be written if one c.commit() is call made after all inserts. Otherwise, about 200 rows/s.

# With async sqlite3
- Aysnc writes rates are about 180 rows/s which is on par with regular writes! 
- with uvloops speeds are faster than straight sql calls, ~220 rows/s.
- using uvloop.install() doesn't seem to have an impact on rates. 

# uvloop
uvloop seems to be slightly faster, but needs to be repeatadly tested. 
- write a function to run 1000 requests 10 tens and calculate the average, save results to a dict. 
- running the requests with access_log = False seems speed things up a bit, probably because Sanic doesn't need to print to std out. 

# aiohttp
- Is the fastest implementation so far! It's faster than the native sqlite python code. 
- However, it has some subtleties. For instance it requires a session when making requests, which is easily accomplished with a context manager.

# flask 
- Break with multiple requests >50. 


# TLDR 
- If you have to go through an API than definitely take advantage of asynchronous calls. However, for local writes it may not be necessary to add complexity to a code base just to eek out a couple of hundred rows per second...unless you really need the speed, then GO Fast. 

