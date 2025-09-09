#inputan
nama=input("Inputkan nama panggilan anda : ")
Nama=input("Inputkan nama lengkap anda : ")
print("Nama Panggilan : ",nama)
print("Nama Lengkap : ",Nama)

#deklarasi variabel
var_bil_bulat=10
var_bil_desimal=3.14
var_text="Agus"
var_bool=True
#cetak jenis variabel
print(type(var_bil_bulat))
print(type(var_bil_desimal))
print(type(var_text))
print(type(var_text))
#operator aritmatika

#operator pembanding

#operator Logika

#operator Penugasan
a=int(input("inputkan nilai a : "))
#a=a-5 di tulis dalam program seperti berikut
a-=5
print(a)

#percabangan
b=int(input("inputkan nilai b : "))
c=int(input("inputkan nilai c : "))
if b>c:
    print("b lebih besar dari pada c")
else:
    print("c lebih besar dari pada b")
    
nilai=int(input("inputkan nilai : "))
if nilai<50:
    print("Nilai E")
elif nilai<65:
    print("Nilai D")
elif nilai<75:
    print("Nilai C")
elif nilai<87:
    print("Nilai B")
else:
    print("Nilai A")

jml_belanja=int(input("Inputkan jumlah barang : "))
harga=int(input("Inputkan harga : "))
diskon=int(input("Inputkan diskon : "))
tot_harga=jml_belanja*harga
hitung_diskon=(tot_harga*diskon)/100
tot_bayar=tot_harga-hitung_diskon
#print("Jumlah Barang : ",jml_belanja)
#print("Harga Barang : ", harga)
#print("Jumlah Diskon : ", diskon,"%")
#print("Jumlah Total Bayar : ",tot_harga)
#print("Jumlah diskon : ",hitung_diskon)
#print("Jumlah Total Bayar setelah diskon : ",hitung_diskon)
if jml_belanja>5:
    print("Bonus 1 Barang")
    #print("Jumlah Total Bayar : ",tot_harga)
    if tot_harga>50000:
        print("Selamat Anda Dapat diskon : ", diskon,"%")
        print("Total Pembayaran : ",tot_bayar)
    else:
        print("Anda Tidak dapat diskon")
        print("Total Pembayaran : ",tot_harga)
else:
    print("Anda Tidak dapat bonus dan diskon")

#perulangan
for var in range(10):
    print("Nama", var)
    
    
    #def function_name(parameters):
    #"""docstring/Komentar"""
    #statemen
    
    
    