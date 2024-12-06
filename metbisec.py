# Definindo a função
def f(x):
    # Função alvo f(x)
    return x**4 - 2.36343 * x**3 - 18.1163 * x**2 + 20.7595 * x + 58.8273

# Função para encontrar intervalos com mudanças de sinal
def encontrar_intervalos(f, x_min, x_max, passo=0.5):
    intervalos = []
    x = x_min
    while x < x_max:
        if f(x) * f(x + passo) < 0:  # Há mudança de sinal entre x e x + passo
            intervalos.append((x, x + passo))
        x += passo
    return intervalos

# Método da Bisseção
def bissecao(a, b, tol=0.001, max_iter=1000):
    if f(a) * f(b) >= 0:
        print(f"O intervalo [{a}, {b}] não contém uma raiz.")
        return None
    
    for _ in range(max_iter):
        # Ponto médio do intervalo
        c = (a + b) / 2
        f_c = f(c)

        # Critério de parada
        if abs(f_c) < tol:
            return c
        
        # Decide o próximo intervalo
        if f(a) * f_c < 0:
            b = c
        else:
            a = c

    print("Número máximo de iterações atingido.")
    return None

# Definindo o intervalo para busca e o passo
x_min, x_max = -100, 100  # Intervalo maior para busca
passo = 0.5  # Intervalo de busca entre cada ponto

# Encontrando intervalos com mudanças de sinal
intervalos_encontrados = encontrar_intervalos(f, x_min, x_max, passo)
print("Intervalos com mudanças de sinal:", intervalos_encontrados)

# Aplicando o método da bisseção nos intervalos encontrados
raizes = []
for (a, b) in intervalos_encontrados:
    raiz = bissecao(a, b)
    if raiz is not None:
        # Arredonda para evitar duplicatas próximas
        raiz = round(raiz, 6)
        if raiz not in raizes:
            raizes.append(raiz)

# Exibindo as raízes encontradas
print("As raízes encontradas são:", raizes)
