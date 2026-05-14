import argparse
import requests

def download(url,loc_fname):
    if loc_fname is None:
        loc_fname=url.split('/')[-1]
    #If srtream==true than parametrs below
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(loc_fname,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return loc_fname

parser=argparse.ArgumentParser()
# TO add command line utality 
parser.add_argument('url',help='url of the file to download')
# - optional argument ka lia 
parser.add_argument('-o','--output',help='Name of the file none',default=None)

# Parse the argument
args=parser.parse_args()

# Use argument in my code
print(args.url)
print(args.output)
download(args.url,args.output)

