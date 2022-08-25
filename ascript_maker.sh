#!/bin/bash
#app:ascript maker
#author: elprezidento :-D 


echo " ###### Ascript Maker ###### "

echo "
 ,           ,
    /             \                                                                                                                                             
   ((__---,,,---__))                                                                                                                                            
      (_) O O (_)____________                                                                                                                                      
         \ _ /               |\                                                                                                                                    
          o_o \ elprezidento | \                                                                                                                                   
               \   _____  |__|   *                                                                                                                                  
                |||   WW|||                                                                                                                                     
                |||     |||"


read -p "name of script to create: " name_s
 
touch ${name_s}

echo "#!/bin/bash " >>${name_s}

echo " #########  Automaticaly Created Script  ########## " >>${name_s}

sudo chmod +x ${name_s}

