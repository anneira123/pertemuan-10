class Sim_Cache:
    def __new__(cls):
        if not hasattr(cls, 'cache'):
            cls.cache = super().__new__(cls)
        return cls.cache

    def __init__(self):
        self.nama_web = "PBOTRI"
        self.create_cache()

    def create_cache(self):
        self.cache_source = self.nama_web + ".txt"
        self.cache_file_name = "cache_" + self.nama_web + ".txt"
        try:  # Tambahkan try-except untuk menangani kesalahan file
            sf = open(self.cache_source, "r")  # buka source file
            cf = open(self.cache_file_name, "w")  # buat file cache baru
            cf.write(f"Ini adalah file cache dari web {self.nama_web}\n")
            line1 = False
            for l in sf:
                if "Start_cache" in l:  # menentukan baris awal cache
                    line1 = True
                if line1:
                    cf.write(l)  # menyalin cache dari source
            sf.close()  # Selalu tutup file setelah digunakan
            cf.close()
        except FileNotFoundError:
            print(f"Error: File {self.cache_source} tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat membuat cache: {e}")

    def get_cache(self):
        if not hasattr(self, 'cache'): #Perbaikan dari self.cache menjadi hasattr(self, 'cache')
            Sim_Cache() #memanggil konstruktor
        print(f"Nama file cache adalah {self.cache.cache_file_name}")
        try: # menambahkan try except
            cf = open(self.cache.cache_file_name, "r")
            print(cf.read())
            cf.close()
        except FileNotFoundError:
            print(f"Error: File {self.cache.cache_file_name} tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat membaca cache: {e}")

print("=====Instansiasi pertama:=====")
cache1 = Sim_Cache()
cache1.get_cache()
print("\n=====Instansiasi kedua:=====")
cache2 = Sim_Cache()
try: # menambahkan try except
    add_cache = open("cache_PBOTRI.txt", "a")
    add_cache.write("\n***Baris tambahan di file cache***")
    add_cache.close()
except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan ke cache: {e}")
cache2.get_cache()