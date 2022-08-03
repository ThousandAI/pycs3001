# 類別
class Character:
    def __init__(self, name, gender, weapon="bat"):  # property (attribute) 屬性
        self.lv = 1
        self.exp = 0
        self.n = name
        self.g = gender
        self.w = weapon
        #print("This is Character Class.")

    def __str__(self):
        return f"Name {self.n}, Gender {self.g}, Weapon {self.w}"

    # method
    def attack(self):
        self.exp += 40
        self.level_up()


    def level_up(self):
        if self.exp >= 100:
            self.lv += 1
            self.exp -= 100
            print(f"{self.n} Level up!!")

class Warrior(Character):
    # 建構子 (Constructor)
    def __init__(self, name, gender, weapon="bat"):  # property (attribute) 屬性
        super().__init__(name, gender, weapon)
        self.sp = 100
        #print("This is warrior class.")

    def attack(self):
        super().attack()
        print(f"{self.lv}, {self.exp}")

    def bash(self):
        if self.lv > 5:
            print("Bash")
            self.sp -= 10
        else:
            print("Not")


class Magician(Character):
    # 建構子 (Constructor)
    def __init__(self, name, gender, weapon="bat"):  # property (attribute) 屬性
        super().__init__(name, gender, weapon)
        self.mp = 100

    def fireball(self):
        if self.lv > 5:
            self.mp -= 10
            print("fireball")
        else:
            print("Not")









class Enemy:
    def __init__(self):
        self.n = "Monster"
        self.hp = 100


w1 = Warrior(name="Thousand", gender="Male", weapon="Sword")
m1 = Magician(name="Allie", gender="Female", weapon="Longbow")
w1.attack()
m1.attack()
# w2 = Warrior(name="Allie", gender="Female", weapon="Longbow")
#
# for i in range(20):
#     w1.attack()
#     w1.bash()

# e = Enemy()
# # print(w1.n, w1.g, w1.lv)
# # print(w2.n, w2.g, w2.lv)
# for i in range(10):
#     w1.attack(enemy=e)
#
# print(e.hp)

