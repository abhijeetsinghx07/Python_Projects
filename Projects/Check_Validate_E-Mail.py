import os

# Replace these values with your own information
github_username = "abhijeetsinghx07"
github_repo_name = "Python_Projects"
image_filename = "Projects/pro_images/Email_valid.png"

# Change to the directory where the image is stored
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Use the git command to add the image to the repository
os.system(f"git add {image_filename}")

# Use the git command to commit the changes to the repository
os.system(f"git commit -m 'Add image {image_filename}'")

# Use the git command to push the changes to the remote repository
os.system("git push")


email=input("Enter your email id: ") 

#mailname213@gmail.com
#mailname213@gmail.in

k,j,d=0,0,0
if len(email)>=6:
     if email[0].isalpha():
         if  ("@" in email) & (email.count("@")==1):
             if (email[-3]==".") ^ (email[-4]=="."):
                 for i in email:
                     if i==i.isspace():
                         k=1
                     elif i.isalpha():
                         if i==i.upper():
                             j=1
                     elif i.isdigit():
                         continue
                     elif i=="_" or i=="." or i=="@":
                         continue
                     else:
                         d=1
             if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
             else:
                 print("Correct Email")
         else:
             print("Wrong Email 3")
     else:
         print("Wrong Email 2")
else:
     print("Wrong Email 1")
