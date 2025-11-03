import matplotlib.pyplot as plt
import numpy as np
import math
# Datos
#x = np.linspace(0, 10, 100)
#y = np.sin(x)
x = []
y = []
for i in range(100):
    x.append(i)
 
for j in range(len(x)):
    y.append(math.cos(2*math.pi*x[j]))
 
 
# Crear la gráfica
plt.plot(x, y)
 
# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('sin(X)')
 
# Mostrar la gráfica
plt.show()
 
 