class ParcareNFA:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.occupied_spots = 0

    def park_car(self):
        if self.occupied_spots < self.total_spots:
            self.occupied_spots += 1
            print(f"Masina parcata. Locuri ocupate: {self.occupied_spots}/{self.total_spots}")
        else:
            print("Eroare: Parcarea este plina!")

    def leave_parking(self):
        if self.occupied_spots > 0:
            self.occupied_spots -= 1
            print(f"Masina a plecat. Locuri ocupate: {self.occupied_spots}/{self.total_spots}")
        else:
            print("Eroare: Parcarea este goala!")

    def check_parking_status(self):
        print(f"Stare parcare: {self.occupied_spots}/{self.total_spots} locuri ocupate.")

parking = ParcareNFA(total_spots=3)

while True:
    command = input("Introduceti comanda (P=parcare, L=plecare, S=status, Q=exit): ").strip().upper()

    if command == "P":
        parking.park_car()
    elif command == "L":
        parking.leave_parking()
    elif command == "S":
        parking.check_parking_status()
    elif command == "Q":
        print("Iesire din sistem.")
        break
    else:
        print("Comanda invalidă!")
