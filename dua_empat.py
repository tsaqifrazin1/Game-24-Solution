def menginisiasiOperasi (angka1,angka2):
    hasil = []
    for a in range(angka1, angka2):
        for b in range(angka1,angka2):
            for c in range(angka1,angka2):
                hasil.append([a,b,c])
    return hasil

def hasilGame24 (angka1,angka2,angka3,angka4):
    operasi = menginisiasiOperasi(0,4)
    listHasilAkhir = []
    operasiHasilAkhir = []
    for i in range(0,len(operasi)):
        n = operasi [i] [0]
        m = operasi [i] [1]
        o = operasi [i] [2]
        if n == 0:
            hasilAkhir = angka1*angka2
        if n == 1:
            hasilAkhir = angka1/angka2
        if n == 2:
            hasilAkhir = angka1+angka2
        elif n == 3:
            hasilAkhir = angka1-angka2
        if m == 0:
            hasilAkhir = hasilAkhir*angka3
        if m == 1:
            hasilAkhir = hasilAkhir/angka3
        if m == 2:
            hasilAkhir = hasilAkhir+angka3
        elif m == 3:
            hasilAkhir = hasilAkhir-angka3
        if o == 0:
            hasilAkhir = hasilAkhir*angka4
        if o == 1:
            hasilAkhir = hasilAkhir/angka4
        if o == 2:
            hasilAkhir = hasilAkhir+angka4
        elif o == 3:
            hasilAkhir = hasilAkhir-angka4
        listHasilAkhir.append(hasilAkhir)
        if hasilAkhir == 24:
            operasiHasilAkhir.append([n,m,o])
        for i in range(0,len(operasiHasilAkhir)):
            for j in range(0,len(operasiHasilAkhir[i])):
                if operasiHasilAkhir[i][j] == 0:
                    operasiHasilAkhir[i][j] = '*'
                elif operasiHasilAkhir[i][j] == 1:
                    operasiHasilAkhir[i][j] = '/'
                elif operasiHasilAkhir[i][j] == 2:
                    operasiHasilAkhir[i][j]= '+'
                elif operasiHasilAkhir[i][j] == 3:
                    operasiHasilAkhir[i][j] = '-'
    output = ''
    if len(operasiHasilAkhir) > 0:
        output = '{},{},{},{} menghasilkan nilai 24 dengan cara\n'.format(angka1,angka2,angka3,angka4)
        for i in range(0,len(operasiHasilAkhir)):
            output = output + " - {} {} {} {} {} {} {}\n".format(angka1,operasiHasilAkhir[i][0],angka2,operasiHasilAkhir[i][1],angka3,operasiHasilAkhir[i][2],angka4)
    return output, len(operasiHasilAkhir)

    

def mengacakAngka (angka1,angka2,angka3,angka4):
    hasil = [angka1, angka2, angka3, angka4]
    hasiltotal = []
    for a in range(0, len(hasil)):
        for b in range(0,len(hasil)):
            if b == a:
                continue
            for c in range(0,len(hasil)):
                if c == b:
                    continue
                if c == a:
                    continue
                for d in range(0,len(hasil)):
                    if d == a:
                        continue
                    if d == b:
                        continue
                    if d == c:
                        continue
                    hasiltotal.append([a,b,c,d])
    hasilakhir = hasiltotal
    for i in range(0,len(hasilakhir)):
        for j in range(0,len(hasilakhir[i])):
            if hasilakhir[i][j] == 0:
                hasilakhir[i][j] = angka1
            elif hasilakhir[i][j] == 1:
                hasilakhir[i][j] = angka2
            elif hasilakhir[i][j] == 2:
                hasilakhir[i][j]= angka3
            elif hasilakhir[i][j] == 3:
                hasilakhir[i][j] = angka4
    return hasilakhir

def menampilkanhasil(angka1,angka2,angka3,angka4):
    a = mengacakAngka(angka1,angka2,angka3,angka4)
    jumlah = 0
    informasi = ''
    for i in range(0, len(a)):
        try:
            output, total = hasilGame24(a[i][0], a[i][1], a[i][2], a[i][3])
            informasi = informasi + output  
            jumlah = jumlah + total
            
        except:
            pass
    return informasi, jumlah







        