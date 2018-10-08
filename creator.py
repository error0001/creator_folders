import os

def CreateStrProj():
  print("Give a name of project: ")
  inNameProj = input()
  try:
    if not os.path.exists('./' + inNameProj + '/'):
      os.makedirs(inNameProj)
    os.chdir(inNameProj)
    os.makedirs('1_pojects')
    os.makedirs('2_documentation')
    os.makedirs('3_cs_structs')
    os.makedirs('4_uml_structs')
    os.makedirs('5_addons_soft')
    os.makedirs('6_other')
    os.chdir('1_pojects')
    os.makedirs('current')
    os.makedirs('old')
  except OSError:
    print('Error: Creating folders of project. ' + inNameProj)

if __name__ == '__main__':
  CreateStrProj()