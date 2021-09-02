import pickle
import json
f = open("system_data.json","r")
data = json.load(f)
mydb = open('system_data_dbase.pkl','wb')
pickle.dump(data,mydb)
pickle_file = open('system_data_dbase.pkl','rb')
new_data = pickle.load(pickle_file)
