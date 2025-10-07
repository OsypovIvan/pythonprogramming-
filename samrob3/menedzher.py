from spivrobitnyk import Spivrobitnyk


class Menedzher(Spivrobitnyk):
    rozmir_premiyi = 100  # стат атрибут для менеджерів

    def __init__(self, imya, zarplata, vidpratsiovani_dni, pidlegli, vidsotok_bonus=0):

        # викликає коснтуктор базового класу
        super().__init__(imya, zarplata, vidpratsiovani_dni, vidsotok_bonus)
        self._pidlegli = pidlegli

    # Гетери/сетери
    def get_pidlegli(self):
        return self._pidlegli

    def set_pidlegli(self, pidlegli):
        self._pidlegli = pidlegli

    def zvit(self):
        return f"Менеджер {self._imya} керує {self._pidlegli} співробітниками."

        #Перевизначення методу бонусу (поліморфізм)
    def rozrahuvaty_bonus(self):
        base_bonus = super().rozrahuvaty_bonus()
        return base_bonus + (self._pidlegli * Menedzher.rozmir_premiyi)
