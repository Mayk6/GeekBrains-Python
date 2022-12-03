class FoodInfo:
    def __init__(self, proteins, fats, carbonhydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbonhydrates = carbonhydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbonhydrates(self):
        return self.carbonhydrates

    def get_kcalories(self):
        return self.proteins * 4 + self.fats * 9 + self.carbonhydrates * 4

    def __add__(self, other):
        return FoodInfo(self.proteins + other.proteins,
                        self.fats + other.fats,
                        self.carbonhydrates + other.carbonhydrates
                        )
