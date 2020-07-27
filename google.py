import sys
import webbrowser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("query", help="keyword to be googled ; enter URL if using exact search (-e flag)")
parser.add_argument("-e","--exact", help="search for an exact URL", action="store_true")
args = parser.parse_args()
if args.exact:
    print("exact search is enabled...")
    print(f"RUNNING EXACT SEARCH FOR: {args.query}")
    webbrowser.open(args.query)
elif args.exact != True:
    print("exact search is disabled...")
    print(f"RUNNING SEARCH FOR: {args.query}")
    url = args.query
    url = url.replace(" ", "+")
    webbrowser.open("https://www.google.com/search?q={}&oq={}&aqs=chrome..69i57j46j0l6.2572j0j7&sourceid=chrome&ie=UTF-8".format(url, url))
    