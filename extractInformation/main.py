# Author: vivek
# Purpose: write json to file

import json
from extractTitle import *
from extractAuthors import *
from extractYear import *
from extractReferences import *

# data is a dictionary which is like a json file
data={}

# add title to data
data.update({'title':extractTitle()})

# add authors details to data
data.update({'authors':extractAuthors()})

# add year
data.update({'year':extractYear()})

# write data to json file
fp=open('file.txt', 'w')
json.dump(data, fp)
fp.close()