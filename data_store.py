import pickle
import json
f = open("system_data.json","rb")
data = json.load(f)
mydb = open('dbase.pkl','wb')
pickle.dump(data,mydb)
pickle_file = open('dbase.pkl','rb')
new_data = pickle.load(pickle_file)
