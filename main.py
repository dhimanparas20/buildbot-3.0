import os
import time
import sync
import up 
import octavi

clear()
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("------------------==================================================---------------------")
print("------------------= WELCOME TO COMPILING SCRIPT BY MST PRODUCTIONS =---------------------")
print("------------------==================================================---------------------")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------BY: Paras Dhiman --")
print()

time.sleep(1)

print ("------------------------------------------------")
print ("            Choose your Choice                  ")
print ("------------------------------------------------")
print ("0: Save Github credentials ")
print ("1: sync Rom Repo")
print ("2: sync Device Trees ")
print ("3: Compile rom ")
print ("4: Upload rom to GD ")
print ("press any other key to exit :") 
print("==================================================")
inp = int(input("Enter your choice :"))
print("==================================================")
print()
clear()
time.sleep(1)

#0- saving credentials
if inp == 0 :
  print("-----------------------------------------------")
  os.system("git config --global credential.helper store")
  print()
  print("-----------------------------------------------")
  print(" work done now exiting.... ")
  time.sleep(3)
  exit()

#1- sync the rom source  
elif inp == 1 :
  sync.disp()  ''' displays the rom choices '''
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of new directory : ")
  print("==================================================")
  print()
  sync.repo(choice,rdir_name)
  print()
  print("----------Work Done , Exiting ---------------")
  time.sleep(2)
  clear()
  exit()
 
#2- sync the device trees 
elif inp == 2 :
  print("==================================================") 
  branch = input("Enter exact name of github branch : ")
  rdir_name = input("enter the name of directory : ")
  print("==================================================")  
  print()
  sync.tree(branch,rdir_name)
  print()
  print("----------Work Done , Exiting ---------------")
  time.sleep(2)
  clear()
  exit()

#3- compiling the rom 
elif inp == 3 :
  sync.opt()
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of directory : ")
  print("==================================================")
  if choice == 1 :
    os.system("cd && cd buildbot && cp cherish.sh /home/mst/"+ rdir_name )
    '''os.system("cd && cd " + rdir_name + " && bash cherish.sh ")'''
  elif choice == 2 :
    os.system("cd && cd buildbot && cp cr.sh /home/mst/"+ rdir_name )
    '''os.system("cd && cd " + rdir_name + " && bash cr.sh ")'''
  elif choice == 3 :
    os.system("cd && cd buildbot && cp dot.sh /home/mst/"+ rdir_name )
    '''os.system("cd && cd " + rdir_name + " && bash dot.sh ")'''
  elif choice == 4 :
    os.system("cd && cd buildbot && cp legion.sh /home/mst/"+ rdir_name )
    '''os.system("cd && cd " + rdir_name + " && bash legion.sh ")'''
  elif choice == 5 :
    inp = input("Do you wante to sync Private repo ? type (Y/N) : ") 
    if inp == "y" or inp == "Y" :
      octavi.fix(rdir_name)
    elif inp == "n"  or inp == "N" :
      os.system("cd && cd buildbot && cp octavi.sh /home/mst/"+ rdir_name )
      '''os.system("cd && cd " + rdir_name + " && bash octavi.sh ")'''
    else :
     time.sleep(1)
     print("invalid input")
     time.sleep(1)
     print("exiting")
     time.sleep(2)
     exit()
      

#4- uploading the rom     
elif inp == 4 :
  print ("------------------------------------------------")
  print ("            Choose rom Choice to upload          ")
  print ("------------------------------------------------")
  print ("1: Gdrive")
  print ("2: Source Forge ")
  print("==================================================")
  cho = int(input("enter where you want to upload : "))
  print("==================================================")
  print()
  clear()
  if cho == 1 :
    print("-----------------------------------------------------------------------------")
    rdir_name = input("enter the name of working directory : ")
    print("-----------------------------------------------------------------------------")
    print()
    os.system("cd && cd "+rdir_name+" cd o*/t*/p*/X* && ls ")
    print()
    print("-----------------------------------------------------------------------------")
    name = input("Enter the name of file: ")
    clear()
    up.gd(rdir_name,name)
    
  elif cho == 2 :
    print("-----------------------------------------------------------------------------")
    rdir_name = input("enter the name of working directory : ")
    print("-----------------------------------------------------------------------------")
    print()
    os.system("cd && cd "+rdir_name+" cd o*/t*/p*/X* && ls ")
    print()
    print("-----------------------------------------------------------------------------")
    name = input("Enter the name of file: ")
    proj = input("Enter the name of project and location: ")
    print("-----------------------------------------------------------------------------")
    clear
    up.sf(rdir_name,name,proj)