# SecureTree-project
EPI-USE recruiting exercise.

Overview of project functionality.

This project was created for the purpose of creating and managing secureTree system that allows users to login, view and make changes to an entity hierarchy tree. 

All the files uploaded must be under the same folder in order for the project to work properly.

I used python as the language of programmming because it is user and programmer friendly in that it is easy to learn and understand, optimized for speed development, easy to formulate and is versitile(can be used as an embedded extension language or standalone). It is also good for frontend jobs which are a big part of majority of this project.I also used Notepad++ for coding because it is easy to install, uses less space and easy to work with. We also installed Anaconda for the functionality of some python modules. There is no need to install tkinter become it already comes installed with each windows 10.

For the security of the data I used encryption and pickle. Encryption changes the values of the "registered_user.json" into encrypted values by use of the key value that needs to be correct for decrytion and stores the encrypted values a a file "user_management.json" it creates . This method of ensuring security is good because it will not allow just anyone to access the data. Only users who- at their first try- write the correct credentials, filename and key can access and use the data which would then be decrypted. Pickle is a python module that is used for persistent data storage. Pickling serialises the data which makes it hard for anyone to understand the code as it is converted from python objects to strings thus making the security of data strong. Only data from a pickled file is used in this project.

For the user management system, a login gui appears to allow the user to enter credential and an additional instruction on the cmd allows the user to enter a filename: user_management.json and key:25. If user credentials, the filename and key are wrong an exception error will be displayed but the user can still change their credentials on the gui screen. If user credentials are correct on the second try but the filename is incorrect the exception will still show and the user can try to enter the correct credentials again. if this time the credentials and filename are correct but the key is not, a Denial access message will appear on cmd and the user can try to enter the correct key and filename again but even if the credentials are correct and filename and key are correct now, the user still is not granted access because of the first wrong attempt. So the user must close the gui and run the project again.If the credentials, filename and key are all correct the user will be granted access. Please follow the instruction on the welcome message that will appear when credentials are correct.

Architecture diagram of the project infrustructure
[code_infrustructure.drawio.pdf](https://github.com/Nompumelelo-Msiza/SecureTree-project/files/7101674/code_infrustructure.drawio.pdf)

Setup instruction
1. Install Notepad ++.

    Step1. Copy the following link and paste it on your web brower url bar: https://notepad-plus-plus.org/downloads/ or search for notepad ++ download and click on this website(https://notepad-plus-plus.org/downloads/ )
   
   Step 2.On the site,click on "Notepad++ 8.1.4 release". This will take you to a new web page where you must click on the image of the box that has a chemeleon on it.
   
   Step 3. Wait for a few minutes. File manager window will appear. Indicate a storage location for the file( preferrably download).
   
   Step 4. When the download is done, double click on it. The user account control window will appear, select yes.
  
   Step 5. Installer language window will appear, select English and click ok.
   
   Step 6. Notepad++ v8.1.4 window will appear, click next, agree then next.
   
   Step 7. On the Notepad++ v8.1.4 window with Choose component, tick "Create shortcut on Desktop" and click install.
    
   Step 8. Installation will start wait till it is finished.
   
   Step 9. Completing Notepad++ v8.1.4 Setup will appear, untick run and click finish.
   The installation is complete.
    
2. Install Python

    Step 1: Copy the following link and paste it on your web brower url bar:https://www.python.org/downloads/ or search for python install and click on this wesite(https://www.python.org)
    
    Step 2: The website will load.Click on the download python 3.9.7 version under the Download the latest version for Windows.
    
    Step 3: Save As window will appear , save the application under downloads on you pc.
    
    Step 4: Wait for the download to finish downloading then doule click on it to open it.
    
    Step 5: Python 3.9.7(64-bit) Setup window will appear, click on the install now.
    
    Step 6: User Account control window will appear, click yes to allow the app to make changes.
    
    Step 7: Wait for Python to finish installing
    
    Step 8: Setup was successful will appear, click close.
    Th installation is complete.
    
3. Install anaconda.

    Step 1:Copy the following link and paste it on your web brower url bar:https://docs.anaconda.com/anaconda/install/index.html or search for anaconda install and click on this wesite(https://docs.anaconda.com/anaconda/install)
    
    Step 2: Scroll down to the green coloured phrases. Click on the installing on Windows.
    
    Step 3: Click on the number 1 green coloured hyperlink which will take you to a different page. 
    
    Step 4: On the page, click on the download button on the right-hand side of your screen.
    
    Step 5: Save As window will appear , save the application under downloads on you pc.
    
    Step 6: Wait for the download to finish downloading then doule click on it to open it.
    
    Step 7: Anaconda3 2021.05(64-bit) Setup window will appear, click next, agree, next, next, install.
    
    Step 8: Wait for Anaconda to finish installation. Then when it says finish, click next.
    
    Step 9: Click next then finish
    Installation finished.
    
    
    
 
 
