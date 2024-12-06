def f(x):
    # Função alvo f(x)
    return x**4 - 2.36343 * x**3 - 18.1163 * x**2 + 20.7595 * x + 58.8273

# Método da Secante
def secante(x0, x1, tol=0.001, max_iter=1000):
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Verificação para evitar divisão por zero
        if f_x1 - f_x0 == 0:
            print("Divisão por zero. Método da Secante falhou para o par inicial:", (x0, x1))
            return None

        # Cálculo da próxima aproximação
        x_novo = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # Critério de parada
        if abs(f(x_novo)) < tol:
            return x_novo

        # Atualiza x0 e x1 para a próxima iteração
        x0, x1 = x1, x_novo

    print("Número máximo de iterações atingido para o par inicial:", (x0, x1))
    return None

# Definindo intervalos para tentar encontrar todas as raízes
# Intervalos baseados em análise da função ou tentativa e erro
pares_iniciais = [(-5, -4), (-2, -1), (1, 2), (3, 5)]
raizes = []

# Encontrando as raízes
for (x0, x1) in pares_iniciais:
    raiz = secante(x0, x1)
    if raiz is not None:
        # Arredonda para evitar duplicatas próximas
        raiz = round(raiz, 6)
        if raiz not in raizes:
            raizes.append(raiz)

# Verificando se encontramos 4 raízes
if len(raizes) == 4:
    print("As quatro raízes encontradas são:", raizes)
else:
    print("Não foi possível encontrar quatro raízes distintas. Raízes encontradas:", raizes)
