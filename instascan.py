# CLI interface 
import sys
from instacore import Instacore
from termcolor import colored



def show_help():
    print(colored("""
┌─────────────────────────────────────────────────────────────┐
│                    Instagram OSINT Tool                     │
│                      Version: 1.0                           │
└─────────────────────────────────────────────────────────────┘

┌─[0xhijazy@kali]──[~]
└──╼ $ python instascan.py <username> <option>

┌─[Options]
├──╼ -download      → Download post with shortcode in post url,  Example: python instascan.py <username> -download CxYZ123ABC file.mp4
├──╼ -picdownload   → Download profile picture 
├──╼ -bio           → Show user biography
├──╼ -postcount     → Show number of posts
├──╼ -status        → Show page status (public/private)
├──╼ -fullname      → Show full name
├──╼ -username      → Show username
└──╼ -help          → Show this help menu

┌─[Example]
└──╼ $ python instascan.py mrbeast -postcount

┌─[0xhijazy]
└──╼ Hoping to be useful
""",'green'))
    




def main ():
    if len(sys.argv) < 2:
        show_help()
        return
    
    username = sys.argv[1]

    

    p1 = Instacore(sys.argv[1])

    if not p1.login():
        print("Login failed!")
        return
    
    print(f'Username: {username}')

    if len(sys.argv) < 3 :
        print("Please provide an option!")
        print("Options: -bio, -status, -postcount, ...")
        return



    option = sys.argv[2]


    if option == '-download':
        if len(sys.argv) >= 4 :
            shortcode = sys.argv[3]
            save_path = sys.argv[4] if len(sys.argv) >= 5 else 'file.mp4'
        else:
            shortcode = input('Enter your shortcode:')
            save_path = input('Save as:')
        
        if p1.download_post(shortcode,save_path):
            print('Done')
        else:
            print('Failed!')

        
    elif option == '-bio':
        print(p1.get_bio())

    elif option == '-postcount':
        print(p1.get_post_count())

    elif option == '-status':
        print(p1.page_status())

    elif option == '-fullname':
        print(p1.get_full_name())

    elif option == '-username':
        print(p1.get_user_name())
    
    elif option == '-picdownload':
        if p1.download_profile_pic('profile.jpg'):
            print('Download successful!')
        else:
            print('Download failed!')
        

    else:
        print(f"Unvalid option! ->{option}")






if __name__=="__main__":
    main()
    