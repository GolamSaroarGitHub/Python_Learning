from collections import OrderedDict
import json
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
print(json.dumps(d))
#Outputs {"foo": 1, "bar": 2, "spam": 3, "grok": 4}


mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key in sorted(mydict.keys()):
    print ("%s: %s" % (key, mydict[key]))

