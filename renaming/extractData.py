# Author: vivek
# Purpose: write json to file

import json

# data is a dictionary which is like a json file
data={}
def extractTitle(paper=''):
	return "This is dummy title"

def extractAuthors(paper=''):
	email='abc@gmail.com'
	name='abc'
	return [{'email':email,'name':name},{'email':email,'name':name}]

def extractYear(paper=''):
	return 2000
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