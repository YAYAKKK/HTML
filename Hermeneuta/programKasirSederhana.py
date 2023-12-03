import os
os.system('cls')

print('=====PROGRAM KASIR SEDERHANA======\n')

class Product:
    def __init__(self, namaProduct, harga, stock, kodeproduct) -> None:
        self.namaProduct = namaProduct
        self.harga = harga
        self.stock = stock
        self.kodeproduct = kodeproduct

    def sisaStock(self, quantitas):
        if quantitas <= self.stock:
            self.stock -= quantitas
            return True
        else:
            print(f'Jumlah stock store kami tidak mencukupi, Mohon maaf!!!')
            return False

def main():
    Pensil = Product('Pensil', 2500, 70, '1')
    Pulpen = Product('Pulpen', 3500, 70, '2')
    Buku = Product('Buku', 5000, 45, '3')
    Stipex = Product('Stipex', 8000, 67, '4')
    Penggaris = Product('Penggaris', 3000, 30, '5')

    stockProduct = [Pensil, Pulpen, Penggaris, Buku, Stipex]

    totalBelanjaan = 0
    belanjaan = []

    while True:
        for DaftarProduct in stockProduct:
            print(f'Produk: {DaftarProduct.namaProduct} Harga: {DaftarProduct.harga} Stok: {DaftarProduct.stock} Kode: {DaftarProduct.kodeproduct}')

        kode_produk = input(f'\nMasukkan kode produk yang ingin Anda beli (atau ketik "D" jika suda selesai belanja): ')
        
        if kode_produk == 'D' or kode_produk == 'd':
            break

        found = False
        for product in stockProduct:
            if product.kodeproduct == kode_produk:
                jumlah_beli = int(input(f'Masukkan jumlah yang ingin Anda beli: '))
                if product.sisaStock(jumlah_beli):
                    totalBelanjaan += product.harga * jumlah_beli
                    belanjaan.append({
                        'Produk': product.namaProduct,
                        'Harga': product.harga,
                        'Jumlah Beli': jumlah_beli,
                        'Subtotal': product.harga * jumlah_beli
                    })
                    print(f'{jumlah_beli} {product.namaProduct} ditambahkan ke keranjang.\n')
                found = True
                break

        if not found:
            print('Kode produk tidak valid. Silakan coba lagi.')

    print('\n--- Struk Belanja ---\n')

    for item in belanjaan:
        print(f'{item["Produk"]} | Harga: {item["Harga"]} | Jumlah Beli: {item["Jumlah Beli"]} | Subtotal: {item["Subtotal"]}')

    print(f'Total Belanja: {totalBelanjaan}')
    print('Terima kasih atas pembelian Anda!')

    # Menampilkan sisa stok setiap produk setelah selesai belanja
    print('\n--- Sisa Stok Produk ---\n')
    for DaftarProduct in stockProduct:
        print(f'Produk: {DaftarProduct.namaProduct} | Sisa Stok: {DaftarProduct.stock}')

if __name__ == "__main__":
    main()
