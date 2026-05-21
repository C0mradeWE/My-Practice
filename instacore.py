# Required packeges
import requests
import instaloader
from errors import  *



class Instacore: # Main Class 
    def __init__(self, username:str):
        self.username = username
        self.obj = instaloader.Instaloader()
        self.profile = None
    

    def login (self): # Login function
        try:
            self.profile = instaloader.Profile(self.obj.context, self.username)
            return True
        except:
            raise LoginFailedError('Login failed')


    def _check_login(self): # A function for check user is logged in or no
        if self.profile is None:
            raise ProfileNotFoundError('Not logged in!')
        
        
    def _check_internet(self): #Function for check Internet connection 
        try:
            
            requests.get('https://www.instagram.com', timeout= 10 )

        except :
            raise ConnectionError('No Internet connection!')
        

    def get_bio (self): #  Function for get user biography
        self._check_internet()
        self._check_login()
        return self.profile.biography
    

    def get_full_name(self): # Function for get user fullname
        self._check_internet()
        self._check_login()
        return self.profile.full_name
    
    
    def get_user_name(self):  # Function for get username
        self._check_internet()
        self._check_login()
        return self.profile.username
    
    
    def get_profile_pic_url(self):  # Function for get user profile picture URL
        self._check_internet()
        self._check_login()
        return self.profile.profile_pic_url
    
    
    def page_status(self):  # Function for check the page status (Private or Public!)
        self._check_internet()
        self._check_login()
        if self.profile.is_private == True:
            return 'This page is private'
        else:
            return 'This page is public'
        
    
    def get_post_count(self): #  # Function for get user posts count
        self._check_internet()
        self._check_login()
        return self.profile.mediacount
    
    
    
    def download_profile_pic (self, savepath = 'capture.jpg'):  # Function for download user profile picture directly 
        self._check_internet()
        self._check_login()
        url = self.get_profile_pic_url()
        response = requests.get(url)
        if response.status_code == 200:
            with open(savepath,'wb') as f :
                f.write(response.content)
            return True
        return False
    

    def download_post (self, shortcode , filepath ):  # Function for download user post from shortcode in post URL 
        self._check_internet()
        self._check_login()

        try:

            post = instaloader.Post.from_shortcode(self.obj.context , shortcode)

            if post.is_video:
                url = post.video_url
            
            elif post.typename == 'GraphImage':
                url = post.url
            
            else:
                return False
            
            response = requests.get(url)

            if response.status_code == 200:
                with open(filepath,'wb') as f :
                    f.write(response.content)
                return True
            return False
        
        except Exception as e:
            raise DownloadFailedError(f'Download failed: {e}')
