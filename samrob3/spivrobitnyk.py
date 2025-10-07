

class Spivrobitnyk:
    def __init__(self, imya, zarplata, vidpratsiovani_dni, vidsotok_bonus=0):
        self._imya = imya
        self._zarplata = zarplata
        self._vidpratsiovani_dni = vidpratsiovani_dni
        self._vidsotok_bonus = vidsotok_bonus

    # Гетери і сетери
    def get_imya(self):
        return self._imya

    def set_imya(self, imya):
        self._imya = imya

    def get_zarplata(self):
        return self._zarplata

    def set_zarplata(self, zarplata):
        self._zarplata = zarplata

    def get_vidpratsiovani_dni(self):
        return self._vidpratsiovani_dni

    def set_vidpratsiovani_dni(self, dni):
        self._vidpratsiovani_dni = dni

    def get_vidsotok_bonus(self):
        return self._vidsotok_bonus

    def set_vidsotok_bonus(self, vidsotok):
        self._vidsotok_bonus = vidsotok

    def rozrahuvaty_zarplatu(self):
        return (self._zarplata / 30) * self._vidpratsiovani_dni

    def rozrahuvaty_bonus(self):
        return (self._zarplata / 100) * self._vidsotok_bonus


