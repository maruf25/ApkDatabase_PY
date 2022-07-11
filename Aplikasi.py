import mysql.connector

cnt = mysql.connector.connect(database="tokoonline",username="root")
cursorObj = cnt.cursor()

def tablePelanggan():
    while True:
        print("""Pilih digunakan untuk tabel Pelanggan
        1. Insert
        2. Delete
        3. Update
        4. Select 
        5. Kembali (bisa pilih angka asal) \n""")
        pilih = int(input("Masukkan pilihan anda : "))
        print("\n")
        if pilih == 1:
            id_pelanggan = int(input("Masukkan id pelanggan : "))
            nama_pelanggan = str(input("Masukkan nama pelanggan : "))
            alamat = str(input("Masukkan alamat : "))
            query = """insert into pelanggan(id_pelanggan,nama_pelanggan,alamat) values(%s,%s,%s)"""
            data = (id_pelanggan,nama_pelanggan,alamat)
            cursorObj.execute(query,data)
            cnt.commit()
            print("Data berhasil ditambahkan")
        elif pilih == 2:
            x = input("Masukkan data attribut yang hendak dihapus : ")
            hapus = """delete from pelanggan where {}""".format(x)
            cursorObj.execute(hapus)
            cnt.commit()
            print("Hapus data berhasil")
        elif pilih == 3:
            x = input("Masukkan set entitas dan value : ")
            y = input("Masukkan where entitas dan value : ")
            update = "update pelanggan set {} where {}".format(x,y)
            cursorObj.execute(update)
            print("Update data berhasil")
        elif pilih == 4:
            query = """select * from pelanggan"""
            cursorObj.execute(query)
            result= cursorObj.fetchall()
            for i in result:
                print(i)
        else:
            break

def tableBarang():
    while True:
        print("""Pilih digunakan untuk tabel barang
        1. Insert
        2. Delete
        3. Update
        4. Select 
        5. Kembali (bisa pilih angka asal) \n""")
        pilih = int(input("Masukkan pilihan anda : "))
        print("\n")
        if pilih == 1:
            id_barang = int(input("Masukkan id barang : "))
            nama_barang = str(input("Masukkan nama barang : "))
            supllier = str(input("Masukkan nama supllier : "))
            query = """insert into barang(id_barang,nama_barang,supplier) values(%s,%s,%s)"""
            data = (id_barang,nama_barang,supllier)
            cursorObj.execute(query,data)
            cnt.commit()
            print("Data berhasil ditambahkan")
        elif pilih == 2:
            x = input("Masukkan data attribut yang hendak dihapus : ")
            hapus = """delete from barang where {}""".format(x)
            cursorObj.execute(hapus)
            cnt.commit()
            print("Hapus data berhasil")
        elif pilih == 3:
            x = input("Masukkan set entitas dan value : ")
            y = input("Masukkan where entitas dan value : ")
            update = "update barang set {} where {}".format(x,y)
            cursorObj.execute(update)
            print("Update data berhasil")
        elif pilih == 4:
            query = """select * from barang"""
            cursorObj.execute(query)
            result= cursorObj.fetchall()
            for i in result:
                print(i)
        else:
            break

def tableTransaksi():
    while True:
        print("""Pilih digunakan untuk tabel barang
        1. Insert
        2. Delete
        3. Update
        4. Select 
        5. Kembali (bisa pilih angka asal) \n""")
        pilih = int(input("Masukkan pilihan anda : "))
        print("\n")
        if pilih == 1:
            no_transaksi = int(input("Masukkan no transaksi : "))
            id_pelangganFK = str(input("Masukkan id pelanggan : "))
            id_barangFK = str(input("Masukkan id barang : "))
            tanggal = str(input("Masukkan tanggal format (YYYY-MM-DD) : "))
            query = """insert into transaksi(no_transaksi,id_pelangganFK,id_barangFK,tanggal) values(%s,%s,%s,%s)"""
            data = (no_transaksi,id_pelangganFK,id_barangFK,tanggal)
            cursorObj.execute(query,data)
            cnt.commit()
            print("Data berhasil ditambahkan")
        elif pilih == 2:
            x = input("Masukkan data attribut yang hendak dihapus : ")
            hapus = """delete from transaksi where {}""".format(x)
            cursorObj.execute(hapus)
            cnt.commit()
            print("Hapus data berhasil")
        elif pilih == 3:
            x = input("Masukkan set entitas dan value : ")
            y = input("Masukkan where entitas dan value : ")
            update = "update transaksi set {} where {}".format(x,y)
            cursorObj.execute(update)
            cnt.commit()
            print("Update data berhasil")
        elif pilih == 4:
            query = """select * from transaksi"""
            cursorObj.execute(query)
            result= cursorObj.fetchall()
            for i in result:
                print(i)
        else:
            break

while True:
    print("""Pilih Table
    1. Pelanggan
    2. Barang
    3. Transaksi \n""")
    pilih = int(input("Masukkan pilihan anda : "))
    print("\n")
    if pilih == 1:
        tablePelanggan()
    elif pilih == 2:
        tableBarang()
    elif pilih == 3:
        tableTransaksi()
    else:
        break

cnt.close()
cursorObj.close()

####Update
# query = """update barang set nama_barang="Oreo" where id_barang= 2"""
# cursorObj.execute(query)
# cnt.commit()
# cursorObj.close()

###Select
# query = """select * from barang"""
# cursorObj.execute(query)
# result= cursorObj.fetchall()
# for i in result:
#     print(i)
# cursorObj.close()

###Delete
# query = """delete from barang where id_barang=2"""
# cursorObj.execute(query)
# cnt.commit()
# cursorObj.close()

###Insert
# query = """insert into barang(id_barang,nama_barang,supplier) values(2,"Teh Pucuk","PT.Teh Pucuk")"""
# cursorObj.execute(query)
# cnt.commit()
# cursorObj.close()
