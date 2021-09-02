from tkinter import*
from tkinter import messagebox
from data_store import *
from entity_hierarchy import *
from encryption import *
import json

class Login_page(Frame):
	def __init__(self, master):
		super(Login_page, self).__init__(master)
		self.grid()
		self.create_widgets()
		self.display()
	#lables and positioning of default text to be displayed at the begining of login_page
	def display(self):
		self.inst_lbl = Label(self, text ="SecuriTree-Security Dashboard", font=("Impact", 20, "bold"), fg = "black")
		self.inst_lbl.grid(row = 0, column = 0,ipadx =3,ipady=3, sticky = W)
		self.inst_lbl0 = Label(self, text="Welcome to SecuriTree", font=("Goudy old style", 15, "bold"), fg = "grey")
		self.inst_lbl1 = Label(self, text ="Please enter your credentials to begin", font=("Goudy old style", 15, "bold"), fg = "grey")
		self.inst_lbl2 = Label(self, text ="Login" ,font=("Goudy old style", 15, "bold"), fg = "grey")
		
		self.inst_lbl0.grid(row = 1, column = 0, columnspan=2,ipadx =5, sticky = W)
		self.inst_lbl1.grid(row = 2, column = 0,columnspan=2,ipadx =5, sticky = W)
		self.inst_lbl2.grid(row = 3, column = 0,columnspan=2,ipadx =5, sticky = W)
		
	#lables and positioning of username,password and submit button 	
	def create_widgets(self):
		self.un_lbl = Label(self, text = "Username:",font=("Goudy old style", 13, "bold"), fg = "grey")
		self.pw_lbl = Label(self, text = "Password:",font=("Goudy old style", 13, "bold"), fg = "grey")
		self.lbl = Label(self, text = "")
		self.un_lbl.grid(row=4, column=0,ipadx =5,ipady=3, sticky = S)
		self.pw_lbl.grid(row = 6, column = 0,ipadx =5,ipady=3, sticky = S)
		self.un_ent = Entry(self)
		self.pw_ent = Entry(self)
		self.un_ent.grid(row =5, column =0,columnspan=4,ipadx =10,ipady=3, sticky = S)
		self.pw_ent.grid(row =7, column =0, columnspan=4,ipadx =10,ipady=3,sticky = S)
		self.lbl.grid(row =8, column =0,sticky = S)
		self.submit_bttn = Button(self, text = "Submit", command =self.login)
		self.submit_bttn.grid(row = 9, column= 0,columnspan=2,ipadx=5, sticky=S)
	#hashing and scanning of credentials
	def login(self):
		print("File encrypted!! ")
		filename = input("please enter filename:")
		key =int(input("And key:"))
		print(filename)
		if(filename =="user_management.json" and key == 25):
			f = open(filename,"rb")
			Decrypt(filename,key)
			data = json.load(f)
			user = self.un_ent.get()
			user_password = hash(self.pw_ent.get())
			num = 0
			for registered_users in data["registered_users"]:
				username= registered_users["username"]
				password= hash(registered_users["password"])
				if user == username and user_password==password:
					num += 1
			if num == 1 :
				messagebox.showwarning( "Welcome","Welcome. Please exit the login page")
				display_menu1()
				Menu_option = int(input("Option:"))
				Menu(Menu_option)
			else:
				messagebox.showerror( "Error","Invalid credentials!! Please enter valid credentials to proceed.", parent=self.master)
		else:
			print("Denied access. Incorrect filename and key")
			Encrypt(filename,key)
			self.login()
			
		
			
#functions used to display the two menu options			
def display_menu1():
	print("*"*80,"\n\t\t\tSecuritree_Security Dashboard\n","_"*80,"\n","*"*80)
	print("Main Menu Options:\n","1. View Security Entity Hierachy\n","2. Manage doors\n","3. LogOut\n\n")
def display_menu2():
	print("*"*80,"\n\t\t\tSecuritree_Security Dashboard\n","_"*80,"\n","*"*80)
	print("Door management Options:\n","1. Close Door\n","2. Open doors\n","3. Back\n\n")			
#Main menu function displayed and used on cmd
def Menu(option):
	if(option == 1):
		print("\nEntity Hierachy\n")
		print("\nPlease press ENTER to go to Main menu")
		f = open("system_data_1.json","r")
		data = json.load(f)
		if __name__ == "__main__":
			root = build_tree()
			root.print_tree()
			pass
		display_menu1()
		Menu_option = int(input("Option:"))
		Menu(Menu_option)
	elif(option == 2):
		display_menu2()
		Manage_option= int(input("Option:"))
		Manage_doors(Manage_option)
	elif(option == 3):
		root = Tk()
		root.title("SecureTree")
		root.geometry("400x330")
		root.resizable(False,False)
		app = Login_page(root)
		root.mainloop()
	else:
		print("error")
#door management menu function displayed and used on cmd
def Manage_doors(option):
	if(option == 1):
		print("*"*80,"\n\t\t\tSecuritree_Security Dashboard\n","_"*80,"\n","*"*80)
		print("Close door\n")
		print("\nPlease enter the ID of the door to closed\n")
		print("Press ESC to return to the door management screen\n")
	
		pickle_file = open('system_data_dbase.pkl','rb')
		new_data = pickle.load(pickle_file)
		if(door_id == ""):
			display_menu2()
			Manage_doors_option = int(input("Option:"))
			Manage_doors(Manage_doors_option)
		else:
			for doors in new_data['system_data']['doors']:
				door_ID = doors['id']
				door_name = doors['name']
				if door_id == door_ID:
					door_status = doors['status'] 
					doors['status'] = "closed"
					print(door_name,"Door:",door_id,doors['status'])
					f = open("dbase.pkl","wb")
					pickle.dump(new_data,f)
		
	elif(option == 2):
		print("*"*80,"\n\t\t\tSecuritree_Security Dashboard\n","_"*80,"\n","*"*80)
		print("Open door\n")
		print("\nPlease enter the ID of the door to open\n")
		print("Press ESC to return to the door management screen\n")
		door_id = input("Door ID:")
		
		for doors in new_data['system_data']['doors']:
			door_ID = doors['id']
			door_name = doors['name']
			if door_id == door_ID:
				door_status = doors['status'] 
				doors['status'] = "open"
				print(door_name,"Door:",door_id,doors['status'])
				f = open("dbase.pkl","wb")
				pickle.dump(new_data,f)
	elif(option == 3):
		display_menu1()
		Menu_option = int(input("Option:"))
		Menu(Menu_option)
		
root = Tk()
root.title("SecureTree")
root.geometry("400x330")
root.resizable(False,False)
app = Login_page(root)
root.mainloop()



