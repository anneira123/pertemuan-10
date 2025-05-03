from abc import ABC, abstractmethod

class Section(ABC):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

# Factory class
class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)

class Linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class Facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

if __name__ == "__main__": # Tambahkan blok if __name__ == "__main__":
    profile_type = input("Profil apa yang ingin anda buat? [Linkedin atau Facebook] ")
    profile_type = profile_type.lower() # Convert input to lowercase
    if profile_type == "linkedin":
        profile = Linkedin()
    elif profile_type == "facebook":
        profile = Facebook()
    else:
        print("Pilihan profil tidak valid.")
        exit() # Keluar dari program jika input tidak valid

    print(f"Profil {type(profile).__name__} sedang dibuat..")
    print("Profil mempunyai Section:")
    for section in profile.getSections():
        section.describe() # Panggil method describe() untuk mencetak deskripsi
