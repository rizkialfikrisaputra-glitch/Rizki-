
# Input data produk
jenis = input("Jenis produk (Elektronik/Pakaian/Makanan/Kosmetik): ")
harga = int(input("Harga produk: "))
jual = int(input("Jumlah terjual: "))

#  kategori jenis
if jenis == "Elektronik":
    kategori_jenis = "Elektronik"
elif jenis == "Pakaian":
    kategori_jenis = "Pakaian"
elif jenis == "Makanan":
    kategori_jenis = "Makanan"
elif jenis == "Kosmetik":
    kategori_jenis = "Kosmetik"
else:
    kategori_jenis = "Tidak diketahui"

#  kategori harga
if harga > 100000:
    kategori_harga = "Premium"
elif harga >= 50000:
    kategori_harga = "Menengah"
else:
    kategori_harga = "Terjangkau"

# kategori penjualan
if jual >= 100:
    kategori_jual = "Best Seller"
elif jual >= 50:
    kategori_jual = "Populer"
else:
    kategori_jual = "Normal"

# Tampilkan hasil
print("--- HASIL KATEGORI PRODUK ---")
print("Jenis     :", kategori_jenis)
print("Harga     :", kategori_harga)
print("Penjualan :", kategori_jual)
