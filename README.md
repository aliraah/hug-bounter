Changed name to "Hug Bounter"

Hug Bounter now stores data in its own database instead of retrieving info from source and parsing it on each request separately (unlike the legacy ver).

Integrated NoSQL database on deta.space

You can choose 1 of 4 available platforms, update records into the latest version and then retrieve from database. (Unfortuantely due to deta base query rate limits, some big queries from HackerOne or Bugcrowd might not be returned fully) 

You can also choose to drop the database and its records completely.

Usage:

Create a '.env' file in the same directory and put your data.space database key in there as below:
DETA_KEY=<INPUT YOUR DATA KEY HERE>

You should be ready to go now.

Happy hunting ;-)
