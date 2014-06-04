import weibo  
  
APP_KEY = '1117457120' 
APP_SECRET = 'da6fa8656236e63540a9513af4fe35d4'  
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'  
  

def run():  
       
    client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)  
        
    auth_url = client.get_authorize_url()  
    
    print "auth_url : " + auth_url  
    
    code = raw_input("input the retured code : ")  
    03a86f890a0ace3076d3acdd439dca7a
    r = client.request_access_token(code)  
        
    client.set_access_token(r.access_token, r.expires_in)   
  
    while True:  
        print "Ready! Do you want to send a new weibo?(y/n)"  
        choice = raw_input()  
        if choice == 'y' or choice == 'Y':  
            content = raw_input('input the your new weibo content : ')  
            if content:  
                client.statuses.update.post(status=content)  
                print "Send succesfully!"  
                break;  
            else:  
                print "Error! Empty content!"  
        if choice == 'n' or choice == 'N':  
            break  
  
