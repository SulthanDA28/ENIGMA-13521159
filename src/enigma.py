import copy
import time
def nextrotor(rotor):
    ambil1 = rotor[0].pop(0)
    rotor[0].append(ambil1)
    ambil2 = rotor[1].pop(0)
    rotor[1].append(ambil2)

def gethuruf(huruf,list):
    for i in range(len(list)):
        if(list[i] == huruf):
            return i
def makeplugin(sambung):
    sambung = sambung.upper()
    cek = []
    buatcek = list(sambung)
    for i in range(len(buatcek)):
        if(buatcek[i] == " "):
            continue
        elif(buatcek[i] not in cek):
            cek.append(buatcek[i])
        elif(buatcek[i] in cek):
            return "Error"
    pisah = sambung.split(" ")
    ambil = []
    for i in range(len(pisah)):
        if(pisah[i] != ""):
            ambil.append(pisah[i])
            if(len(pisah[i]) != 2):
                return "Error"
    hasil = []
    for i in range(len(ambil)):
        masuk1 = []
        masuk1.append(ambil[i][0])
        masuk1.append(ambil[i][1])
        masuk2 = []
        masuk2.append(ambil[i][1])
        masuk2.append(ambil[i][0])
        hasil.append(masuk1)
        hasil.append(masuk2)
    return hasil
def enigma(huruf,listhuruf,rotor1,rotor2,rotor3,reflector):
    index1 = gethuruf(huruf,listhuruf)
    hurufrotor1ke1 = rotor1[0][index1]
    indexrotor1ke1 = gethuruf(hurufrotor1ke1,rotor1[1])
    hurufrotor2ke1 = rotor2[0][indexrotor1ke1]
    indexrotor2ke1 = gethuruf(hurufrotor2ke1,rotor2[1])
    hurufrotor3ke1 = rotor3[0][indexrotor2ke1]
    indexrotor3ke1 = gethuruf(hurufrotor3ke1,rotor3[1])
    hurufreflector = reflector[0][indexrotor3ke1]
    indexreflector = gethuruf(hurufreflector,reflector[1])
    hurufrotor3ke2 = rotor3[1][indexreflector]
    indexrotor3ke2 = gethuruf(hurufrotor3ke2,rotor3[0])
    hurufrotor2ke2 = rotor2[1][indexrotor3ke2]
    indexrotor2ke2 = gethuruf(hurufrotor2ke2,rotor2[0])
    hurufrotor1ke2 = rotor1[1][indexrotor2ke2]
    indexrotor1ke2 = gethuruf(hurufrotor1ke2,rotor1[0])
    hurufakhir = listhuruf[indexrotor1ke2]
    
    return hurufakhir, listhuruf[indexrotor1ke1], listhuruf[indexrotor2ke1], listhuruf[indexrotor3ke1], listhuruf[indexreflector], listhuruf[indexrotor3ke2], listhuruf[indexrotor2ke2], listhuruf[indexrotor1ke2]
def enigma_plugin(huruf,plugin,listhuruf,rotor1,rotor2,rotor3,reflector):
    ubahplugin = makeplugin(plugin)
    if(ubahplugin == "Error"):
        print("Plugin tidak valid")
        return "Error", "Error", "Error", "Error", "Error", "Error", "Error", "Error", "Error"
    else:
        pluginawal = huruf
        for i in range(len(ubahplugin)):
            if(huruf == ubahplugin[i][0]):
                pluginawal = ubahplugin[i][1]
                break
        hasilenigma,r11,r21,r31,rf,r32,r22,r12 = enigma(pluginawal,listhuruf,rotor1,rotor2,rotor3,reflector)
        hasilakhir = hasilenigma
        for i in range(len(ubahplugin)):
            if(hasilenigma == ubahplugin[i][1]):
                hasilakhir = ubahplugin[i][0]
                break
        return hasilakhir, r11, r21, r31, rf, r32, r22, r12,pluginawal
    
def alan_turing(teks):
    hasilakhirbanget = []
    listallhuruf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    reflector = [list("YRUHQSLDPXNGOKMIEBFZCWVJAT"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
    jml = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                jml+=1
                if(i==0):
                    left = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchleft = "Q"
                elif(i==1):
                    left = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchleft = "E"
                elif(i==2):
                    left = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchleft = "V"
                if(j==0):
                    mid =[list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")] 
                    notchmid = "Q"
                elif(j==1):
                    mid = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchmid = "E"
                elif(j==2):
                    mid = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchmid = "V"
                if(k==0):
                    right = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchright = "Q"
                elif(k==1):
                    right = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchright = "E"
                elif(k==2):
                    right = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchright = "V"
                awal = 0
                current_rotor = "AAA"
                stop = False
                while(True):
                    print(current_rotor)
                    if(awal>1 and current_rotor=="AAA"):
                        break
                    rotor1 = copy.deepcopy(left)
                    rotor2 = copy.deepcopy(mid)
                    rotor3 = copy.deepcopy(right)
                    for m in range(len(teks)):
                        if(teks[m]==" "):
                            continue
                        else:
                            if(rotor2[1][0]==notchmid and rotor3[1][0]==notchright):
                                nextrotor(rotor1)
                                nextrotor(rotor2)
                                nextrotor(rotor3)
                            elif(rotor2[1][0]==notchmid):
                                nextrotor(rotor1)
                                nextrotor(rotor2)
                                nextrotor(rotor3)
                            elif(rotor3[1][0]==notchright):
                                nextrotor(rotor3)
                                nextrotor(rotor2)
                            else:
                                nextrotor(rotor3)
                            hasil, r11, r21, r31, rf, r32, r22, r12 = enigma(teks[m],listallhuruf,rotor3,rotor2,rotor1,reflector)
                            if(m==0 and hasil=="H"):
                                continue
                            elif(m==1 and hasil=="E"):
                                continue
                            elif(m==2 and hasil=="L"):
                                continue
                            elif(m==3 and hasil=="L"):
                                continue
                            elif(m==4 and hasil=="O"):
                                continue
                            elif(m==6 and hasil=="S"):
                                continue
                            elif(m==7 and hasil=="U"):
                                continue
                            elif(m==8 and hasil=="D"):
                                continue
                            elif(m==9 and hasil=="O"):
                                stop = True
                                break
                            else:
                                stop = False
                                break
                    if(stop==True):
                        print("Hasil akhir: ",current_rotor,str(i+1),str(j+1),str(k+1))

                        hasilakhir = [current_rotor,str(i+1),str(j+1),str(k+1)]
                        hasilakhirbanget.append(hasilakhir)
                        break
                    else:
                        awal+=1
                        if(mid[1][0]==notchmid and right[1][0]==notchright):
                            nextrotor(left)
                            nextrotor(mid)
                            nextrotor(right)
                        elif(mid[1][0]==notchmid):
                            nextrotor(left)
                            nextrotor(mid)
                            nextrotor(right)
                        elif(right[1][0]==notchright):
                            nextrotor(right)
                            nextrotor(mid)
                        else:
                            nextrotor(right)
                        current_rotor = left[1][0]+mid[1][0]+right[1][0]
                print("Jumlah percobaan: ",jml)
                print("Hasil akhir: ",hasilakhirbanget)
                if(hasilakhirbanget!=[]):
                    break
            if(hasilakhirbanget!=[]):
                break
        if(hasilakhirbanget!=[]):
            break
    if(hasilakhirbanget==[]):
        return "None"
    else:
        return hasilakhirbanget
def alan_turing_plugin(teks):
    listallhuruf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    reflector = [list("YRUHQSLDPXNGOKMIEBFZCWVJAT"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
    jml = 0
    hasilakhirbanget = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=2 or j!=2 or k!=2):
                    continue
                jml+=1
                if(i==0):
                    left = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchleft = "Q"
                elif(i==1):
                    left = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchleft = "E"
                elif(i==2):
                    left = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchleft = "V"
                if(j==0):
                    mid =[list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")] 
                    notchmid = "Q"
                elif(j==1):
                    mid = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchmid = "E"
                elif(j==2):
                    mid = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchmid = "V"
                if(k==0):
                    right = [list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchright = "Q"
                elif(k==1):
                    right = [list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchright = "E"
                elif(k==2):
                    right = [list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
                    notchright = "V"
                awal = 0
                current_rotor = "AAA"
                plugin = ''
                
                while(True):
                    print(current_rotor)
                    if(awal>1 and current_rotor=="AAA"):
                        break
                    plugin = ''
                    for a in range(26):
                        huruflarang = ""
                        plugin = ''
                        rotor1 = copy.deepcopy(left)
                        rotor2 = copy.deepcopy(mid)
                        rotor3 = copy.deepcopy(right)
                        stop = False
                        for m in range(10):
                            if(teks[m]==" "):
                                continue
                            else:
                                if(rotor2[1][0]==notchmid and rotor3[1][0]==notchright):
                                    nextrotor(rotor1)
                                    nextrotor(rotor2)
                                    nextrotor(rotor3)
                                elif(rotor2[1][0]==notchmid):
                                    nextrotor(rotor1)
                                    nextrotor(rotor2)
                                    nextrotor(rotor3)
                                elif(rotor3[1][0]==notchright):
                                    nextrotor(rotor3)
                                    nextrotor(rotor2)
                                else:
                                    nextrotor(rotor3)
                                if(plugin==''):
                                    plugin+=teks[m]+listallhuruf[a]+" "
                                if(makeplugin(plugin)=="Error"):
                                    break
                                if(m==0):
                                    hasil0, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                    if(hasil0=="H"):
                                        huruflarang+="H"
                                    else:
                                        plugin+=hasil0+"H"+" "
                                elif(m==1):
                                    if("E" in plugin):
                                        hasil1, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("E",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil1==teks[m]):
                                            huruflarang+=teks[m]
                                        else:
                                            if(hasil1 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil1+teks[m]+" "
                                                huruflarang+=teks[m]+hasil1
                                    else:
                                        hasil1, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil1=="E"):
                                            huruflarang+="E"
                                        else:
                                            if(hasil1 in huruflarang or "E" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil1+"E"+" "
                                                huruflarang+="E"+hasil1
                                elif(m==2):
                                    if("L" in plugin):
                                        hasil2, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("L",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil2==teks[m]):
                                            huruflarang+=teks[m]
                                        else:
                                            if(hasil2 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil2+teks[m]+" "
                                                huruflarang+=teks[m]+hasil2
                                    else:
                                        hasil2, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil2=="L"):
                                            huruflarang+="L"
                                        else:
                                            if(hasil2 in huruflarang or "L" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil2+"L"+" "
                                                huruflarang+="L"+hasil2
                                elif(m==3):
                                    if("L" in plugin):
                                        hasil3, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("L",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil3==teks[m]):
                                            huruflarang+=teks[m]
                                        else:
                                            if(hasil3 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil3+teks[m]+" "
                                                huruflarang+=teks[m]+hasil3
                                    else:
                                        hasil3, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil3=="L"):
                                            huruflarang+="L"
                                        else:
                                            if(hasil3 in huruflarang or "L" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil3+"L"+" "
                                                huruflarang+="L"+hasil3
                                elif(m==4):
                                    if("O" in plugin):
                                        hasil4, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("O",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil4==teks[m]):
                                            huruflarang+=teks[m]
                                        else:
                                            if(hasil4 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil4+teks[m]+" "
                                                huruflarang+=teks[m]+hasil4
                                    else:
                                        hasil4, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil4=="O"):
                                            huruflarang+="O"
                                        else:
                                            if(hasil4 in huruflarang or "O" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil4+"O"+" "
                                                huruflarang+="O"+hasil4
                                elif(m==6):
                                    if("S" in plugin):
                                        hasil6, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("S",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil6==teks[m]):
                                            huruflarang+=teks[m]
                                        else:
                                            if(hasil6 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil6+teks[m]+" "
                                                huruflarang+=teks[m]+hasil6
                                    else:
                                        hasil6, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil6=="S"):
                                            huruflarang+="S"
                                        else:
                                            if(hasil6 in huruflarang or "S" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil6+"S"+" "
                                                huruflarang+="S"+hasil6
                                elif(m==7):
                                    if("U" in plugin):
                                        hasil7, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("U",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil7==teks[m]):
                                            huruflarang+=teks[m]
                                        else:
                                            if(hasil7 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil7+teks[m]+" "
                                                huruflarang+=teks[m]+hasil7
                                    else:
                                        hasil7, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil7=="U"):
                                            huruflarang+="U"
                                        else:
                                            if(hasil7 in huruflarang or "U" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil7+"U"+" "
                                                huruflarang+="U"+hasil7
                                elif(m==8):
                                    if("D" in plugin):
                                        hasil8, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("D",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil8==teks[m]):
                                            huruflarang+=teks[m]
                                        else:
                                            if(hasil8 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil8+teks[m]+" "
                                                huruflarang+=teks[m]+hasil8
                                    else:
                                        hasil8, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil8=="D"):
                                            huruflarang+="D"
                                        else:
                                            if(hasil8 in huruflarang or "D" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil8+"D"+" "
                                                huruflarang+="D"+hasil8
                                elif(m==9):
                                    if("O" in plugin):
                                        hasil9, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin("O",plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil9==teks[m]):
                                            huruflarang+=teks[m]
                                            stop = True
                                        else:
                                            if(hasil9 in huruflarang or teks[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil9+teks[m]+" "
                                                stop = True
                                    else:
                                        hasil9, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil9=="O"):
                                            huruflarang+="O"
                                            stop = True
                                        else:
                                            if(hasil9 in huruflarang or "O" in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil9+"O"+" "
                                                stop = True
                                
                                if(makeplugin(plugin)=="Error"):
                                    break
                                else:
                                    continue
                        if(stop==True and makeplugin(plugin)!="Error"):
                            hasilcuuy = [current_rotor,str(i+1),str(j+1),str(k+1),plugin]
                            hasilakhirbanget.append(hasilcuuy)
                        else:
                            continue  
                    awal+=1
                    if(mid[1][0]==notchmid and right[1][0]==notchright):
                        nextrotor(left)
                        nextrotor(mid)
                        nextrotor(right)
                    elif(mid[1][0]==notchmid):
                        nextrotor(left)
                        nextrotor(mid)
                        nextrotor(right)
                    elif(right[1][0]==notchright):
                        nextrotor(right)
                        nextrotor(mid)
                    else:
                        nextrotor(right)
                    current_rotor = left[1][0]+mid[1][0]+right[1][0]
                    
                if(hasilakhirbanget!=[]):
                    break
            if(hasilakhirbanget!=[]):
                break
        if(hasilakhirbanget!=[]):
            break
    if(hasilakhirbanget==[]):
        return "None"
    else:
        return hasilakhirbanget
# start = time.time()
# # coba = alan_turing("KQVHS IPCC")
# coba= alan_turing_plugin("RCXPV NSWX")
# end = time.time()
# print(coba)
# print("Waktu eksekusi: ",end-start," detik")






                        









    
                






