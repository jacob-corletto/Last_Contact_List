import json

class contacts:
  def __init__(self,*,filename):
    self.file = filename
    self.data = {}

    try:
      with open(self.file,'r') as f:
        self.data = json.load(f)
  
    except FileNotFoundError:
      print('file not found')

  def add_contact(self,*,id,first_name,last_name):
    if id in self.data:
      return ValueError

    else:
      self.data[id] = [first_name, last_name]

      self.data = dict(sorted(self.data.items(), key = lambda x: (x[1][0].lower(), x[1][1])))

      with open(self.file, "w") as outfile:
        json.dump(self.data, outfile)
        
    return self.data[id]

  def modify_contact(self,*,id,first_name,last_name):
    if id not in self.data:
      print('invalid number')
      return ValueError

    else:
      self.data[id] = [first_name,last_name]
      self.data = dict(sorted(self.data.items(), key = lambda x: (x[1][0].lower(), x[1][1])))

      with open(self.file, "w") as outfile:
        json.dump(self.data, outfile)

    return self.data[id]

  def delete_contact(self,*,id):
    if id not in self.data:
      print('invalid number')
      return ValueError

    else:
      deleted_value = self.data.pop(id)

      with open(self.file, "w") as outfile:
        json.dump(self.data, outfile)
      
      return deleted_value
      
      