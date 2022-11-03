import requests
import time


def hcaptcha():

    apikey = "use your own API key"
    sitekey = '3ceb8624-1970-4e6b-91d5-70317b70b651'

    page_url = "https://2captcha.com/demo/hcaptcha?difficulty=always-on"


    api = f"https://2captcha.com/in.php?key={apikey}&method=hcaptcha&sitekey={sitekey}&pageurl={page_url}&json=1&invisible=1"
    apiget = requests.get(api)
    print(apiget.json())
    rid = apiget.json().get("request")
    u2 = f"https://2captcha.com/res.php?key={apikey}&action=get&id={rid}&json=1"
    time.sleep(3)
    while True:
        r2 = requests.get(u2)
        print(r2.json())
        if r2.json().get("status") == 1:
            tftwocaptcha = r2.json().get("request")
            break
        time.sleep(4)
    data = {'h-captcha-response' : f'{tftwocaptcha}', 'xpath' :'//*[@id="root"]/div/main/div/section/form/button[1]'}
    requests.post('https://2captcha.com/demo/hcaptcha?difficulty=always-on', params = data)
    print (data)





if __name__ == '__main__':
    hcaptcha()