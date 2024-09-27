import platform

def about():
    s_color = "\033[92m" if platform.system() != "Windows" else ""
    e_color = "\033[0m" if platform.system() != "Windows" else ""
    about = f"""{s_color}
    
            linuxcmd Framework
            Author : yanrbts
            Contact : yanruibinghxu@gmail.com
            Twitter : @ruibingyan18530
            Codename : linuxcmd
            Project Github : https://github.com/yanrbts/linuxcmd.git
            Other Projects : https://github.com/yanrbts
            
    {e_color}"""
    print(about)