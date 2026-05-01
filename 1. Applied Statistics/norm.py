import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. Configurações da Distribuição Normal Padrão
media = 0
desvio_padrao = 1
nivel_confianca = 0.95

# 2. Calcular os valores Z críticos usando norm.ppf (o coração da sua pergunta!)
# Para 95% de confiança no centro, sobra 2.5% (0.025) em cada cauda.
z_critico_inf = norm.ppf((1 - nivel_confianca) / 2) # Dá -1.96
z_critico_sup = norm.ppf(1 - (1 - nivel_confianca) / 2) # Dá +1.96

# 3. Gerar dados para a linha da curva (eixo X e Y)
x = np.linspace(-4, 4, 1000) # Criar 1000 pontos entre -4 e 4
y = norm.pdf(x, media, desvio_padrao) # Calcular a densidade de probabilidade (PDF)

# 4. Iniciar a plotagem
plt.figure(figsize=(12, 6))

# Plotar a linha azul da distribuição
plt.plot(x, y, color='blue', label='Distribuição Normal Padrão (Z)')

# 5. Sombrear a área de confiança (os 95%)
# Criar os pontos X específicos para a área sombreada
x_sombra = np.linspace(z_critico_inf, z_critico_sup, 500)
y_sombra = norm.pdf(x_sombra, media, desvio_padrao)
plt.fill_between(x_sombra, y_sombra, color='green', alpha=0.3, label='95% de Confiança')

# 6. Adicionar linhas verticais nos pontos críticos 1.96 e -1.96
plt.axvline(x=z_critico_inf, color='red', linestyle='--', linewidth=1.5)
plt.axvline(x=z_critico_sup, color='red', linestyle='--', linewidth=1.5)

# 7. Anotações e Textos no Gráfico
# Anotar os valores de Z
plt.text(z_critico_inf - 0.1, -0.02, f'{z_critico_inf:.2f}', color='red', ha='right', fontweight='bold')
plt.text(z_critico_sup + 0.1, -0.02, f'{z_critico_sup:.2f}', color='red', ha='left', fontweight='bold')

# Anotar a porcentagem central
plt.text(media, 0.15, '95%', color='green', fontsize=20, ha='center', fontweight='bold')

# Anotar as caudas (2.5% cada)
plt.text(z_critico_inf - 0.5, 0.05, '2.5%', color='black', ha='center')
plt.text(z_critico_sup + 0.5, 0.05, '2.5%', color='black', ha='center')

# Títulos e legendas
plt.title('Distribuição Normal Padrão: O Significado do Z=1,96', fontsize=16)
plt.xlabel('Desvios Padrão (Valor Z)')
plt.ylabel('Densidade de Probabilidade')
plt.legend(loc='upper right')
plt.grid(axis='x', alpha=0.3)

# Mostrar o gráfico
plt.tight_layout()
plt.show()