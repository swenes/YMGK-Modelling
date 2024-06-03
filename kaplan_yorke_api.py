class KaplanYorkeMap:
    def __init__(self, x0, y0, a):
        """Kaplan-Yorke Map başlangıç durumunu başlatır."""
        self.x = x0
        self.y = y0
        self.a = a

    def step(self):
        """Kaplan-Yorke Map'te bir adım ilerler."""
        new_x = 0.5 * (self.x + abs(self.x)) - self.y
        new_y = 0.5 * (self.y + abs(self.y)) - self.a * self.x
        self.x = new_x
        self.y = new_y
        return self.x, self.y

    def run(self, steps):
        """Kaplan-Yorke Map'te belirli sayıda adım ilerler."""
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
kaplan_yorke_map = KaplanYorkeMap(0.1, 0.1, 0.5)
print("Başlangıç durumu:", kaplan_yorke_map.get_state())
trajectory = kaplan_yorke_map.run(10)
print("10 adım sonrası durumlar:", trajectory)
print("Son durum:", kaplan_yorke_map.get_state())
