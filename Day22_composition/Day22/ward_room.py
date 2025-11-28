class Room:
    def __init__(self, number):
        self.number = number
    
class Ward:
    def __init__(self ,name, num_rooms):
        self.name = name
        self.rooms = [Room(i) for i in range(1, num_rooms+1)]
        
w = Room("JSM 001")
wa = Ward("Ward A", 4)
print(f"Room number: {w.number}")
print(f"ward names: {wa.name}")
print(f"no of rooms in ward: {len(wa.rooms)}")