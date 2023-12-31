import tkinter as tk
from tkinter import messagebox
import enigma


window = tk.Tk()
window.title("ENIGMA")
allhuruf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
hurufrotor1 = "A"
hurufrotor2 = "A"
hurufrotor3 = "A"
notch1 = "Q"
notch2 = "E"
notch3 = "V"
listallhuruf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
rotor1all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")] #Left
rotor2all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")] #Middle
rotor3all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")] #Right
reflector = [list("YRUHQSLDPXNGOKMIEBFZCWVJAT"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
window.configure(bg="#33FF99", padx=10, pady=10, relief="groove", borderwidth=5, cursor="arrow")



def alan_turing():
    global rotor1all
    global rotor2all
    global rotor3all
    global hurufrotor1
    global hurufrotor2
    global hurufrotor3
    global reflector
    global listallhuruf
    global notch1
    global notch2
    global notch3
    getinput = input1.get().upper()
    inputtext.config(state="normal")
    inputtext.delete("1.0", tk.END)
    inputtext.insert(tk.END, getinput + "\n")
    inputtext.config(state="disabled")
    hasilalan = enigma.alan_turing(getinput)
    hasil = ""
    if(hasilalan=="Error"):
        messagebox.showerror("Error", "Input tidak valid")
    elif(hasilalan=="None"):
        messagebox.showerror("Alert", "Tidak dapat menemukan kecocokan")
    else:
        rincian = "Initial Position: " + hasilalan[0][0] + "\n"
        rincian += "Rotor Left: " + hasilalan[0][1] + "\n"
        rincian += "Rotor Middle: " + hasilalan[0][2] + "\n"
        rincian += "Rotor Right: " + hasilalan[0][3] + "\n \n"
        if(hasilalan[0][1]=="1"):
            rotor1all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch1 = "Q"
            hurufrotor1 = "A"
        elif(hasilalan[0][1]=="2"):
            rotor1all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch1 = "E"
            hurufrotor1 = "A"
        elif(hasilalan[0][1]=="3"):
            rotor1all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch1 = "V"
            hurufrotor1 = "A"
        if(hasilalan[0][2]=="1"):
            rotor2all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch2 = "Q"
            hurufrotor2 = "A"
        elif(hasilalan[0][2]=="2"):
            rotor2all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch2 = "E"
            hurufrotor2 = "A"
        elif(hasilalan[0][2]=="3"):
            rotor2all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch2 = "V"
            hurufrotor2 = "A"
        if(hasilalan[0][3]=="1"):
            rotor3all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch3 = "Q"
            hurufrotor3 = "A"
        elif(hasilalan[0][3]=="2"):
            rotor3all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch3 = "E"
            hurufrotor3 = "A"
        elif(hasilalan[0][3]=="3"):
            rotor3all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
            notch3 = "V"
            hurufrotor3 = "A"
        if(hasilalan[0][0][0]!=hurufrotor1):
            while(True):
                if(rotor1all[1][0]!=hasilalan[0][0][0]):
                    enigma.nextrotor(rotor1all)
                else:
                    break
        if(hasilalan[0][0][1]!=hurufrotor2):
            while(True):
                if(rotor2all[1][0]!=hasilalan[0][0][1]):
                    enigma.nextrotor(rotor2all)
                else:
                    break
        if(hasilalan[0][0][2]!=hurufrotor3):
            while(True):
                if(rotor3all[1][0]!=hasilalan[0][0][2]):
                    enigma.nextrotor(rotor3all)
                else:
                    break
        for i in range(len(getinput)):
            if(getinput[i] == " "):
                hasil += " "
                continue
            else:
                if(rotor2all[1][0]==notch2 and rotor3all[1][0]==notch3):
                    enigma.nextrotor(rotor3all)
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor1all)
                elif(rotor2all[1][0]==notch2):
                    enigma.nextrotor(rotor3all)
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor1all)
                elif(rotor3all[1][0]==notch3):
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor3all)
                else:
                    enigma.nextrotor(rotor3all)
                hasilenigma,r11,r21,r31,ref,r32,r22,r12 = enigma.enigma(getinput[i],listallhuruf,rotor3all,rotor2all,rotor1all,reflector)
                hasil += hasilenigma
                rincian += "Huruf input: " + getinput[i] + "\n"
                rincian += "Current Rotor Position: " + rotor1all[1][0] + rotor2all[1][0] + rotor3all[1][0] + "\n"
                rincian += "Rotor 3: " + r11 + "\n"
                rincian += "Rotor 2: " + r21 + "\n"
                rincian += "Rotor 1: " + r31 + "\n"
                rincian += "Reflector: " + ref + "\n"
                rincian += "Rotor 1: " + r32 + "\n"
                rincian += "Rotor 2: " + r22 + "\n"
                rincian += "Rotor 3: " + r12 + "\n"
                rincian += "Huruf output: " + hasilenigma + "\n"
                rincian += "\n"
        outputtext.config(state="normal")
        outputtext.delete("1.0", tk.END)
        outputtext.insert(tk.END, hasil + "\n")
        outputtext.config(state="disabled")
        hurufrotor1  = rotor1all[1][0]
        hurufrotor2  = rotor2all[1][0]
        hurufrotor3  = rotor3all[1][0]
        huruf1.set(hurufrotor1)
        huruf2.set(hurufrotor2)
        huruf3.set(hurufrotor3)
        textrincian.config(state="normal")
        textrincian.delete("1.0", tk.END)
        textrincian.insert(tk.END, rincian + "\n")
        textrincian.config(state="disabled")
        
        


def inputketext():
    global rotor1all
    global rotor2all
    global rotor3all
    global hurufrotor1
    global hurufrotor2
    global hurufrotor3
    global reflector
    global listallhuruf
    global notch1
    global notch2
    global notch3
    if(menurotorleft.get()=="I"):
        rotor1all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch1 = "Q"
        hurufrotor1 = "A"
    elif(menurotorleft.get()=="II"):
        rotor1all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch1 = "E"
        hurufrotor1 = "A"
    elif(menurotorleft.get()=="III"):
        rotor1all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch1 = "V"
        hurufrotor1 = "A"
    if(menurotormiddle.get()=="I"):
        rotor2all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch2 = "Q"
        hurufrotor2 = "A"
    elif(menurotormiddle.get()=="II"):
        rotor2all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch2 = "E"
        hurufrotor2 = "A"
    elif(menurotormiddle.get()=="III"):
        rotor2all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch2 = "V"
        hurufrotor2 = "A"
    if(menurotorright.get()=="I"):
        rotor3all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch3 = "Q"
        hurufrotor3 = "A"
    elif(menurotorright.get()=="II"):
        rotor3all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch3 = "E"
        hurufrotor3 = "A"
    elif(menurotorright.get()=="III"):
        rotor3all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        notch3 = "V"
        hurufrotor3 = "A"
    rincian = ""
    hasil = ""
    getinput = input1.get().upper()
    inputtext.config(state="normal")
    inputtext.delete("1.0", tk.END)
    inputtext.insert(tk.END, getinput + "\n")
    inputtext.config(state="disabled")
    getplugin = plugin1.get().upper()
    if(enigma.makeplugin(getplugin)== "Error"):
        messagebox.showerror("Error", "Plugin tidak valid")
    elif(enigma.makeplugin(getplugin)==[]):
        if(huruf1.get()!=hurufrotor1):
            while(True):
                if(rotor1all[1][0]!=huruf1.get()):
                    enigma.nextrotor(rotor1all)
                else:
                    break
        if(huruf2.get()!=hurufrotor2):
            while(True):
                if(rotor2all[1][0]!=huruf2.get()):
                    enigma.nextrotor(rotor2all)
                else:
                    break
        if(huruf3.get()!=hurufrotor3):
            while(True):
                if(rotor3all[1][0]!=huruf3.get()):
                    enigma.nextrotor(rotor3all)
                else:
                    break
        
        for i in range(len(getinput)):
            if(getinput[i] == " "):
                hasil += " "
                continue
            else:
                if(rotor2all[1][0]==notch2 and rotor3all[1][0]==notch3):
                    enigma.nextrotor(rotor3all)
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor1all)
                elif(rotor2all[1][0]==notch2):
                    enigma.nextrotor(rotor3all)
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor1all)
                elif(rotor3all[1][0]==notch3):
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor3all)
                else:
                    enigma.nextrotor(rotor3all)
                hasilenigma,r11,r21,r31,ref,r32,r22,r12 = enigma.enigma(getinput[i],listallhuruf,rotor3all,rotor2all,rotor1all,reflector)
                hasil += hasilenigma
                rincian += "Huruf input: " + getinput[i] + "\n"
                rincian += "Current Rotor Position: " + rotor1all[1][0] + rotor2all[1][0] + rotor3all[1][0] + "\n"
                rincian += "Rotor 3: " + r11 + "\n"
                rincian += "Rotor 2: " + r21 + "\n"
                rincian += "Rotor 1: " + r31 + "\n"
                rincian += "Reflector: " + ref + "\n"
                rincian += "Rotor 1: " + r32 + "\n"
                rincian += "Rotor 2: " + r22 + "\n"
                rincian += "Rotor 3: " + r12 + "\n"
                rincian += "Huruf output: " + hasilenigma + "\n"
                rincian += "\n"

        outputtext.config(state="normal")
        outputtext.delete("1.0", tk.END)
        outputtext.insert(tk.END, hasil + "\n")
        outputtext.config(state="disabled")
        textrincian.config(state="normal")
        textrincian.delete("1.0", tk.END)
        textrincian.insert(tk.END, rincian + "\n")
        textrincian.config(state="disabled")
        hurufrotor1  = rotor1all[1][0]
        hurufrotor2  = rotor2all[1][0]
        hurufrotor3  = rotor3all[1][0]
        huruf1.set(hurufrotor1)
        huruf2.set(hurufrotor2)
        huruf3.set(hurufrotor3)
    else:
        if(huruf1.get()!=hurufrotor1):
            while(True):
                if(rotor1all[1][0]!=huruf1.get()):
                    enigma.nextrotor(rotor1all)
                else:
                    break
        if(huruf2.get()!=hurufrotor2):
            while(True):
                if(rotor2all[1][0]!=huruf2.get()):
                    enigma.nextrotor(rotor2all)
                else:
                    break
        if(huruf3.get()!=hurufrotor3):
            while(True):
                if(rotor3all[1][0]!=huruf3.get()):
                    enigma.nextrotor(rotor3all)
                else:
                    break
        
        for i in range(len(getinput)):
            if(getinput[i] == " "):
                hasil += " "
                continue
            else:
                if(rotor2all[1][0]==notch2 and rotor3all[1][0]==notch3):
                    enigma.nextrotor(rotor3all)
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor1all)
                elif(rotor2all[1][0]==notch2):
                    enigma.nextrotor(rotor3all)
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor1all)
                elif(rotor3all[1][0]==notch3):
                    enigma.nextrotor(rotor2all)
                    enigma.nextrotor(rotor3all)
                else:
                    enigma.nextrotor(rotor3all)
                hasilenigma,r11,r21,r31,ref,r32,r22,r12,plugawal = enigma.enigma_plugin(getinput[i],getplugin,listallhuruf,rotor3all,rotor2all,rotor1all,reflector)
                hasil += hasilenigma
                rincian += "Huruf input: " + getinput[i] + "\n"
                rincian += "Current Rotor Position: " + rotor1all[1][0] + rotor2all[1][0] + rotor3all[1][0] + "\n"
                rincian += "Plugboard: " + plugawal + "\n"
                rincian += "Rotor 3: " + r11 + "\n"
                rincian += "Rotor 2: " + r21 + "\n"
                rincian += "Rotor 1: " + r31 + "\n"
                rincian += "Reflector: " + ref + "\n"
                rincian += "Rotor 1: " + r32 + "\n"
                rincian += "Rotor 2: " + r22 + "\n"
                rincian += "Rotor 3: " + r12 + "\n"
                rincian += "Plugboard: " + hasilenigma + "\n"
                rincian += "Huruf output: " + hasilenigma + "\n"
                rincian += "\n"

        outputtext.config(state="normal")
        outputtext.delete("1.0", tk.END)
        outputtext.insert(tk.END, hasil + "\n")
        outputtext.config(state="disabled")
        textrincian.config(state="normal")
        textrincian.delete("1.0", tk.END)
        textrincian.insert(tk.END, rincian + "\n")
        textrincian.config(state="disabled")
        hurufrotor1  = rotor1all[1][0]
        hurufrotor2  = rotor2all[1][0]
        hurufrotor3  = rotor3all[1][0]
        huruf1.set(hurufrotor1)
        huruf2.set(hurufrotor2)
        huruf3.set(hurufrotor3)

def alan_turing_plugin():
    global rotor1all
    global rotor2all
    global rotor3all
    global hurufrotor1
    global hurufrotor2
    global hurufrotor3
    global reflector
    global listallhuruf
    global notch1
    global notch2
    global notch3
    rincian = ""
    hasil = ""
    getinput = input1.get().upper()
    inputtext.config(state="normal")
    inputtext.delete("1.0", tk.END)
    inputtext.insert(tk.END, getinput + "\n")
    inputtext.config(state="disabled")
    if(teliti.get()=="Tidak Teliti"):
        hasilalanplugin = enigma.alan_turing_plugin(getinput)
    else:
        hasilalanplugin = enigma.alan_turing_plugin_teliti(getinput)
    if(hasilalanplugin=="None"):
        messagebox.showerror("Error", "Tidak dapat menemukan kecocokan")
    else:
        jml = 0
        for i in range(len(hasilalanplugin)):
            init = hasilalanplugin[i][0]
            rotor1 = hasilalanplugin[i][1]
            rotor2 = hasilalanplugin[i][2]
            rotor3 = hasilalanplugin[i][3]
            plugboard = hasilalanplugin[i][4]
            if(rotor1=="1"):
                rotor1all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch1 = "Q"
                hurufrotor1 = "A"
            elif(rotor1=="2"):
                rotor1all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch1 = "E"
                hurufrotor1 = "A" 
            elif(rotor1=="3"):
                rotor1all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch1 = "V"
                hurufrotor1 = "A"
            if(rotor2=="1"):
                rotor2all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch2 = "Q"
                hurufrotor2 = "A"
            elif(rotor2=="2"):
                rotor2all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch2 = "E"
                hurufrotor2 = "A"
            elif(rotor2=="3"):
                rotor2all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch2 = "V"
                hurufrotor2 = "A"
            if(rotor3=="1"):
                rotor3all = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch3 = "Q"
                hurufrotor3 = "A"
            elif(rotor3=="2"):
                rotor3all = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch3 = "E"
                hurufrotor3 = "A"
            elif(rotor3=="3"):
                rotor3all = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                notch3 = "V"
                hurufrotor3 = "A"
            if(init[0]!=hurufrotor1):
                while(True):
                    if(rotor1all[1][0]!=init[0]):
                        enigma.nextrotor(rotor1all)
                    else:
                        break
            if(init[1]!=hurufrotor2):
                while(True):
                    if(rotor2all[1][0]!=init[1]):
                        enigma.nextrotor(rotor2all)
                    else:
                        break
            if(init[2]!=hurufrotor3):
                while(True):
                    if(rotor3all[1][0]!=init[2]):
                        enigma.nextrotor(rotor3all)
                    else:
                        break
            hasilencript = ""
            for j in range(len(getinput)):
                if(getinput[j]==" "):
                    hasilencript += " "
                
                else:
                    if(rotor2all[1][0]==notch2 and rotor3all[1][0]==notch3):
                        enigma.nextrotor(rotor3all)
                        enigma.nextrotor(rotor2all)
                        enigma.nextrotor(rotor1all)
                    elif(rotor2all[1][0]==notch2):
                        enigma.nextrotor(rotor3all)
                        enigma.nextrotor(rotor2all)
                        enigma.nextrotor(rotor1all)
                    elif(rotor3all[1][0]==notch3):
                        enigma.nextrotor(rotor2all)
                        enigma.nextrotor(rotor3all)
                    else:
                        enigma.nextrotor(rotor3all)
                    hasilenigma,r11,r21,r31,ref,r32,r22,r12,plugawal = enigma.enigma_plugin(getinput[j],plugboard,listallhuruf,rotor3all,rotor2all,rotor1all,reflector)
                    hasilencript += hasilenigma
            if(hasilencript[0]=="H" and hasilencript[1]=="E" and hasilencript[2]=="L" and hasilencript[3]=="L" and hasilencript[4]=="O" and hasilencript[5]==" " and hasilencript[6]=="S" and hasilencript[7]=="U" and hasilencript[8]=="D" and hasilencript[9]=="O"):
                jml+=1
                hasil += str(jml)+". Kemungkinan ke-"+str(jml)+"\n"
                hasil += hasilencript + "\n\n"
                rincian += str(jml)+". Kemungkinan ke-"+str(jml)+"\n"
                rincian += "Initial Position: " + init + "\n"
                rincian += "Rotor Left: " + rotor1 + "\n"
                rincian += "Rotor Middle: " + rotor2 + "\n"
                rincian += "Rotor Right: " + rotor3 + "\n"
                rincian += "Plugboard: " + plugboard + "\n\n"
        print(jml)
    outputtext.config(state="normal")
    outputtext.delete("1.0", tk.END)
    outputtext.insert(tk.END, hasil + "\n")
    outputtext.config(state="disabled")
    textrincian.config(state="normal")
    textrincian.delete("1.0", tk.END)
    textrincian.insert(tk.END, rincian + "\n")
    textrincian.config(state="disabled")
    hurufrotor1  = rotor1all[1][0]
    hurufrotor2  = rotor2all[1][0]
    hurufrotor3  = rotor3all[1][0]
    huruf1.set(hurufrotor1)
    huruf2.set(hurufrotor2)
    huruf3.set(hurufrotor3)

                





        

        





label1 = tk.Label(window, text="Input", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
label1.grid(row=0, column=0,)
input1 = tk.Entry(window, width=60, borderwidth=5, bg="white", fg="black", font=("Arial", 10))
input1.grid(row=0, column=1,columnspan=2)
label2 = tk.Label(window, text="Plugin", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
label2.grid(row=1, column=0)
plugin1 = tk.Entry(window, width=60, borderwidth=5, bg="white", fg="black", font=("Arial", 10))
plugin1.grid(row=1, column=1,columnspan=2)

encripdecripbut = tk.Button(window, text="Enkripsi/Dekripsi", padx=10, pady=5, command=inputketext, bg="green", fg="white", font=("Arial", 10))
encripdecripbut.grid(row=2, column=1)

alanturingbut = tk.Button(window, text="Alan Turing", padx=10, pady=5, bg="green", fg="white", font=("Arial", 10), command=alan_turing)
alanturingbut.grid(row=2, column=2)

alan_turing_pluginbut = tk.Button(window, text="Alan Turing Plugin", padx=10, pady=5, bg="green", fg="white", font=("Arial", 10), command=alan_turing_plugin)
alan_turing_pluginbut.grid(row=2, column=0)


label3 = tk.Label(window, text="Input:", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
label3.grid(row=3, column=0)
inputtext = tk.Text(window, height=10, width=50, state="disabled", bg="white", fg="black", font=("Arial", 10))
inputtext.grid(row=3, column=1)

label4 = tk.Label(window, text="Output:", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
label4.grid(row=4, column=0)
outputtext = tk.Text(window, height=10, width=50, state="disabled", bg="white", fg="black", font=("Arial", 10))
outputtext.grid(row=4, column=1)

labelframe = tk.LabelFrame(window, text="Rincian", padx=10, pady=10, bg="#33FF99", fg="black", font=("Arial", 10))
labelframe.grid(row=0, column=3, rowspan=8, padx=10, pady=10,columnspan=2)
textrincian = tk.Text(labelframe, height=30, width=60, state="disabled", bg="white", fg="black", font=("Arial", 10))
textrincian.grid(row=0, column=3, rowspan=8, padx=10, pady=10,columnspan=2)

label5 = tk.Label(window, text="Left", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
label5.grid(row=6, column=0)

menurotor = ["I","II","III"]

#menu rotor left
menurotorleft = tk.StringVar()
menurotorleft.set("I")
rotorleft = tk.OptionMenu(window, menurotorleft, *menurotor)
rotorleft.grid(row=7, column=0)

huruf1 = tk.StringVar()
huruf1.set("A")
rotor1 = tk.OptionMenu(window, huruf1, *allhuruf)
rotor1.grid(row=8, column=0)


label6 = tk.Label(window, text="Middle", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
label6.grid(row=6, column=1)

menurotormiddle = tk.StringVar()
menurotormiddle.set("II")
rotormiddle = tk.OptionMenu(window, menurotormiddle, *menurotor)
rotormiddle.grid(row=7, column=1)

huruf2 = tk.StringVar()
huruf2.set("A")
rotor2 = tk.OptionMenu(window, huruf2, *allhuruf)
rotor2.grid(row=8, column=1)

label7 = tk.Label(window, text="Right", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
label7.grid(row=6, column=2)

menurotorright = tk.StringVar()
menurotorright.set("III")
rotorright = tk.OptionMenu(window, menurotorright, *menurotor)
rotorright.grid(row=7, column=2)


huruf3 = tk.StringVar()
huruf3.set("A")
rotor3 = tk.OptionMenu(window, huruf3, *allhuruf)
rotor3.grid(row=8, column=2)

pilihteliti = tk.Label(window, text="Alan Turing Teliti/Tidak", padx=10, pady=5, bg="#33FF99", fg="black", font=("Arial", 10))
pilihteliti.grid(row=8, column=3)

telititidak = ["Teliti","Tidak Teliti"]
teliti = tk.StringVar()
teliti.set("Tidak Teliti")
telitibut = tk.OptionMenu(window, teliti, *telititidak)
telitibut.grid(row=8, column=4)



window.mainloop()

