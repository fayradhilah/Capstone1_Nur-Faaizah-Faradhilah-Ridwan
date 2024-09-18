import getpass
from prettytable import PrettyTable
import re

print('=== SELAMAT DATANG DI LAYANAN YELLOW PAGES ===')

def login():
    print('\n1. Masuk Sebagai User')
    print('2. Masuk Sebagai Admin')

    login_option = input('\nPilih opsi Log In (1/2) : ')

    if login_option == '1':
        print('Anda Masuk Sebagai User')
        menu_utama_user()
    elif login_option == '2':
        print('Anda Masuk Sebagai Admin')
        admin_login()
    else:
        print('Opsi Tidak Valid.')
        login()

def admin_login():
    correct_username = 'admin'
    correct_password = '1234'

    username_admin = input('Masukkan Username Anda: ').lower()
    password_admin = getpass.getpass('Masukkan Password Anda: ')

    if username_admin == correct_username and password_admin == correct_password:
        print('Log In Berhasil!')
        menu_utama_admin()
    else:
        print('Username atau Password Anda Salah! Silahkan Log In Ulang.')
        login()

# Admin's Service
list_layanan = [
    '\n===== MENU UTAMA ADMIN =====',
    '1. Mencari Daftar Kontak',
    '2. Menambah Kontak',
    '3. Edit Kontak',
    '4. Menghapus Kontak',
    '5. Menampilkan Seluruh Kontak'
    '6. Exit',
]

def menu_utama_admin():
    while True:
        print('\n===== LAYANAN =====')
        print('1. Mencari Daftar Kontak')
        print('2. Menambah Kontak')
        print('3. Edit Kontak')
        print('4. Menghapus Kontak')
        print('5. Menampilkan Seluruh Kontak')
        print('6. Exit')

        pilihan = input('Masukkan Layanan yang Ingin Dijalankan: ')

        if pilihan == '1':
            search_contact(daftar_Kontak, role='admin')
        elif pilihan == '2':
            new_contact(daftar_Kontak, kontak, kodeArea, provinsi1, kotaKabupaten)
        elif pilihan == '3':
            edit_contact()
        elif pilihan == '4':
            del_contact()
        elif pilihan == '5':
            all_contact(daftar_Kontak, showed_ID=True)
        elif pilihan == '6':
            print('Terima Kasih!')
            break
        else:
            print('Silahkan pilih antara 1 - 6')
            menu_utama_admin()

# User's Service
list_layanan_user = [
    '===== LAYANAN =====',
    '1. Mencari Daftar Kontak',
    '2. Menampilkan Seluruh Kontak',
    '3. Exit'
]

def menu_utama_user():
    while True:
        print('\n===== LAYANAN =====')
        print('1. Mencari Daftar Kontak')
        print('2. Menampilkan Seluruh Kontak')
        print('3. Exit')

        pilihan = input('Masukkan Layanan yang Ingin Dijalankan: ')

        if pilihan == '1':
            search_contact(daftar_Kontak, role='user')
        elif pilihan == '2':
            all_contact(daftar_Kontak, showed_ID=False)
        elif pilihan == '3':
            print('Terima Kasih!')
            break
        else:
            print('Silahkan pilih antara 1 - 3')
            menu_utama_user()

# Daftar Tabel Kontak
daftar_Kontak = [
    {'ID': 'ID001', 'NAMA': 'PT MAJU SEJAHTERA', 'BIDANG BISNIS': 'Perdagangan', 'ALAMAT': 'Jl. Merdeka No.1', 'DESA/KELURAHAN': 'Gambir', 'KECAMATAN': 'Gambir', 'KOTA/KABUPATEN': 'Jakarta Pusat', 'PROVINSI': 'DKI JAKARTA', 'KODE AREA': '021', 'NO. TELEPON': '1234567'},
    {'ID': 'ID002', 'NAMA': 'CV SUKSES ABADI', 'BIDANG BISNIS': 'Konstruksi', 'ALAMAT': 'Jl. Sukabumi No.10', 'DESA/KELURAHAN': 'Bojong Gede', 'KECAMATAN': 'Bojong Gede', 'KOTA/KABUPATEN': 'Bogor', 'PROVINSI': 'JAWA BARAT', 'KODE AREA': '0251', 'NO. TELEPON': '7654321'},
    {'ID': 'ID003', 'NAMA': 'UD JAYA MANDIRI', 'BIDANG BISNIS': 'Kuliner', 'ALAMAT': 'Jl. Raya Sawangan No.25', 'DESA/KELURAHAN': 'Pancoran Mas', 'KECAMATAN': 'Pancoran Mas', 'KOTA/KABUPATEN': 'Depok', 'PROVINSI': 'JAWA BARAT', 'KODE AREA': '021', 'NO. TELEPON': '9876543'},
    {'ID': 'ID004', 'NAMA': 'TOKO HARAPAN', 'BIDANG BISNIS': 'Ritel', 'ALAMAT': 'Jl. Daan Mogot No.55', 'DESA/KELURAHAN': 'Ciledug', 'KECAMATAN': 'Ciledug', 'KOTA/KABUPATEN': 'Tangerang', 'PROVINSI': 'BANTEN', 'KODE AREA': '021', 'NO. TELEPON': '8765432'},
    {'ID': 'ID005', 'NAMA': 'PT BINA USAHA', 'BIDANG BISNIS': 'Jasa Keuangan', 'ALAMAT': 'Jl. Cut Meutia No.12', 'DESA/KELURAHAN': 'Bekasi Timur', 'KECAMATAN': 'Bekasi Timur', 'KOTA/KABUPATEN': 'Bekasi', 'PROVINSI': 'JAWA BARAT', 'KODE AREA': '021', 'NO. TELEPON': '6543210'},
    {'ID': 'ID006', 'NAMA': 'HARAPAN JAYA', 'BIDANG BISNIS': 'Ritel', 'ALAMAT': 'Jl. Daan Mogot No.13', 'DESA/KELURAHAN': 'Ciledug', 'KECAMATAN': 'Ciledug', 'KOTA/KABUPATEN': 'Tangerang', 'PROVINSI': 'BANTEN', 'KODE AREA': '021', 'NO. TELEPON': '8901234'},
    {'ID': 'ID007', 'NAMA': 'PT CIPTA KARYA', 'BIDANG BISNIS': 'Properti', 'ALAMAT': 'Jl. M.H. Thamrin No.35', 'DESA/KELURAHAN': 'Menteng', 'KECAMATAN': 'Menteng', 'KOTA/KABUPATEN': 'Jakarta Pusat', 'PROVINSI': 'DKI JAKARTA', 'KODE AREA': '021', 'NO. TELEPON': '1234578'},
    {'ID': 'ID008', 'NAMA': 'UD ANEKA RASA', 'BIDANG BISNIS': 'Kuliner', 'ALAMAT': 'Jl. Raya Lenteng Agung No.77', 'DESA/KELURAHAN': 'Jagakarsa', 'KECAMATAN': 'Jagakarsa', 'KOTA/KABUPATEN': 'Jakarta Selatan', 'PROVINSI': 'DKI JAKARTA', 'KODE AREA': '021', 'NO. TELEPON': '8765431'},
    {'ID': 'ID009', 'NAMA': 'CV MEGAH JAYA', 'BIDANG BISNIS': 'Logistik', 'ALAMAT': 'Jl. Raya Bogor KM 24', 'DESA/KELURAHAN': 'Cibubur', 'KECAMATAN': 'Ciracas', 'KOTA/KABUPATEN': 'Jakarta Timur', 'PROVINSI': 'DKI JAKARTA', 'KODE AREA': '021', 'NO. TELEPON': '5678912'},
    {'ID': 'ID010', 'NAMA': 'PT MULTI USAHA', 'BIDANG BISNIS': 'Teknologi Informasi', 'ALAMAT': 'Jl. BSD Raya No.101', 'DESA/KELURAHAN': 'Serpong', 'KECAMATAN': 'Serpong', 'KOTA/KABUPATEN': 'Tangerang Selatan', 'PROVINSI': 'BANTEN', 'KODE AREA': '021', 'NO. TELEPON': '3456789'}
]

def all_contact(daftar_Kontak, showed_ID = True):
    tabel_kontak = PrettyTable()
    
    if showed_ID:
        tabel_kontak.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
        for kontak in daftar_Kontak:
            tabel_kontak.add_row([kontak['ID'], kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])

    else:
        tabel_kontak.field_names = ['NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
        for kontak in daftar_Kontak:
            tabel_kontak.add_row([kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])

    print('\nDAFTAR KONTAK')
    print(tabel_kontak)     

nama_kontak = ['PT MAJU SEJAHTERA', 'CV SUKSES ABADI', 'UD JAYA MANDIRI', 'TOKO HARAPAN', 'PT BINA USAHA', 'HARAPAN JAYA', 'PT CIPTA KARYA', 'UD ANEKA RASA', 'CV MEGAH JAYA', 'PT MULTI USAHA']
jenis_bisnis = ['Perdagangan', 'Konstruksi','Kuliner', 'Ritel', 'Jasa Keuangan', 'Properti', 'Logistik', 'Teknologi Informasi']
kotaKabupaten = ['Jakarta Pusat', 'Jakarta Barat', 'Jakarta Utara', 'Jakarta Timur', 'Jakarta Selatan', 'Bogor', 'Depok', 'Tangerang', 'Bekasi']
provinsi1 = ['DKI JAKARTA', 'BANTEN', 'JAWA BARAT']
kodeArea = ['021', '0251']
kontak = ['1234567', '7654321', '9876543', '8765432', '6543210', '8901234', '1234578', '8765431', '5678912', '3456789']

# Mencari Kontak
def search_contact(daftar_Kontak, role='user'):
    print('\n===== PILIH KATEGORI PENCARIAN =====')
    print('1. Pencarian 1 Kategori')
    print('2. Pencarian 2 Kategori')
    print('3. Pencarian 3 Kategori')
    print('0. Menu Utama')

    opsi = input('Pilih Opsi Pencarian Kontak (1/2/3): ')

    showed_ID = True if role == 'admin' else False

    if opsi == '0':
        return
    
    elif opsi == '1':
        print('\n===== PENCARIAN 1 KATEGORI =====')
        print('1. Cari Berdasarkan Nama')
        print('2. Cari Berdasarkan Bidang Bisnis')
        print('3. Cari Berdasarkan Kota')

        opsi1 = input('Pilih Opsi Pencarian Kontak (1/2/3): ')

        all_contact(daftar_Kontak, showed_ID=showed_ID)
        
        if opsi1 == '0':
            return
        
        elif opsi1 == '1':
            while True:
                nama_contact = input('Masukkan Nama Kontak yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').upper()
                hasil_pencarian = [kontak for kontak in daftar_Kontak if re.search(nama_contact, kontak['NAMA'], re.IGNORECASE)]
                if nama_contact == '0':
                    search_contact(daftar_Kontak, role=role)
                    return
                elif nama_contact == '1':
                    return
                
                if not hasil_pencarian:
                    print('Kontak Tidak Terdaftar.')
                    continue
                break

        elif opsi1 == '2':
            while True:
                bdg_bisnis = input('Masukkan Bidang Bisnis yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').title()
                hasil_pencarian = [kontak for kontak in daftar_Kontak if re.search(bdg_bisnis, kontak['BIDANG BISNIS'], re.IGNORECASE)]
                if bdg_bisnis == '0':
                    search_contact(daftar_Kontak, role=role)
                    return
                elif bdg_bisnis == '1':
                    return
                
                if not hasil_pencarian:
                    print('Kontak Tidak Terdaftar.')
                    continue
                break
    
        elif opsi1 == '3':
            while True:
                kota_bisnis = input('Masukkan Kota/Kabupaten yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').title()
                hasil_pencarian = [kontak for kontak in daftar_Kontak if re.search(kota_bisnis,kontak['KOTA/KABUPATEN'], re.IGNORECASE)]
                if kota_bisnis == '0':
                    search_contact(daftar_Kontak, role=role)
                    return
                elif kota_bisnis == '1':
                    return
                
                if not hasil_pencarian:
                    print('Kontak Tidak Terdaftar.')
                    continue
                break

        else:
            print('Input Invalid!')
            return
    
        if hasil_pencarian:
            tabel_pencarian = PrettyTable()

            if showed_ID:
                tabel_pencarian.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
            else:
                tabel_pencarian.field_names = ['NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']

            for kontak in hasil_pencarian:
                if showed_ID:
                    tabel_pencarian.add_row([kontak['ID'], kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])
                else:
                    tabel_pencarian.add_row([kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])
        print('Hasil Pencarian Kontak: ')
        print(tabel_pencarian)

    elif opsi == '2':
        print('\n===== PENCARIAN 2 KATEGORI =====')
        print('1. Cari Berdasarkan Nama dan Bidang Bisnis')
        print('2. Cari Berdasarkan Nama dan Kota')
        print('3. Cari Berdasarkan Bidang Bisnis dan Kota')

        opsi2 = input('Pilih Opsi Pencarian Kontak (1/2/3): ')

        all_contact(daftar_Kontak, showed_ID=showed_ID)

        if opsi2 == '1':
            while True:
                nama_contact = input('Masukkan Nama Kontak yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').upper()
                if nama_contact == '0':
                    search_contact(daftar_Kontak, role=role)
                    return
                elif nama_contact == '1':
                    return
                
                bdg_bisnis = input('Masukkan Bidang Bisnis yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').title()
                hasil_pencarian = [kontak for kontak in daftar_Kontak if re.search(nama_contact, kontak['NAMA'],re.IGNORECASE) and re.search(bdg_bisnis, kontak['BIDANG BISNIS'], re.IGNORECASE)]
                
                if not hasil_pencarian:
                    print('Kontak Tidak Terdaftar.')
                    continue
                break

        elif opsi2 == '2':
            while True:
                nama_contact = input('Masukkan Nama Kontak yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').upper()
                if nama_contact == '0':
                    search_contact(daftar_Kontak, role=role)
                    return
                elif nama_contact == '1':
                    return
                
                kota_bisnis = input('Masukkan Kota/Kabupaten yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').title()
                hasil_pencarian = [kontak for kontak in daftar_Kontak if re.search(nama_contact, kontak['NAMA'],re.IGNORECASE) and re.search(kota_bisnis, kontak['KOTA/KABUPATEN'], re.IGNORECASE)]
                
                
                if not hasil_pencarian:
                    print('Kontak Tidak Terdaftar.')
                    continue
                break
    
        elif opsi2 == '3':
            while True:
                bdg_bisnis = input('Masukkan Bidang Bisnis yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').title()
                if bdg_bisnis == '0':
                    search_contact(daftar_Kontak, role=role)
                    return
                elif bdg_bisnis == '1':
                    return
                
                kota_bisnis = input('Masukkan Kota/Kabupaten yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').title()
                hasil_pencarian = [kontak for kontak in daftar_Kontak if re.search(bdg_bisnis, kontak['BIDANG BISNIS'],re.IGNORECASE) and re.search(kota_bisnis, kontak['KOTA/KABUPATEN'], re.IGNORECASE)]
                
                    
                if not hasil_pencarian:
                    print('Kontak Tidak Terdaftar.')
                    continue
                break

        else:
            print('Input Invalid!')
            return
    
        if hasil_pencarian:
            tabel_pencarian = PrettyTable()

            if showed_ID:
                tabel_pencarian.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
            else:
                tabel_pencarian.field_names = ['NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']


            for kontak in hasil_pencarian:
                if showed_ID:
                    tabel_pencarian.add_row([kontak['ID'], kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])
                else:
                    tabel_pencarian.add_row([kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])

        print('Hasil Pencarian Kontak: ')
        print(tabel_pencarian)

    elif opsi == '3':
        
        all_contact(daftar_Kontak, showed_ID=True)
        
        while True:
            nama_contact = input('Masukkan Nama Kontak yang Ingin Dicari (Ketik 0 untuk Kembali dan 1 untuk Menu Utama): ').upper()
            if nama_contact == '0':
                search_contact(daftar_Kontak, role=role)
                return
            elif nama_contact == '1':
                return
            
            bdg_bisnis = input('Masukkan Bidang Bisnis yang Ingin Dicari: ').title()
            kota_bisnis = input('Masukkan Kota/Kabupaten yang Ingin Dicari: ').title()
            hasil_pencarian = [kontak for kontak in daftar_Kontak if re.search(nama_contact, kontak['NAMA'],re.IGNORECASE) and re.search(bdg_bisnis, kontak['BIDANG BISNIS'], re.IGNORECASE) and re.search(kota_bisnis, kontak['KOTA/KABUPATEN'], re.IGNORECASE)]
                
            if nama_contact not in nama_kontak and kota_bisnis not in kotaKabupaten and kota_bisnis not in kotaKabupaten:
                print('Kontak Tidak Terdaftar.')
                continue
            break
    
        if hasil_pencarian:
            tabel_pencarian = PrettyTable()

            if showed_ID:
                tabel_pencarian.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
            else:
                tabel_pencarian.field_names = ['NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']


            for kontak in hasil_pencarian:
                if showed_ID:
                    tabel_pencarian.add_row([kontak['ID'], kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])
                else:
                    tabel_pencarian.add_row([kontak['NAMA'], kontak['BIDANG BISNIS'], kontak['ALAMAT'], kontak['DESA/KELURAHAN'], kontak['KECAMATAN'], kontak['KOTA/KABUPATEN'], kontak['PROVINSI'], kontak['KODE AREA'], kontak['NO. TELEPON']])

        print('Hasil Pencarian Kontak: ')
        print(tabel_pencarian)
    
    else:
        print('Input Invalid!')
        return

# Menambah Kontak
def new_contact(daftar_Kontak, kontak, kodeArea, provinsi1, kotaKabupaten):
    print('\n===== MENAMBAH KONTAK =====')
    
    while True:
        no_telepon = input('Masukkan Nomor Telepon (Ketik 0 Jika Ingin Berhenti): ')
        
        if no_telepon == '0':
            return
        
        if not no_telepon.isdigit():
            print('Nomor Telepon Tidak Valid!')
            continue

        if no_telepon in kontak:
            print('Nomor Telepon Telah Terdaftar!')
            continue
        else:
            print('Nomor Telepon Berhasil Didaftarkan!')
            kontak.append(no_telepon)
            break

    while True:
        kode_Area = input('Masukkan Kode Area: ')
        if kode_Area not in kodeArea:
            print('Kode Area Tidak Ditemukan!')
            continue
        else:
            print('Kode Area Berhasil Ditambahkan!')
            break
        
    no_id = f"ID{len(daftar_Kontak) + 1:03d}" 
    
    while True:
        nama = input('Masukkan Nama: ').upper()
        if nama in nama_kontak:
            nama.append(nama_kontak)
            continue
        break

    while True:
        bidangBisnis = input('Masukkan Bidang Bisnis: ').title()
        if bidangBisnis in jenis_bisnis:
            bidangBisnis.append(jenis_bisnis)
            continue
        break

    alamat = input('Masukkan Alamat Lengkap: ').title()
    desa_kelurahan = input('Masukkan Desa/Kelurahan: ').title()
    kecamatan = input('Masukkan Kecamatan: ').title()

    while True:
        kota_kabupaten = input('Masukkan Kota/Kabupaten: ').title()
        if kota_kabupaten not in kotaKabupaten:
            print('Kota/Kabupaten Tidak Ditemukan!')
            continue
        break
    
    while True:
        provinsi = input('Masukkan Provinsi: ').upper()
        if provinsi not in provinsi1:
            print('Provinsi Tidak Ditemukan!')
            continue
        break  
        
    kontak_baru = {
        'ID': no_id,
        'NAMA': nama,
        'BIDANG BISNIS': bidangBisnis,
        'ALAMAT': alamat,
        'DESA/KELURAHAN': desa_kelurahan,
        'KECAMATAN': kecamatan,
        'KOTA/KABUPATEN': kota_kabupaten,
        'PROVINSI': provinsi,
        'KODE AREA': kode_Area,
        'NO. TELEPON': no_telepon
    }

    print('Data Kontak Baru: ')
    tabel_kontak_baru = PrettyTable()
    tabel_kontak_baru.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
    tabel_kontak_baru.add_row([kontak_baru['ID'], kontak_baru['NAMA'], kontak_baru['BIDANG BISNIS'], kontak_baru['ALAMAT'], kontak_baru['DESA/KELURAHAN'], kontak_baru['KECAMATAN'], kontak_baru['KOTA/KABUPATEN'], kontak_baru['PROVINSI'], kontak_baru['KODE AREA'], kontak_baru['NO. TELEPON']])

    print(tabel_kontak_baru)

    text = input('Apakah Data yang Ditampilkan Sudah Benar? (ya/tidak): ').lower()
    if text == 'ya':
        daftar_Kontak.append(kontak_baru)
        print('Berhasil Menambahkan Kontak Baru!')
    else:
        print('Gagal Menambahkan Kontak Baru.')

    all_contact(daftar_Kontak, showed_ID=True)

# Edit Kontak
def edit_contact():
    all_contact(daftar_Kontak, showed_ID=True)

    nama_edit = input('Masukkan Nama Kontak: ').upper()
    kontak_edit = None
    
    # Mencari Kontak berdasarkan ID
    for kontak in daftar_Kontak:
        if kontak['NAMA'] == nama_edit:
            kontak_edit = kontak
            break

    if kontak_edit:
        kontak_asli = kontak_edit.copy()

        print('Data Kontak yang Akan Diubah: ')
        tabel_kontak_edit = PrettyTable()
        tabel_kontak_edit.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
        tabel_kontak_edit.add_row([kontak_edit['ID'], kontak_edit['NAMA'], kontak_edit['BIDANG BISNIS'], kontak_edit['ALAMAT'], kontak_edit['DESA/KELURAHAN'], kontak_edit['KECAMATAN'], kontak_edit['KOTA/KABUPATEN'], kontak_edit['PROVINSI'], kontak_edit['KODE AREA'], kontak_edit['NO. TELEPON']])    

        print(tabel_kontak_edit)

        text = input('Apakah Data yang Ditampilkan Sudah Benar? (ya/tidak): ').lower()
        if text == 'tidak':
            print('Mengubah Kontak Dibatalkan.')
            return
        
        else:
            print('Pilih Kategori yang Ingin di Ubah: ')
            print('1. Nama Pelanggan')
            print('2. Bidang Bisnis')
            print('3. Alamat Pelanggan')
            print('4. Desa/Kelurahan Pelanggan')
            print('5. Kecamatan Pelanggan')
            print('6. Nomor Telepon Pelanggan')
            print('0. Menu Utama')

            opsi_edit = input('Pilih Opsi untuk Mengubah Kontak: ')

            if opsi_edit == '0':
                menu_utama_admin()
            elif opsi_edit == '1':
                nama_edit = input('Masukkan Nama Baru (Ketik 0 untuk Kembali): ').upper()
                kontak_edit['NAMA'] = nama_edit
            elif opsi_edit == '2':
                bisnis_edit = input('Masukkan Bidang Bisnis Terbaru: ')
                kontak_edit['BIDANG BISNIS'] = bisnis_edit
            elif opsi_edit == '3':
                alamat_edit = input('Masukkan Alamat Terbaru: ')
                kontak_edit['ALAMAT'] = alamat_edit
            elif opsi_edit == '4':
                kelurahan_edit = input('Masukkan Desa/Kelurahan Terbaru: ')
                kontak_edit['DESA/KELURAHAN'] = kelurahan_edit
            elif opsi_edit == '5':
                kecamatan_edit = input('Masukkan Kecamatan Terbaru: ')
                kontak_edit['KECAMATAN'] = kecamatan_edit
            elif opsi_edit == '6':
                notelp_edit = input('Masukkan Nomor Telepon Terbaru: ')
                kontak_edit['NO. TELEPON'] = notelp_edit
                if not notelp_edit.isdigit():
                    print('Nomor Telepon Tidak Valid!')
                    edit_contact()

            else:
                print('Opsi Tidak Valid!')
                return

            print('Data Kontak: ')
            tabel_kontak_edit = PrettyTable()
            tabel_kontak_edit.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
            tabel_kontak_edit.add_row([kontak_edit['ID'], kontak_edit['NAMA'], kontak_edit['BIDANG BISNIS'], kontak_edit['ALAMAT'], kontak_edit['DESA/KELURAHAN'], kontak_edit['KECAMATAN'], kontak_edit['KOTA/KABUPATEN'], kontak_edit['PROVINSI'], kontak_edit['KODE AREA'], kontak_edit['NO. TELEPON']])

            print(tabel_kontak_edit)

            text = input('Apakah Data yang Ditampilkan Sudah Benar? (ya/tidak): ').lower()
            if text == 'ya':
                print('Berhasil Mengubah Kontak')
                return
            else:
                print('Perubahan Kontak Dibatalkan.')
                
                for key in kontak_asli:
                    kontak_edit[key] = kontak_asli[key]
    else:
        print('ID Tidak Ditemukan.')

# Menghapus Daftar Kontak
def del_contact():

    all_contact(daftar_Kontak, showed_ID=True)

    nama_del = input('Masukkan Nama yang Ingin Dihapus: ').upper()
    found = False

    kontak_hapus = None 
    original_index = None 

    for i, kontak in enumerate(daftar_Kontak): 
        if kontak['NAMA'] == nama_del:
            kontak_hapus = kontak
            original_index = i 
            del daftar_Kontak[i]
            found = True
            break

    if not found:
        print('Nama Tidak Terdaftar!')
        del_contact() 
      
    print('Data Kontak yang Akan Dihapus: ')
    tabel_kontak_hapus = PrettyTable()
    tabel_kontak_hapus.field_names = ['ID', 'NAMA', 'BIDANG BISNIS', 'ALAMAT', 'DESA/KELURAHAN', 'KECAMATAN', 'KOTA/KABUPATEN', 'PROVINSI', 'KODE AREA', 'NO. TELEPON']
    tabel_kontak_hapus.add_row([kontak_hapus['ID'], kontak_hapus['NAMA'], kontak_hapus['BIDANG BISNIS'], kontak_hapus['ALAMAT'], kontak_hapus['DESA/KELURAHAN'], kontak_hapus['KECAMATAN'], kontak_hapus['KOTA/KABUPATEN'], kontak_hapus['PROVINSI'], kontak_hapus['KODE AREA'], kontak_hapus['NO. TELEPON']])    

    print(tabel_kontak_hapus)

    text = input('Apakah Data yang Ditampilkan Sudah Benar? (ya/tidak): ').lower()
    if text == 'ya':
        print('Kontak Telah Dihapus.')
    else:
        print('Menghapus Kontak Dibatalkan.')

        if original_index is not None:
            daftar_Kontak.insert(original_index, kontak_hapus)
            
    all_contact(daftar_Kontak)

login()