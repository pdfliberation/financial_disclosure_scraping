# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import zipfile
import StringIO
import csv

# <markdowncell>

# 0. Download list of doc ids from clerk.house.gov

# <codecell>

listing_urls = "http://clerk.house.gov/public_disc/financial-pdfs/{year}FD.ZIP"

# <markdowncell>

# even though forms change over time, we're going to get all of them.  NB, though

# <codecell>

for year in years_available:
    r = requests.get(listing_urls.format(year=year)

# <codecell>

years_available = xrange(2008,2014)

# <codecell>

r = requests.get(listing_urls.format(year=2013))
z = zipfile.ZipFile(StringIO.StringIO(r.content))

# <codecell>

z.namelist()

# <codecell>

listing = z.extract('2013FD.txt')

# <codecell>

my_dialect = csv.Sniffer().sniff(open(listing).read())

# <codecell>

listing_reader = csv.DictReader(open(listing), dialect=my_dialect)

# <codecell>

listing_reader.fieldnames

# <codecell>

DocIDs = [row['DocID'] for row in listing_reader]

# <codecell>

DocIDs

# <codecell>

doc_urls = "http://clerk.house.gov/public_disc/financial-pdfs/2013/{DocID}.pdf"

# <codecell>

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

# <codecell>

pfd_filenames = []

for DocID in DocIDs:
    pfd_filenames.append(download_file(doc_urls.format(DocID=DocID)))

# <codecell>

pfd_filenames

# <codecell>


