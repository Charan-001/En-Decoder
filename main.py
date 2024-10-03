from tkinter import *
import tkinter.messagebox
import tkinter.messagebox as messagebox

root = Tk()
root.title("En|Decoder")
root.geometry("700x500+0+0")
root.configure(bg='black')

def encrypt_decrypt(text,key):
    encrypted = ''.join(chr(ord(x)^key) for x in text)
    return encrypted


def encrypt():
    try:
        key = int(key_entry.get())
        plaintext = plaintext_text.get("1.0", END).strip()
        encrypted = encrypt_decrypt(plaintext,key)
        plaintext_text.delete("1.0",END)
        plaintext_text.insert("1.0",encrypted)
        key_entry.delete(0,END)
    except Exception as e:
        messagebox.showerror("Error", str(e)) 

def decrypt():
    try:
        key = int(key_entry.get())
        plaintext = plaintext_text.get("1.0", END).strip()
        decrypted = encrypt_decrypt(plaintext,key)
        plaintext_text.delete("1.0",END)
        plaintext_text.insert("1.0",decrypted)
        key_entry.delete(0,END)
    except Exception as e:
        messagebox.showerror("Error", str(e)) 

def reset():
    key_entry.delete(0,END)
    key_entry.focus()
    plaintext_text.delete("1.0",END)

def exit():
    exit = tkinter.messagebox.askyesno("En|Decoder","Confirm if you want to exit?")
    if exit > 0:
        root.destroy()
        return



plain_frame = Frame(root,bg= "black")
plain_frame.pack(pady=20)

plaintext_label=Label(plain_frame,font=('arial',15,'bold'),bg='black', fg='#f00',text='Enter Plain Text:')
plaintext_label.pack(pady=10 )
plaintext_text=Text(plain_frame,font=('arial',15,'bold'),bg='black', fg='green',width=40,height=8 )
plaintext_text.pack(pady=10 )

key_frame = Frame(root,bg= "black")
key_frame.pack(pady=20 )

key_label=Label(key_frame,font=('arial',15,'bold'),bg='black', fg='#f00',text='Enter Pass Key:')
key_label.pack(side=LEFT,padx=10 )
key_entry=Entry(key_frame,font=('arial',15,'bold'),bg='black', fg='green',width=10,justify='center',show="*")
key_entry.pack(side=LEFT,padx=10 )

button_frame = Frame(root,bg= "black")
button_frame.pack()

Encrypt_button=Button(button_frame,font=('arial',15,'bold'),bg='black', fg='#f00',width=10,text='Encrypt',command= encrypt)
Encrypt_button.pack(side=LEFT,padx=10 )

Decrypt_button=Button(button_frame,font=('arial',15,'bold'),bg='black', fg='#f00',width=10,text='Decrypt',command= decrypt)
Decrypt_button.pack(side=LEFT,padx=10 )

Reset_button=Button(button_frame,font=('arial',15,'bold'),bg='black', fg='#f00',width=10,text='Reset',command= reset)
Reset_button.pack(side=LEFT,padx=10 )

Exit_button=Button(button_frame,font=('arial',15,'bold'),bg='black', fg='#f00',width=10,text='Exit',command= exit)
Exit_button.pack(side=LEFT,padx=10 )




root.mainloop()