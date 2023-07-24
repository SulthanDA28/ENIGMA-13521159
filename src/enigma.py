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
def buangspasi(teks):
    hasil = ""
    for i in range(len(teks)):
        if(teks[i]!=" "):
            hasil+=teks[i]
    return hasil
def alan_turing_plugin(teks):
    teks = buangspasi(teks)
    cribs = "HELLOSUDO"
    listallhuruf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    reflector = [list("YRUHQSLDPXNGOKMIEBFZCWVJAT"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
    jml = 0
    hasilakhirbanget = []
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
                        for m in range(len(cribs)):
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
                                    if(hasil0==cribs[m]):
                                        huruflarang+=cribs[m]
                                    else:
                                        plugin+=hasil0+cribs[m]+" "
                                elif(m>0 and m<len(cribs)-1):
                                    if(cribs[m] in plugin):
                                        hasil1, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(cribs[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
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
                                        if(hasil1==cribs[m]):
                                            huruflarang+=cribs[m]
                                        else:
                                            if(hasil1 in huruflarang or cribs[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil1+cribs[m]+" "
                                                huruflarang+=cribs[m]+hasil1
                                elif(m==len(cribs)-1):
                                    if(cribs[m] in plugin):
                                        hasil9, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(cribs[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
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
                                        if(hasil9==cribs[m]):
                                            huruflarang+=cribs[m]
                                            stop = True
                                        else:
                                            if(hasil9 in huruflarang or cribs[m] in huruflarang):
                                                huruflarang = ""
                                                plugin = ''
                                                break
                                            else:
                                                plugin+=hasil9+cribs[m]+" "
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
                    # if(hasilakhirbanget!=[]):
                    #     break
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
def alan_turing_plugin_teliti(teks):
    teks = buangspasi(teks)
    cribs = "HELLOSUDO"
    listallhuruf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    reflector = [list("YRUHQSLDPXNGOKMIEBFZCWVJAT"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
    jml = 0
    hasilakhirbanget = []
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
                plugin = ''
                huruflarangawal = ''
                
                while(True):
                    print(current_rotor)
                    print(hasilakhirbanget)
                    if(awal>1 and current_rotor=="AAA"):
                        break
                    huruflarang = ""
                    rotor1awal = copy.deepcopy(left)
                    rotor2awal = copy.deepcopy(mid)
                    rotor3awal = copy.deepcopy(right)
                    count = 0
                    plugin = ''
                    for z in range(len(cribs)):
                        plugin = ''
                        copysebelum1 = copy.deepcopy(rotor1awal)
                        copysebelum2 = copy.deepcopy(rotor2awal)
                        copysebelum3 = copy.deepcopy(rotor3awal)
                        if(rotor2awal[1][0]==notchmid and rotor3awal[1][0]==notchright):
                            nextrotor(rotor1awal)
                            nextrotor(rotor2awal)
                            nextrotor(rotor3awal)
                        elif(rotor2awal[1][0]==notchmid):
                            nextrotor(rotor1awal)
                            nextrotor(rotor2awal)
                            nextrotor(rotor3awal)
                        elif(rotor3awal[1][0]==notchright):
                            nextrotor(rotor3awal)
                            nextrotor(rotor2awal)
                        else:
                            nextrotor(rotor3awal)
                        hasilawal, r1,r2,r3,r4,r5,r6,r7 = enigma(cribs[z],listallhuruf,rotor3awal,rotor2awal,rotor1awal,reflector)
                        if(hasilawal==teks[z]):
                            huruflarangawal+=teks[z]+cribs[z]
                            count+=1
                        else:
                            break
                    if(count==len(cribs)):
                        hasilakhirbanget.append([current_rotor,str(i+1),str(j+1),str(k+1),plugin])
                        print("Masuk sini")
                    else:
                        plugin = ''
                        for a in range(26):
                            huruflarang = huruflarangawal
                            plugin = ''
                            rotor1 = copy.deepcopy(copysebelum1)
                            rotor2 = copy.deepcopy(copysebelum2)
                            rotor3 = copy.deepcopy(copysebelum3)
                            stop = False
                            for m in range(count,len(cribs)):
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
                                    if(m==count):
                                        hasil0, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                        if(hasil0==cribs[m]):
                                            huruflarang+=cribs[m]+teks[m]
                                        else:
                                            if(hasil0 in huruflarang or cribs[m] in huruflarang):
                                                break
                                            else:
                                                plugin+=hasil0+cribs[m]+" "
                                                huruflarang+=cribs[m]+hasil0+teks[m]
                                    elif(m>count and m<len(cribs)-1):
                                        if(cribs[m] in plugin):
                                            hasil1, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(cribs[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                            if(hasil1==teks[m]):
                                                huruflarang+=teks[m]+cribs[m]
                                            else:
                                                if(hasil1 in huruflarang or teks[m] in huruflarang):
                                                    break
                                                else:
                                                    plugin+=hasil1+teks[m]+" "
                                                    huruflarang+=teks[m]+hasil1+cribs[m]
                                        else:
                                            hasil1, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                            if(hasil1==cribs[m]):
                                                huruflarang+=cribs[m]+teks[m]
                                            else:
                                                if(hasil1 in huruflarang or cribs[m] in huruflarang):
                                                    break
                                                else:
                                                    plugin+=hasil1+cribs[m]+" "
                                                    huruflarang+=cribs[m]+hasil1+teks[m]
                                    elif(m==len(cribs)-1):
                                        if(cribs[m] in plugin):
                                            hasil9, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(cribs[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                            if(hasil9==teks[m]):
                                                huruflarang+=teks[m]+cribs[m]
                                                stop = True
                                            else:
                                                if(hasil9 in huruflarang or teks[m] in huruflarang):
                                                    break
                                                else:
                                                    plugin+=hasil9+teks[m]+" "
                                                    stop = True
                                        else:
                                            hasil9, r11, r21, r31, rf, r32, r22, r12,pluginawal = enigma_plugin(teks[m],plugin,listallhuruf,rotor3,rotor2,rotor1,reflector)
                                            if(hasil9==cribs[m]):
                                                huruflarang+=cribs[m]+teks[m]
                                                stop = True
                                            else:
                                                if(hasil9 in huruflarang or cribs[m] in huruflarang):
                                                    break
                                                else:
                                                    plugin+=hasil9+cribs[m]+" "
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
                    # if(hasilakhirbanget!=[]):
                    #     break
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
# coba2 = alan_turing_plugin_test("RCXPV NSWX")
# print(coba)
# print(coba2)
# end = time.time()
# print(coba)
# print("Waktu eksekusi: ",end-start," detik")






                        









    
                






