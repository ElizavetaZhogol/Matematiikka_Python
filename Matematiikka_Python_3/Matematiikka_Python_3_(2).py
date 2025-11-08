# Kuvan oletuskoko 6.4 * 4.8 tuumaa. Haluat tehdä kuvaajan väliltä -3π - 3π.
# Levennä kuva kolminkertaiseksi ja vaihdä käyrien värit sekä piirtotyyli. Lisää myöskin kuvaan selite.
# Akselitkin ovat vähän tylsät. Aseta akselien tekstit muoton π, π/2 jne ...

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(19.2, 14.4))

X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color='green', linestyle='-', label='cos(x)')
plt.plot(X, S, color='red', linestyle='--', label='sin(x)')

x_ticks = [-3*np.pi, -2.5*np.pi, -2*np.pi, -1.5*np.pi, -np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi, 2.5*np.pi, 3*np.pi]
x_labels = [r'$-3\pi$', r'$-\frac{5\pi}{2}$', r'$-2\pi$', r'$-\frac{3\pi}{2}$', 
            r'$-\pi$', r'$-\frac{\pi}{2}$', '0', 
            r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', 
            r'$\frac{5\pi}{2}$', r'$3\pi$']

plt.xticks(x_ticks, x_labels, fontsize=12)

plt.legend(loc='upper right', fontsize=14)

plt.title('Funktioiden sin(x) ja cos(x) kuvaajat')

plt.show()