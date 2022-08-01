from re import T
from tkinter.font import BOLD
from selenium import webdriver
import time
import kullaniciBilgileri as kb 
from msilib.schema import ListBox
import tkinter as tk
from typing import Text
from tkinter import *
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.chrome.service import Service as ChromeService

form = tk.Tk()
form.title("Instagram'da Takip Etmeyenleri Yakala!")
form.geometry("500x500")
form.configure(background="#07bcad")
form.iconbitmap(default="instagram.ico")

label1 = tk.Label(text="Kullanıcı Adı",font=("Helvetica",9,BOLD),fg="purple",bg="#07bcad")
label1.place(x=10, y=20)
label2 = tk.Label(text="Şifre",font=("Helvetica",9,BOLD),fg="purple",bg="#07bcad")
label2.place(x=10, y=50)



username1 = tk.Entry()
username1.place(x=100, y= 20,width=100,height=20)
password1= tk.Entry(show = "*")
password1.place(x=100, y= 50,width=100,height=20)

listbox = Listbox(form)
listbox.place(x=260, y= 50,width=220,height=360)


def verial():
    kb.userName=username1.get()
    kb.password=password1.get()
    Browser("https://www.instagram.com")
	
def temizle():
	list1.clear()
	list2.clear()
	listbox.delete(0,END)

buton = tk.Button(form,text = "Giriş",command=verial,fg="white",bg="purple",font=("Arial",10))
buton.place(x=120, y= 80,width=60,height=30)

buton2 = tk.Button(form,text = "Temizle",command=temizle,fg="white",bg="purple",font=("Arial",10))
buton2.place(x=260, y= 415,width=60,height=30)


label3 = tk.Label(text="Takip Ettiğin Fakat",font=("Helvetica",10,BOLD),fg="white",bg="#07bcad")
label3.place(x=260, y=5,width=220)
label4 = tk.Label(text="Seni Takip Etmeyen Kullanıcılar",font=("Helvetica",10,BOLD),fg="white",bg="#07bcad")
label4.place(x=260, y=25,width=220)

instagram_logo = PhotoImage(file="instagram.png")

instagram_label = tk.Label(image=instagram_logo,bg="#07bcad" )
instagram_label.place(x=20, y= 130)

kusha_logo = PhotoImage(file="kusha.png")

kusha_label = tk.Label(image=kusha_logo,bg="#07bcad" )
kusha_label.place(x=20, y= 430)

label14 = tk.Label(text="Kusha",font=("Helvetica",13,BOLD),fg="black",bg="#07bcad")
label14.place(x=110, y=430)

label15 = tk.Label(text="Engineering",font=("Helvetica",13,BOLD),fg="black",bg="#07bcad")
label15.place(x=110, y=450)

label16 = tk.Label(text="kusha-berke@hotmail.com",font=("Helvetica",10,BOLD),fg="purple",bg="#07bcad")
label16.place(x=320, y=450)

label17 = tk.Label(text="İletişim:",font=("Helvetica",10,BOLD),fg="black",bg="#07bcad")
label17.place(x=380, y=430)

label5 = tk.Label(text="- Program'a Kullanıcı Adı ve",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label5.place(x=90, y=135)

label6 = tk.Label(text="Şifre Girilir.",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label6.place(x=120, y=155)

label7 = tk.Label(text="- Ardından Giriş Tuşuna Basıldığında",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label7.place(x=20, y=190)

label8 = tk.Label(text="Chrome Tarayıcısı Açılır.",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label8.place(x=50, y=210)

label9 = tk.Label(text="- Uygun ChromeDriver Yüklü Olmalıdır.",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label9.place(x=20, y=250)

label10 = tk.Label(text="- Program Çalışırken Müdahale Etmeniz",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label10.place(x=20, y=290)

label11 = tk.Label(text="Durumunda Sorun Yaşanabilir.",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label11.place(x=50, y=310)

label12 = tk.Label(text="- Giriş Yapılırken veya Program",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label12.place(x=20, y=350)

label13 = tk.Label(text="Çalışırken Sorun Yaşarsanız",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label13.place(x=27, y=370)

label13 = tk.Label(text="Lütfen Kapatıp Tekrar Açınız.",font=("Helvetica",9,BOLD),fg="#32353d",bg="#07bcad")
label13.place(x=27, y=390)



list1=[]
list2=[]





class Browser:
	def __init__(self,link):
		options = webdriver.ChromeOptions()
		options.headless = False
		self.link = link
		chrome_service = ChromeService('chromedriver')
		chrome_service.creationflags = CREATE_NO_WINDOW
		self.browser = webdriver.Chrome(service=chrome_service,chrome_options=options)
		
		Browser.goInstagram(self)

	

	def goInstagram(self):
		self.browser.get(self.link)
		time.sleep(2)
		Browser.login(self)
		Browser.getFollowers(self)

	def getFollowers(self):

		#planWorkbook = xlsxwriter.Workbook("Instagram.xlsx")
		#planSheet = planWorkbook.add_worksheet("Followers")
		#self.browser.find_element_by_xpath("//*[@id=\"mount_0_0_PK\"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/ul/li[2]/a").click()
		self.browser.get("https://www.instagram.com/"+kb.userName+"/followers/")
		time.sleep(4)

		Browser.scrollDown(self)

		takipciler = self.browser.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")
		#sayac = 0
		#planSheet.write("A1","Takipçiler")
		for takipci in takipciler:
			#sayac += 1
			#print(str(sayac) + " --> " +takipci.text)
			#planSheet.write("A"+str(sayac+1),takipci.text)
			list1.append(takipci.text)

		self.browser.get("https://www.instagram.com/"+kb.userName+"/following/")		
		time.sleep(4)
		Browser.scrollDown(self)

		takipedilenler = self.browser.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")
		#sayac = 0
		#planSheet.write("B1","Takip Edilenler")
		for takipedilen in takipedilenler:
			#sayac += 1
			#print(str(sayac) + " --> " +takipedilen.text)
			#planSheet.write("B"+str(sayac+1),takipedilen.text)
			list2.append(takipedilen.text)

		#planWorkbook.close()
		sayac = 0
		for c in list2:
				if not c in list1:
					listbox.insert(END,c)
					

	def scrollDown(self):
		jsKomut = """
		sayfa = document.querySelector("._aano");
		sayfa.scrollTo(0,sayfa.scrollHeight);
		var sayfaSonu = sayfa.scrollHeight;
		return sayfaSonu;
		"""
		sayfaSonu = self.browser.execute_script(jsKomut)
		while True:
			son = sayfaSonu 
			time.sleep(2)
			sayfaSonu = self.browser.execute_script(jsKomut)
			if son == sayfaSonu:
				break
	

	def login(self):
		username = self.browser.find_element_by_name("username")
		password = self.browser.find_element_by_name("password")

		username.send_keys(kb.userName)
		password.send_keys(kb.password)

		loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
		loginBtn.click()
		time.sleep(4)

		 #self.browser.get(self.link+"/"+kb.userName)
		time.sleep(3)



form.mainloop()