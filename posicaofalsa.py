def f(x):
    # Função alvo f(x)
    return x**4 - 2.36343 * x**3 - 18.1163 * x**2 + 20.7595 * x + 58.8273

# Função para encontrar intervalos com mudança de sinal
def encontrar_intervalos(f, x_min, x_max, passo=0.5):
    intervalos = []
    x_atual = x_min

    while x_atual < x_max:
        x_prox = x_atual + passo
        if f(x_atual) * f(x_prox) < 0:
            intervalos.append((x_atual, x_prox))
        x_atual = x_prox

    return intervalos

# Método da Posição Falsa
def posicao_falsa(a, b, tol=0.001, max_iter=1000):
    if f(a) * f(b) > 0:
        print(f"O intervalo [{a}, {b}] não contém uma raiz.")
        return None

    for _ in range(max_iter):
        # Calcula o ponto de aproximação pela posição falsa
        c = b - (f(b) * (b - a)) / (f(b) - f(a))

        # Critério de parada
        if abs(f(c)) < tol:
            return c

        # Atualiza o intervalo com base na mudança de sinal
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Número máximo de iterações atingido.")
    return None

# Definindo os limites de busca e o passo
x_min, x_max = -10, 10
passo = 0.5

# Encontrando intervalos candidatos a conter raízes
intervalos_encontrados = encontrar_intervalos(f, x_min, x_max, passo)
print("Intervalos encontrados:", intervalos_encontrados)

# Encontrando as raízes nos intervalos identificados
raizes = []
for (a, b) in intervalos_encontrados:
    raiz = posicao_falsa(a, b)
    if raiz is not None:
        # Arredonda para evitar duplicatas próximas
        raiz = round(raiz, 6)
        if raiz not in raizes:
            raizes.append(raiz)

# Exibindo as raízes encontradas
print("As raízes encontradas são:", raizes)
