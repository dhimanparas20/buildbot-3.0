import time
import os
import sync 

def run(choice,rdir_name,inp):
  sync.opt()
  print("==================================================")
  if choice == 1 :
    return(
      os.system("cd && cd buildbot && cp cherish.sh /home/mst/"+ rdir_name ),
      os.system("cd && cd " + rdir_name + "chmod +x cherish.sh && bash cherish.sh "))
  elif choice == 2 :
    return(
      os.system("cd && cd buildbot && cp cr.sh /home/mst/"+ rdir_name ),
      os.system("cd && cd " + rdir_name + "chmod +x cr.sh && bash cr.sh "))
  elif choice == 3 :
    return(
      os.system("cd && cd buildbot && cp dot.sh /home/mst/"+ rdir_name ),
      os.system("cd && cd " + rdir_name + "chmod +x dot.sh && bash dot.sh "))
  elif choice == 4 :
    if inp == "y" or inp == "Y" :
      return(
        octavi.fix(rdir_name),
        os.system("cd && cd buildbot && cp octavi.sh /home/mst/"+ rdir_name ),
        os.system("cd && cd " + rdir_name + "chmod +x octavi.sh && bash octavi.sh "))
    elif inp == "n"  or inp == "N" :
      return(
        os.system("cd && cd buildbot && cp octavi.sh /home/mst/"+ rdir_name ),
        os.system("cd && cd " + rdir_name + "chmod +x octavi.sh && bash octavi.sh "))
    else :
      return(
        time.sleep(1),
        print("invalid input"),
        time.sleep(1),
        print("exiting"),
        time.sleep(2),
        exit())
  else():
    return(
      time.sleep(1),
      print("invalid input"),
      time.sleep(1),
      print("exiting"),
      time.sleep(2),
      exit())
    