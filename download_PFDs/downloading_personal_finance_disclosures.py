# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import zipfile
import StringIO
import csv
import os

# <codecell>

working_dir = os.getcwd()

# <codecell>

INFO_DIR = os.path.join(working_dir,'filing_info')
PDF_DIR = os.path.join(working_dir,'pdf_documents')
DOC_DIR = os.path.join(PDF_DIR,'PFD')

for d in [INFO_DIR, PDF_DIR, DOC_DIR]:
    if not os.path.exists(d):
        os.mkdir(d)

# <markdowncell>

# 0. Download list of doc ids from clerk.house.gov

# <codecell>

listing_urls = "http://clerk.house.gov/public_disc/financial-pdfs/{year}FD.ZIP"

# <markdowncell>

# even though forms change over time, we're going to get all of them.  NB, though

# <codecell>

for year in years_available:
    r = requests.get(listing_urls.format(year=year))
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extract('{year}FD.txt'.format(year=year), path=INFO_DIR)

# <codecell>

!tree filing_info

# <codecell>

doc_url = "http://clerk.house.gov/public_disc/financial-pdfs/{year}/{doc_id}.pdf"

def download_file(url, out_filename):
    # NOTE the stream=True parameter
    try:
        r = requests.get(url, stream=True)
        with open(out_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return out_filename
    except:
        sys.stderr.write('download error: {}\n'.format(url))
        raise

def read_info_file(info_file):
    my_dialect = csv.Sniffer().sniff(open(info_file).read())
    listing_reader = csv.DictReader(open(info_file), dialect=my_dialect)
    return listing_reader

def get_pdfs_for_year(info_year):
    #sys.stderr.write('starting {}\n'.format(info_year))
    info_file = os.path.join(INFO_DIR,'{}FD.txt'.format(info_year))
    docs_info = [row for row in read_info_file(info_file)]
    downloaded_files = []
    years = list(set([di['Year'] for di in docs_info]))
    for y in years:
        if not os.path.exists(os.path.join(DOC_DIR,str(y))):
            os.mkdir(os.path.join(DOC_DIR,str(y)))
    for doc_info in docs_info:
        #sys.stderr.write(doc_info['DocID']+'\n')
        _dir = os.path.join(DOC_DIR,str(y))
        out_filename = os.path.join(_dir, doc_info['DocID']+'.pdf')
        if not os.path.exists(out_filename):
            download_file(doc_url.format(year=doc_info['Year'], doc_id=doc_info['DocID']), out_filename)
            downloaded_files.append(out_filename)
    #sys.stderr.write('\nDone {}\n'.format(info_year))
    sys.stderr.write("{year} Finished\n".format(year=info_year))

# <codecell>

years_available = xrange(2008,2014)
for year in years_available:
    get_pdfs_for_year(year)

# <codecell>


