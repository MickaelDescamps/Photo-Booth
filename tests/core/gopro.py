import json
import time
import traceback
import requests
import shutil

gopro_api = "http://172.25.154.51:8080"


    

def get_state():
    try:
        route = gopro_api + "/gopro/camera/state"
        #route = gopro_api + "/gopro/webcam/version"
        
        r = requests.get(route, timeout=5)
    
        print("Status Code : \t" + str(r.status_code) +  "\nResponse : \t" + str(r.json()))
        
    except:
        pass
    

def take_photo():
    
    
    pass

def enabling_usb_control():
    
    route = gopro_api + "/gopro/camera/control/wired_usb?p=1"
    
    response = requests.get(route, timeout=5)
    
    print("Status Code : \t" + str(response.status_code) +  "\nResponse : \t" + str(response.json()))
    
def change_zoom(new_zoom):
    
    route = gopro_api + "/gopro/camera/digital_zoom?percent=" + str(new_zoom)
    
    response =requests.get(route)
    
    print("Status Code : \t" + str(response.status_code) +  "\nResponse : \t" + str(response.json()))
    
    
def enable_photo_mode():
    
    route = gopro_api + "/gopro/camera/presets/set_group?id=1001"
    
    response =requests.get(route)
    
    print("Status Code : \t" + str(response.status_code) +  "\nResponse : \t" + str(response.json()))
    
def start_capture_taking():
    
    route = gopro_api + "/gopro/camera/shutter/start"
    
    response =requests.get(route)
    
    print("Status Code : \t" + str(response.status_code))

def get_media_list() -> any:
    
    route = gopro_api + "/gopro/media/list"

    response =requests.get(route)
    
    #print("Status Code : \t" + str(response.status_code) +  "\nResponse : \t" + str(json.dumps(response.json())))
    
    return response.json()["media"][0]["fs"]

def get_photo_names(media_list_response) -> list:
    
    ret = []
    
    for media_infos in media_list_response:
        ret.append(media_infos["n"])
        
    return ret

def download_photo(file_name, directory_name):
    route = gopro_api + "/videos/DCIM/" + directory_name + "/" + file_name
    
    path = "/opt/photo_booth/images/"+ file_name

    r = requests.get(route, stream=True)
    
    print("Status code : \t" + str(r.status_code))
    
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f) 
    

if __name__ == '__main__':
    print("Hello")
    get_state()
    time.sleep(1)
    enabling_usb_control()
    time.sleep(1)
    start_capture_taking()
    time.sleep(5)
    response_media_list = get_media_list()
    photo_list = get_photo_names(response_media_list)
    
    
    for photo_name in photo_list[-6:-1]:
        
        download_photo(photo_name, "100GOPRO")
        time.sleep(1)
    
    
    print("Hello 2")

