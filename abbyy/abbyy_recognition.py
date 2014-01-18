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
import local_settings as ls
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

settings.OutputFormat = 'xml'

# <codecell>

doc_id = doc_files[0].split('.')[0]

# <codecell>

task = processor.ProcessImage(os.path.join(doc_dir,doc_files[0]), settings)

# <codecell>

processor.GetTaskStatus(task).Status

# <codecell>

processor.DownloadResult(task,os.path.join(os.getcwd(),'output_{}.xml'.format(doc_id)))

# <codecell>

!head output_8209580.xml

# <codecell>

#z = zipfile.ZipFile(open('output.zip'))
#z.namelist()

# <codecell>

xml_file = open(os.path.join(os.getcwd(),'output_{}.xml'.format(doc_id)))
xd = xmltodict.parse(xml_file.read())

# <codecell>

xd.keys()

# <codecell>

print json.dumps(xd, indent=2)

# <codecell>


