from tkinter import *
from functools import partial 
from tkinter import messagebox

root=Tk()
w=650
h=350
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
root.resizable(False,False)
inner_frame_1=Frame(root,bg="green")
inner_frame_2=Frame(root,bg="red")
input_text=Entry(inner_frame_2,font=("Courier",15))
output_text=Entry(inner_frame_2,font=("Courier",15))
bt_list=[]
count_backet=0

def solve(x):
	global copy_text
	global count_backet
	temp=['0','1','2','3','4','5','6','7','8','9','+','-','×','÷','⌫','.','CE','()']
	if x in temp:
		if(x=='⌫'):
			print('⌫')
			input_text.delete(len(input_text.get())-1)
		elif(x=='CE'):
			input_text.delete(0,END)
			count_backet=0
		elif(x=='()'):
			count_backet+=1
			if(count_backet%2!=0):
				input_text.insert(END,'(')
			else:
				input_text.insert(END,')')
		else:
			input_text.insert(END,x)
	elif(x=='=' or x=='CoPy'):
		try:
			e=""
			output_text['state']=NORMAL
			e=input_text.get().replace('×','*')
			e=e.replace('÷','/')
			output_text.delete(first=0,last=END)
			output_text.insert(0,"=>"+str(eval(e)))
			if(x=='CoPy'):
				root.clipboard_append(str(eval(e)))
			output_text['state']=DISABLED
		except:
			messagebox.showwarning("Warning","Wrong Input!!!!")

def calculate(event):
	solve('=')

def draw():
	count=0
	for i in range(20):
		bt_list.append(Button(inner_frame_1,text=i,font=("Courier",20),cursor="hand2",compound="center"))

	for i in range(5):
		for j in range(4):
			bt_list[count].grid(row=i,column=j,sticky="nswe",padx=1,pady=1)
			if(count==0):
				bt_list[count]['text']='1'
			elif(count==1):
				bt_list[count]['text']='2'
			elif(count==2):
				bt_list[count]['text']='3'
			elif(count==3):
				bt_list[count]['text']='+'
			elif(count==4):
				bt_list[count]['text']='4'
			elif(count==5):
				bt_list[count]['text']='5'
			elif(count==6):
				bt_list[count]['text']='6'
			elif(count==7):
				bt_list[count]['text']='-'
			elif(count==8):
				bt_list[count]['text']='7'
			elif(count==9):
				bt_list[count]['text']='8'
			elif(count==10):
				bt_list[count]['text']='9'
			elif(count==11):
				bt_list[count]['text']='×'
			elif(count==12):
				bt_list[count]['text']='0'
			elif(count==13):
				bt_list[count]['text']='()'
			elif(count==14):
				bt_list[count]['text']='.'
			elif(count==15):
				bt_list[count]['text']='÷'
			elif(count==16):
				bt_list[count]['text']='CoPy'
			elif(count==17):
				bt_list[count]['text']='CE'
			elif(count==18):
				bt_list[count]['text']='⌫'
			elif(count==19):
				bt_list[count]['text']='='
			bt_list[count]['command']=partial(solve,bt_list[count]['text'])
			count+=1
	inner_frame_1.grid_columnconfigure((0,1,2,3),weight=1)
	inner_frame_1.grid_rowconfigure((0,1,2),weight=1)


if __name__ == '__main__':
	inner_frame_1.pack(side=BOTTOM,expand=True,fill='both')
	inner_frame_2.pack(side=TOP,expand=True,fill='both')
	input_text.grid(row=0,column=0,sticky="nswe",padx=1,pady=1)
	output_text['state']=DISABLED
	input_text.focus_set()
	output_text.grid(row=1,column=0,sticky="nswe",padx=1,pady=1)
	
	inner_frame_2.grid_columnconfigure((0),weight=1)
	inner_frame_2.grid_rowconfigure((0,1),weight=1)
	root.bind('<Return>',calculate)
	draw()
	root.mainloop()