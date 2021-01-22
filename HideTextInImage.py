#Created by Errikos Alexiou on the 22/01/21 program is free to use not to sell.

#importing os to use the os.system command to do commands that will execute the copy function
import os

#printing some ascii art
print ('''
  _     _     _     _            
 | |   (_)   | |   | |           
 | |__  _  __| | __| | ___ _ __  
 | '_ \| |/ _` |/ _` |/ _ \ '_ \ 
 | | | | | (_| | (_| |  __/ | | |
 |_| |_|_|\__,_|\__,_|\___|_| |_|
                                 
                                 
Created by Errikos Alexiou
''')


#info
print ('This code need to be ran in the same directory as the image or file that you are adding text to.')

#talking the users input
choice = input ('Would you like to use: \n[1] File (.txt)\n[2] Input Text\n')

#seeing what the user inputted
if choice == '1':
#inputs for the command
    IF = input ('What is the name of the file that is going to have text added? :')
    TF = input ('What is the name of the .txt file? (you must add .txt on the end) :')
    RF = input ('What would you like to name the result file? (must add the same extention as the file used ei. .mp4, .png) :')

#the command is being created and inputted as a var
    command = ('copy /b '+ IF + ' + ' + TF + ' ' + RF)
#command is being executed and this will mean completion unless an error.
    os.system(str(command))
    print ('file should have been created')

#seeing what the user inputted
elif choice == '2':
#inputs for the command
    IF = input ('What is the name of the file that is going to have text added? :')
    text = (str(input('What is the text that you want to put into this file? :')))
    RF = input ('What would you like to name the result file? (must add the same extention as the file used ei. .mp4, .png) :')

#created a file to use for the text
    with open('file.txt', 'w') as f:
        f.write('\n')
        f.write(text)
        f.close()

#the command being created and inputted as a var
    command = ('copy /b ' + IF + ' + ' + 'file.txt' + ' ' + RF)
#command is being executed and this will mean completion unless error.
    os.system(str(command))
    print ('file should have been created')
