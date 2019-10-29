import tkinter as tk
import pickle
from tkinter import messagebox
import urllib.request
import json
import game
import requests
def usr_login():
	usr_name = var_usr_name.get()
	usr_pwd = var_usr_pwd.get()
	#进行登录验证
	url='https://api.shisanshui.rtxux.xyz/auth/login'
	headers = {'Content-Type': 'application/json'}
	Body={}
	Body['username']=usr_name
	Body['password']=usr_pwd
	r = requests.post(url=url, json=Body, headers=headers)
	res=r.json()

	if res['status'] == 0:
		tk.messagebox.showinfo(title = 'Welcome',message = '别来无恙? ' + usr_name)

		#登录验证获得对战id
		url2='https://api.shisanshui.rtxux.xyz/auth/validate'
		header2 = {'Content-Type': 'application/json','X-Auth-Token':res['data']['token'] }
	
		r2 = requests.get(url=url2,  headers=header2)
		res2=r2.json()
		
		window.destroy()
		game.Game(res['data']['token'],res2['data']['user_id'])
	else:
		is_sign_up = tk.messagebox.askyesno('Welcome','你的密码错误或者是账号未注册。是否注册新账号?')
		if is_sign_up:
			usr_sign_up()

def usr_sign_up():
	
	def sign_to_Mofan_Python():

		np = new_pwd.get()
		npf = new_pwd_confirm.get()
		nn = new_name.get()

		n1=stu.get()
		nn1=pwd.get()

		if np!= npf:
			tk.messagebox.showerror('Error','Password and confirm password must be the same!')
		else:
			Body={}
			Body['username']=nn
			Body['password']=np
			Body['student_number']=n1
			Body['student_password']=nn1
			url='https://api.shisanshui.rtxux.xyz/auth/register2'
			headers = {'Content-Type': 'application/json'}
			r = requests.post(url=url, json=Body, headers=headers)
			res=r.json()
			if res['status'] == 0:
				tk.messagebox.showinfo('Welcome','You have successfully signed up!')
			elif res['status']== 1002:
				tk.messagebox.showerror('哦吼！', '学号已经绑定')
			elif res['status']== 1003:
				tk.messagebox.showerror('哦吼！', '教务处认证失败')
			elif res['status']== 1004:
				tk.messagebox.showerror('哦吼！', '不存在此学号')
			else :
				tk.messagebox.showerror('哦吼！','似乎用户名已经被注册过了')

	window_sign_up = tk.Toplevel(window)
	window_sign_up.geometry('350x250')
	window_sign_up.title('Sign up window')

	new_name = tk.StringVar()
	tk.Label(window_sign_up,text ='用户名:').place(x = 10,y = 10)
	entry_new_name = tk.Entry(window_sign_up,textvariable = new_name)
	entry_new_name.place(x = 150,y = 10)
	
	new_pwd = tk.StringVar()
	tk.Label(window_sign_up,text = '密码:').place(x = 10,y = 50)
	entry_new_pwd = tk.Entry(window_sign_up,textvariable = new_pwd,show = '*')
	entry_new_pwd.place(x = 150,y = 50)



	stu = tk.StringVar()
	tk.Label(window_sign_up,text = '教务处账号:').place(x = 10,y = 130)
	student= tk.Entry(window_sign_up,textvariable = stu,show = '*')
	student.place(x = 150,y = 130)

	pwd = tk.StringVar()
	tk.Label(window_sign_up, text='教务处密码:').place(x=10, y=170)
	stu_pwd = tk.Entry(window_sign_up, textvariable=pwd, show='*')
	stu_pwd.place(x=150, y=170)

	new_pwd_confirm = tk.StringVar()
	tk.Label(window_sign_up, text='确认密码:').place(x=10, y=90)
	entry_comfirm_sign_up = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
	entry_comfirm_sign_up.place(x=150, y=90)

	btn_comfirm_sign_up = tk.Button(window_sign_up,text = 'Sign up',command = sign_to_Mofan_Python)
	btn_comfirm_sign_up.place(x = 150,y = 200)
	

def run():
	window.mainloop()


window = tk.Tk()
window.title('福建十三水')
window.geometry('450x300')
#welcome image
#创建一个200X500的画布
canvas =  tk.Canvas(window,height = 450,width = 500)
#logo的路径
image_file = tk.PhotoImage(file ='IMA/12.gif')
#什么位置插入logo图片
image = canvas.create_image(0,0,anchor = 'nw',image = image_file)
canvas.pack(side = 'top')
tk.Label(window,text = 'Username:').place(x = 50,y = 150)
tk.Label(window,text = 'Password:').place(x = 50,y = 190)
var_usr_name = tk.StringVar()
var_usr_pwd = tk.StringVar()
entry_usr_name = tk.Entry(window,textvariable = var_usr_name)
entry_usr_name.place(x = 160,y = 150)
entry_usr_pwd = tk.Entry(window,textvariable = var_usr_pwd,show ='*')
entry_usr_pwd.place(x = 160,y = 190)
#Login and Sign up button
# command = usr_login 调用usr_login函数
btn_login = tk.Button(window,text = '登录',command = usr_login)
btn_login.place(x = 170,y = 230)
btn_sign_up = tk.Button(window,text = '注册',command = usr_sign_up)
btn_sign_up.place(x = 270,y = 230)
