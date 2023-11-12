# hug-bounter
Be the first to report the bug!

Hug Bounter provides you with easy access to latest bug bounty program data available on HackerOne, Bugcrowd, Intigriti, and YesWeHack. 

Interact with the database through a user-friendly crud interface to manually or automatically manage records.

Due to query rate limit restrictions on data.space, currently integrated with MongoDB.

<h2>Usage</h2>

1. Create a `.env` file in the root directory, and insert your MongoDB connection string:
``` 
CONNECTION_STRING=<INSERT_YOUR_CONNECTION_STRING_HERE>
```

2. Make sure your IP address is added into you MongoDB cluster under the `Network Access` tab.


<h2>Live</h2>

Test hug bounter live on streamlit cloud:
```
https://hug-bounter.streamlit.app/
```
 
<br>
Happy bounting ;-)
