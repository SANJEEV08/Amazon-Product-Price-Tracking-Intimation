#Importing Packages
import requests                  #Sending requests to HTTP Pages with python to allow access for its contents
import smtplib                   #Client used to send emails
from bs4 import BeautifulSoup    #Beautiful soup - used for web scrapping


#URL variable - Product (Price of the item we are checking)
URL="https://www.amazon.in/Nestle-Everyday-Dairy-Whitener-Pouch/dp/B00NYZQX9A/ref=lp_21246948031_1_1?srs=21246948031&ie=UTF8&qid=1587126878&sr=8-1"


#Headers variable - everytime the browser makes a request to a page it sends in information of the details of the system one is working with Eg:Windows version,Bit version etc.
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}


#Function definition - To track prices & analyse
def track_price():
    
    #Getting a page for access
    page=requests.get(URL,headers=headers) 

    #Getting the page content by web scrapping            
    soup=BeautifulSoup(page.content,"html.parser")   

    #Getting the Product title from the page content  
    title=soup.find(id="productTitle").get_text()           
    print(f"Product Title:{title}") 

    #Getting the Product price from the page content                    
    price=soup.find(id="priceblock_ourprice").get_text()    
    print(f"Discounted Price: {price}")

    #Converting the price to integer,excluding the ₹ symbol etc.                     
    converted_price=int(price[2:5])

    #Condition to send the email                     
    if(converted_price>400):                                
        send_mail()
        

#Function definition - To send email
def send_mail():
    
    #Defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
    server=smtplib.SMTP("smtp.gmail.com",587)

    #Mail transfer protocol - used to extend communication between the 2 ends                                
    server.ehlo()

    #Encryption - Email command to turn a insecure connection into a secure one                                                           
    server.starttls()                                                            
    server.ehlo()
    
    #Login email & app password
    server.login("sanjeevsethu8@gmail.com", "fheuiwvybpyemldz")

    #Subject of the email              
    subject="Dip in Prices!!- Grab your wishlists at prices < 400/-(INR) "

    #Body of the email   
    body="!!Left Tap your Mouse on the link to avail your discounted product!! \n Product Link - https://www.amazon.in/Nestle-Everyday-Dairy-Whitener-Pouch/dp/B00NYZQX9A/ref=lp_21246948031_1_1?srs=21246948031&ie=UTF8&qid=1587126878&sr=8-1 "  
    msg=f"Subject:{subject} \n\n {body}"
    
    #From & To email
    server.sendmail("sanjeevsethu8@gmail.com","sanjeevsethu8@gmail.com",msg)     
    print("Execution Level-Mail sent!!")
    
    #Terminating the server the server
    server.quit()                                                                
    

#Function call
track_price()