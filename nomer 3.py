class Hewan:
    def jenis(self):  # Perhatikan 'Self' diganti menjadi 'self'
        pass

class Harimau(Hewan):
    def jenis(self):
        return "Harimau adalah jenis Kucing yang berbahaya"

class Ular(Hewan):
    def jenis(self):  # Perhatikan 'Self' diganti menjadi 'self'
        return "ular adalah jenis hewan yang berbisa"

class Factory:  # Perhatikan 'pass Factory' diganti menjadi 'class Factory'
    @staticmethod
    def binatang(jenis_hewan):  # Perhatikan 'binatang' (lebih deskriptif)
        if jenis_hewan == "Harimau":
            return Harimau()
        elif jenis_hewan == "Ular":
            return Ular()
        else:
            raise ValueError("Hewan ini tidak ada dalam list")

# Penggunaan Factory Pattern yang dibetulkan
hewan1 = Factory.binatang("Harimau")  # Perhatikan 'analisis_hewan' diganti 'binatang'
print(hewan1.jenis())

hewan2 = Factory.binatang("Ular")  # Perhatikan 'analisis_hewan' diganti 'binatang'
print(hewan2.jenis())