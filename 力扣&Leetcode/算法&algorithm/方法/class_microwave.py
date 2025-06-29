
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand}之前已经开机")
        else:
            self.turned_on = True
            print(f"{self.brand}之前关机，现在开机")

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"{self.brand}之前开机，现在关机")
        else:
            print(f"{self.brand}之前已经关机")

    def run(self, second: int) -> None:
        if self.turned_on:
            print(f"{self.brand}开机并且运行{second}秒")
        else:
            print(f"先把{self.brand}开机")

smeg = Microwave(brand='Smeg', power_rating='B')

smeg.turn_on()
smeg.turn_on()
smeg.run(30)
smeg.turn_off()
smeg.turn_off()
