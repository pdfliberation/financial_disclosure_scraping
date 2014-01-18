# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
import os
import xmltodict
import zipfile
import StringIO
import json

import AbbyyOnlineSdk as abbyy
#import local_settings as ls
reload(ls)

# <codecell>

repo_dir = ls.repo_dir
doc_dir = os.path.join(repo_dir, 'download_PFDs')

# <codecell>

doc_files = os.listdir(doc_dir)

# <codecell>

processor = abbyy.AbbyyOnlineSdk()

# <codecell>

processor.ApplicationId = ls.app_id
processor.Password = ls.app_password

# <codecell>

settings = abbyy.ProcessingSettings()

# <codecell>

settings.Language

# <codecell>

settings.OutputFormat

# <codecell>

#settings.OutputFormat = 'xml'

# <codecell>

task = processor.ProcessImage(os.path.join(doc_dir,doc_files[0]), settings)

# <codecell>

processor.GetTaskStatus(task).Status

# <codecell>

processor.DownloadResult(task,os.path.join(os.getcwd(),'output.zip'))

# <codecell>

z = zipfile.ZipFile(open('output.zip'))

# <codecell>

z.namelist()

# <codecell>

z.extractall()

# <codecell>

xd = xmltodict.parse(z.read('word/document.xml'))

# <codecell>

xd.keys()

# <codecell>

doc_files[0]

# <codecell>

xd.keys()

# <codecell>

print json.dumps(xd, indent=2)

# <codecell>


