from contacts import *
import os

contact_list = contacts(filename='Friends.dat')

while True:
  print("*** TUFFY TITAN CONTACT MAIN MENU\n")
  print ('1. Add contact\n')
  print('2. Modify contact \n')
  print('3. Delete contact \n')
  print('4. Print contact list \n')
  print('5. Set contact filename \n')
  print('6. Exit the program \n')
  
  choice = int(input('Enter choice: '))

  if (choice ==1):
    id = input('enter number: ')
    first_name = input('enter first name: ')
    last_name = input('enter last name: ')
    
    contact_list.add_contact(id = id,first_name=first_name,last_name= last_name)

  elif (choice ==2):
    id = input('enter number: ')
    first_name = input('enter first name: ')
    last_name = input('enter last name: ')
    (contact_list.modify_contact(id=id,first_name=first_name,last_name=last_name))
    print(f'{contact_list.data[id][0]} {contact_list.data[id][1]}')
    

  elif (choice ==3):
    id = input('enter number: ')

    contact_list.delete_contact(id=id)

  elif (choice ==4):
    print('==================== CONTACT LIST ====================')
    print('Last Name            First Name         Phone')
    print('==================== ==================== ==========')
    for i in contact_list.data.keys():
      print(f'{contact_list.data[i][0]:21}{contact_list.data[i][1]:21}{i:20}')

  elif(choice ==5):
    newfile = input('enter file name: ')
    try :
      contact_list.file = newfile

      with open(contact_list.file,'r') as f:
          contact_list.data = json.load(f)
    except:
      print('file not found')

  elif (choice ==6):
    break

  else:
    print('invalid entry')