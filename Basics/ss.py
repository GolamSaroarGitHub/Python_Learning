import shelve
#
shelfile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfile['cats'] = cats
shelfile.close()

shelfile = shelve.open('mydata')
print(shelfile['cats'])
shelfile.close()