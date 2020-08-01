import json
data='{"var1":"nitesh", "var2":56}'
parsed=json.loads(data)
print(parsed)
print(type(parsed))
print(parsed['var1'])

data2={"channel_name":"python",
       "cars" : ['bmw' , 'ausi a8', 'ferrari'],
       "fridge" : ('roti', 'chawal'),
       "isbad" : False}

jscomp=json.dump(data2)
print(jscomp)

#Task=What is sort_keys parameters in dump


#Task - 1 json.load
