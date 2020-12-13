import tkinter as tk
def Blocker():
        website_lists = Websites.get(1.0, 'END')
        Website =list(website_lists.split(","))

        with open(host_path, 'r+') as host_file:
            file_content = host_file.read()
            for website in Website:
                if website in file_content:
                    tk.Label(win, text='Already Blocked!', font = 'arial 12').place(x=200,y=200)
                    pass
                else:
                    host_file.write(ip_address + " " + website + '\n')
                    tk.Label(win, text= "Blocked", font = 'arial 12 bold').place(x=230,y=200)

win = tk.Tk()
win.geometry('800x600')
win.resizable(True, True)
win.title('Website Blocker')
win.config(bg='grey')

tk.Label(win, text='Website_blocker', font ='arial 25 bold').pack()
tk.Label(win, text='Keep Focus!', font='arial 20').pack(side='bottom')

host_path= r'D:\'
ip_address = '127.0.0.1'
tk.Label(win, text='Enter website (full url):', font = 'arial 14').place(x=5, y=60)
Websites = tk.Text(win, font = 'arial 10', height='2', width='40', wrap='word', padx=5, pady=5)
Websites.place(x = 200, y = 60)

block = tk.Button(win, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 230, y = 150)
win.mainloop()

    



