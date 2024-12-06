# Definindo a função e sua derivada
def f(x):
    # Função alvo f(x)
    return x**4 - 2.36343 * x**3 - 18.1163 * x**2 + 20.7595 * x + 58.8273

def df(x):
    # Derivada de f(x)
    return 4 * x**3 - 3 * 2.36343 * x**2 - 2 * 18.1163 * x + 20.7595

# Método de Newton-Raphson
def newton_raphson(x0, tol=0.001, max_iter=1000):
    # Começando com o valor inicial x0
    x = x0
    for _ in range(max_iter):
        fx = f(x)      # Calcula f(x)
        dfx = df(x)    # Calcula f'(x)
        
        if dfx == 0:
            # Caso a derivada seja zero, o método falha
            print("Derivada é zero, método falhou.")
            return None
        
        # Atualiza o valor de x com a fórmula de Newton-Raphson
        x_novo = x - fx / dfx
        
        # Critério de parada: se o valor de f(x) for menor que a tolerância (0.001)
        if abs(f(x_novo)) < tol:
            return x_novo
        
        # Atualiza x para a próxima iteração
        x = x_novo
    
    print("Número máximo de iterações atingido.")
    return None

# Encontrando as raízes
# Testamos valores iniciais diferentes para tentar encontrar todas as raízes
chutes_iniciais = [-5, -2, 2, 5]
raizes = []

for chute in chutes_iniciais:
    raiz = newton_raphson(chute)
    if raiz is not None:
        # Arredonda para evitar duplicação de raízes próximas
        raiz = round(raiz, 6)
        if raiz not in raizes:
            raizes.append(raiz)

print("As raízes encontradas são:", raizes)
