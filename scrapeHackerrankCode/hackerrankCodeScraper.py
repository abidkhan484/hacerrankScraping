from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os


def findCssMore(css):
    try:
        return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))
    except:
        pass

def findCssOne(css):
    try:
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    except:
        pass
    

def login_to_hackerrank():
    driver.get('https://www.hackerrank.com/login')

    # click for the login page
    #driver.find_element_by_css_selector("a[class='btn btn-line btn-flat btn-green mlL']").click()
    
    # send user name and password to the browser
    name = input('input your user name: ').strip()
    css = "input[id='login']"
    elem = findCssOne(css)
    elem.send_keys(name)
    
    password = input('input your password: ').strip()
    css = "input[id='password']"
    elem = findCssMore(css)
    elem[1].send_keys(password)
    
    css = "button[class='btn btn-primary login-button auth']"
    elem = findCssOne(css)
    elem.click()
    # if internet connection is slow then this time should be increased by the user
    time.sleep(2)

    return

def urlsCollection():
    login_to_hackerrank()
    driver.get('https://www.hackerrank.com/submissions/all')
        
    # this variable keeps how many pages of submission
    # here 'data-attr8' is the attribute that holds how many submission page
    # and it is the last element of the list that's why i use [-1]
    
    # here the class name is 'backbone'
    try:
        var = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located\
                           ((By.CLASS_NAME, 'backbone')))[-1].get_attribute('data-attr8')
    except:
        pass
    
    urls = []
    for i in range(int(var)):
        url = 'https://www.hackerrank.com/submissions/all/page/' + str(i+1)
        driver.get(url)
        
        # all submissions of a page
        css = "a[class='btn btn-inverse view-results backbone']"
        linksOnPage = findCssMore(css)
        for p in linksOnPage:
            url = p.get_attribute('href')
            # here's the urls list where my submission is
            urls.append(url)    
    
    for p in linksOnPage:
        url = p.get_attribute('href')
        urls.append(url)

    return urls


def collectInfo(urls):
    for p in range(len(urls)):
        driver.get(urls[p])

        css = 'span[class="status pull-right bold small psR color-orange"]'
        status = findCssOne(css)
        
        if not status:
            css = 'span[class="status pull-right bold small psR color-green"]'
            status = findCssOne(css)
        status = status.text[8:]
        
        css = "p[class='msT msB small']"
        lang = findCssOne(css).text[10:]
        # here url is the current url (driver.current_url)
        # here urls[p]
        filename = urls[p].split('/')[4]
        
        css = 'span[role="presentation"]'
        c = findCssMore(css)
        code = ''
        for i in range(len(c)):
            code += (c[i].text + '\n')
            
        
        # i just add python extension
        if (lang=='Python 2') or (lang=='Python 3'):
            filename = filename + '.py'
        else:
            filename = filename + '.txt'
        
        if filename not in os.listdir():
            with open(filename, 'w') as f:
                tmp = '# ' + status + '\n' + '# ' + lang +'\n\n' + code
                f.write(tmp)
        else:
            filename = filename[:-3]
            filename = filename + str(p) + '.py'
            with open(filename, 'w') as f:
                tmp = '# ' + status + '\n' + '# ' + lang +'\n\n' + code
                f.write(tmp)
        


driver = webdriver.PhantomJS()
urls = urlsCollection()
collectInfo(urls)







'''
# I used the code when i first scrape the site. 
# but now i can make it better by using "Explicit Wait" of selenium.
# login_to_hackerrank function was added here below. i just modify the login function.



def urlsCollection():
    login_to_hackerrank()
    driver.get('https://www.hackerrank.com/submissions/all')
        
    # this variable keeps how many pages of submission
    # here 'data-attr8' is the attribute that holds how many submission page
    # and it is the last element of the list that's why i use [-1]
    
    var = 0
    while not var:
        var = driver.find_elements_by_class_name('backbone')[-1].get_attribute('data-attr8')
    
    urls = []
    for i in range(int(var)-1):
        url = 'https://www.hackerrank.com/submissions/all/page/' + str(i+1)
        driver.get(url)
        
        # all submissions of a page
        linksOnPage = []
        # need some better process to scrape the submissions
        while len(linksOnPage) < 10:
            linksOnPage = driver.find_elements_by_css_selector("a[class='btn btn-inverse view-results backbone']")
        for p in linksOnPage:
            url = p.get_attribute('href')
            # here's the urls list where my submission is
            urls.append(url)

        print(len(urls))
    
    url = 'https://www.hackerrank.com/submissions/all/page/' + str(i+1)
    driver.get(url)
    linksOnPage = []
    while len(linksOnPage) < 3:
        linksOnPage = driver.find_elements_by_css_selector("a[class='btn btn-inverse view-results backbone']")
    
    for p in linksOnPage:
        url = p.get_attribute('href')
        urls.append(url)
    
    with open('links.txt', 'w') as f:
        f.write('\n'.join(urls))
    
    return urls


# here i already scrape the links "links.txt" using "urlsCollection" function

driver = webdriver.PhantomJS()
login_to_hackerrank()
urls = urlsCollection()
with open('links.txt', 'r') as f:
    urls = f.read().split('\n')
os.chdir('codes')

for p in range(len(urls)):
    #def collectInfo(url):
    k = 0
    while k != 10:
        if k==9:
            print('urls', p)
        try:
            driver.get(urls[p])
            
            try:    
                status = driver.find_element_by_css_selector('span[class="status pull-right bold small psR color-orange"]').text[8:]
            except:
                status = driver.find_element_by_css_selector('span[class="status pull-right bold small psR color-green"]').text[8:]
            lang = driver.find_element_by_css_selector("p[class='msT msB small']").text[10:]
            # here url is the current url (driver.current_url)
            filename = urls[p].split('/')[4]
            
            c = []
            # i have find something better approach to solve this problem
            while not c:
                c = driver.find_elements_by_css_selector('span[role="presentation"]')
            code = ''
            for i in range(len(c)):
                code += (c[i].text + '\n')
            
            # i just add python extension
            if (lang=='Python 2') or (lang=='Python 3'):
                filename = filename + '.py'
            else:
                filename = filename + '.txt'
            
            if filename not in os.listdir():
                with open(filename, 'w') as f:
                    tmp = '# ' + status + '\n' + '# ' + lang +'\n\n' + code
                    f.write(tmp)
            else:
                filename = filename[:-3]
                filename = filename + str(p) + '.py'
                with open(filename, 'w') as f:
                    tmp = '# ' + status + '\n' + '# ' + lang +'\n\n' + code
                    f.write(tmp)
        
            print(p)
            break
        except:
            k += 1
            
'''
