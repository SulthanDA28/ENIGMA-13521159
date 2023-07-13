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
        return "Error"
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
                






