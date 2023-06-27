print("=======================SELAMAT DATANG DI MELA COSMETIC=======================")
print("")
data_product ={
    1:"Bedak ",
    2:"Foundation ",
    3:"Lipcream",
    4:"Eyeshadow",
    5:"Eyeliner",
}
daftar_harga ={
    1: 45000,
    2: 50000,
    3: 25000, 
    4: 35000,
    5: 20000,
}

dict_trx = {}
daftar_metode_pembayaran ={
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash on Delivery",
    4:"Kartu Kredit",
}
print("=========================LIST PRODUCT=============================")
for i in data_product:
    print("Id Product :",i,"\t Nama Product :",data_product[i],"\t Harga Product : ",daftar_harga[i])

pilih_id =int(input("Pilih Id Product :"))
if pilih_id in data_product :
    pilih_beli = input("Ingin Beli ? (Y/N): ")
    if pilih_beli =="y" or pilih_beli =="Y":
        jml_produk       =int(input("Jumlah Pembelian :"))
        nama_penerima    = input("Nama Penerima :")
        alamat_penerima  = input("Alamat Penerima :")
        telepon          = input("No Hp :")
        kurir_pengiriman = input("Kurir Pengiriman :")
        dict_trx ={
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "No Hp":telepon,
            "Kurir Pengiriman":kurir_pengiriman,
            "product id":data_product,
}
else:
    pass
if len (dict_trx) > 0 :
    print ("========================== METODE PEMBAYARAN ==========================")
for i in daftar_metode_pembayaran:
    print("Id : ", i, "\t Metode Pembayaran :", daftar_metode_pembayaran[i])
pilih_metode =int(input("Pilih Id Metode Pembayaran : "))
if pilih_metode in daftar_metode_pembayaran :
    print("Nama Penerima : ", dict_trx["nama penerima"])
    print("Alamat Penerima : ", dict_trx["alamat penerima"])
    print("No Hp : ", dict_trx["No Hp"])
    print("Kurir Pengiriman : ", dict_trx["Kurir Pengiriman"])
    print("Product : ", data_product[pilih_id])
    print("Harga : ", daftar_harga[pilih_id])
    print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
    konfirmasi =input("Apakah and Yakin Ingin Melakukan Pembayaran? (Y/N) : ")
    if konfirmasi == "y" or konfirmasi == "Y":
        print("silahkan lakukan pembayaran anda")
    else:
        pass
else:
    print("Id Metode Pembayaran tidak Tersedia")

jml_produk = int(input("Masukkan Jumlah Pembelian: "))
total = jml_produk * daftar_harga[pilih_id]
print("Total yang harus anda bayar=Rp. ",total)
bayar = int(input("Uang anda = Rp. "))
kembalian = bayar - total
print("kembalian:",kembalian)

print("")
print("===============TERIMA KASIH SUDAH BERBELANJA DI TOKO KAMI==================")
