from flask import Flask, request, send_file
import numpy as np
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

def logistic_map(r, x0, num_steps):
    x = np.zeros(num_steps)
    x[0] = x0
    for i in range(1, num_steps):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x

@app.route('/logisticmap.png')
def logistic_map_png():
    # Parametreleri alın
    r = float(request.args.get('r', 3.9))
    x0 = float(request.args.get('x0', 0.5))
    num_steps = int(request.args.get('num_steps', 100))

    # Logistic haritasını hesaplayın
    population = logistic_map(r, x0, num_steps)

    # Grafik oluştur
    plt.figure()
    plt.plot(population, 'b-', label='Logistic Haritası')
    plt.title('Logistic Haritası (r={})'.format(r))
    plt.xlabel('Adım')
    plt.ylabel('Popülasyon Oranı')
    plt.legend()

    # Grafiği hafızada saklayın
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()  # Grafiği kapatın

    # PNG dosyasını yanıt olarak gönderin
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
