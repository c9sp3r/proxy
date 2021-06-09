from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

from webdriver_manager.chrome import ChromeDriverManager

z=open("proxy.txt","r")


for i in z :
    print (i)
    proxy_ip_port = i
    
    proxy = Proxy()
    
    proxy.http_proxy = proxy_ip_port
    proxy.ssl_proxy = proxy_ip_port
    
    proxy.proxy_type = ProxyType.MANUAL
    capabilities = webdriver.DesiredCapabilities.CHROME
 
    proxy.add_to_capabilities(capabilities)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.my-ip-finder.fr/')
    time.sleep(10)
driver.quit()
