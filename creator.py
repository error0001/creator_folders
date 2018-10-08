import os

def CreateStrProj(inNameProj):
  print("Give a name of project: ")
  try:
    if not os.path.exists(inNameProj):
      os.makedirs(inNameProj)
  except OSError:
    print('Error: Creating folders of project. ' + inNameProj)

if __name__ == '__main__':
  CreateStrProj('./data/')