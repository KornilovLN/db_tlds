import numpy as np
import os

def generate_data(n=10000):
    data = []
    for i in range(n):
        x = np.random.rand()
        y = 1000 * np.sin(x)
        data.append((x, y))
        if(i%100==0):
            print(f"Generated {i+1}/{n}: x={x}, y={y}")
    return data

if __name__ == '__main__':
    data = generate_data()
    # Сохраняем сгенерированные данные в файл
    os.makedirs('/app/data', exist_ok=True)
    with open('/app/data/generated_data.npy', 'wb') as f:
        np.save(f, data)

