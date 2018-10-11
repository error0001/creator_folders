import os

def CreateStrProj():
  print("Give a name of project: ")
  inNameProj = input()
  try:
    if not os.path.exists('./' + inNameProj + '/'):
      os.makedirs(inNameProj)
    os.chdir(inNameProj)
    # Create folders
    os.makedirs('_poject')
    os.makedirs('_documentation')
    os.makedirs('_cs_structs')
    os.makedirs('_uml_structs')
    os.makedirs('_addons_soft')
    os.makedirs('_other')
  except OSError:
    print('Error: Creating folders of project. ' + inNameProj)

if __name__ == '__main__':
  CreateStrProj()


#walk in the directory, for future
#*********************************
#from_dir = input()  # get dir
#print("***************************************")
#for crtgs in os.walk(from_dir):  # Generate a cortages
#  print (crtgs)                  # and print whole
#print("***************************************")