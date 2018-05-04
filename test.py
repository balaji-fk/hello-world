a=['chennai-tn','madurai,tn']


for x in a:
	if '-' in x:
		print x.split('-')
	elif  "," in x:
		print x.split(',')