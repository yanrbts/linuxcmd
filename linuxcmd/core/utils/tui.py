from .version import version
from random import choice

def logo():

    banners =[ f"""\033[92m
    
 ___                                                     __     
/\_ \    __                                             /\ \    
\//\ \  /\_\    ___   __  __  __  _   ___    ___ ___    \_\ \   
  \ \ \ \/\ \ /' _ `\/\ \/\ \/\ \/'\ /'___\/' __` __`\  /'_` \  
   \_\ \_\ \ \/\ \/\ \ \ \_\ \/>  <//\ \__//\ \/\ \/\ \/\ \L\ \ 
   /\____ \\ \_\ \_\ \_\ \____//\_/\_\ \____\ \_\ \_\ \_\ \___,_\\
   \/____/ \/_/\/_/\/_/\/___/ \//\/_/\/____/\/_/\/_/\/_/\/__,_ /

    \033[0m
    """,

    f"""\033[92m
 __    ____  _  _  __  __  _  _  ___  __  __  ____  
(  )  (_  _)( \( )(  )(  )( \/ )/ __)(  \/  )(  _ \ 
 )(__  _)(_  )  (  )(__)(  )  (( (__  )    (  )(_) )
(____)(____)(_)\_)(______)(_/\_)\___)(_/\/\_)(____/ 
 
    \033[0m
    """,

    f"""\033[92m

   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ 
 ( l | i | n | u | x | c | m | d )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

    \033[0m
    """,

    f"""\033[92m


▄▄▌  ▪   ▐ ▄ ▄• ▄▌▐▄• ▄  ▄▄· • ▌ ▄ ·. ·▄▄▄▄  
██•  ██ •█▌▐██▪██▌ █▌█▌▪▐█ ▌▪·██ ▐███▪██▪ ██ 
██▪  ▐█·▐█▐▐▌█▌▐█▌ ·██· ██ ▄▄▐█ ▌▐▌▐█·▐█· ▐█▌
▐█▌▐▌▐█▌██▐█▌▐█▄█▌▪▐█·█▌▐███▌██ ██▌▐█▌██. ██ 
.▀▀▀ ▀▀▀▀▀ █▪ ▀▀▀ •▀▀ ▀▀·▀▀▀ ▀▀  █▪▀▀▀▀▀▀▀▀• 
 

    \033[0m
    """,

    ]

    return choice(banners)