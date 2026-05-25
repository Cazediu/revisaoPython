import matplotlib.pyplot as plt
import numpy as np

categorias = ['Alimentação', 'Transporte', 'Lazer', 'Anna', 'Outros']
gastos = [1200, 600, 400, 300, 500]
cores = ['#3498DB', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6']
 
plt.figure(figsize=(7, 7))
plt.pie(
    gastos,
    labels=categorias,
    colors=cores,
    autopct='%1.1f%%',      # mostra porcentagem com 1 casa decimal
    startangle=234,           # começa do topo
    explode=(0.5, 0, 0, 0, 0)   # destaca a primeira fatia
)
plt.title('Distribuição de Gastos Mensais', fontsize=14)
plt.tight_layout()
plt.show()



