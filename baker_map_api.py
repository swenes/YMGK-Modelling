class BakerMap:
    def __init__(self, x0, y0):
        """Baker Map başlangıç durumunu başlatır."""
        self.x = x0
        self.y = y0

    def step(self):
        """Baker Map'te bir adım ilerler."""
        new_x = (self.x + self.y) % 1
        new_y = (self.x + 2 * self.y) % 1
        self.x = new_x
        self.y = new_y
        return self.x, self.y

    def run(self, steps):
        """Baker Map'te belirli sayıda adım ilerler."""
        trajectory = []
        for _ in range(steps):
            trajectory.append(self.step())
        return trajectory

    def get_state(self):
        """Mevcut durumu döner."""
        return self.x, self.y

    def set_state(self, x, y):
        """Durumu ayarlar."""
        self.x = x
        self.y = y

# Kullanım örneği:
baker_map = BakerMap(0.1, 0.1)
print("Başlangıç durumu:", baker_map.get_state())
trajectory = baker_map.run(10)
print("10 adım sonrası durumlar:", trajectory)
print("Son durum:", baker_map.get_state())
