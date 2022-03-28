#!/usr/bin/env python3
from tkinter import Label, PhotoImage

class Settings():
	"Method for general widgets settings"

	def configure(self, app, path_file):
		# Screen configuration
		app.configure(background="white")
		app.geometry("1280x800")    
		app.title("INFO COVID-19")
		#app.resizable(True,True)
		app.maxsize(width=1280, height=800)
		app.minsize(width=1280, height=800)
		
		"Logo Project"
		self.__img = PhotoImage(file= path_file + "/img/" + "Logo1.png")
		self.__logo = Label(app, image=self.__img)
		self.__logo.place(x=870,y=0,width=400,height=120)
		
		"LogoIFRN Project"
		self.__imgIFRN = PhotoImage(file= path_file + "/img/" + "IFRN.png")
		self.__logoIFRN = Label(app, image=self.__imgIFRN)
		self.__logoIFRN.place(x=0,y=0,width=400,height=120)        
		
		
	def clean_frame(self, frame):
		"Method to clear frames"
	
		for i in frame.winfo_children():
			i.destroy()