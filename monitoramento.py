import sqlite3

def newton_cooling(T, Tamb, k):
    """Calcula a derivada da temperatura segundo a Lei de Resfriamento de Newton."""
    return -k * (T - Tamb)

def run_simulation():
    # Parametros da simulacao
    k = 0.1
    Tamb = 20.0
    t0, tf = 0.0, 50.0
    y0 = 100.0
    n_iteracoes = 10
    dt = (tf - t0) / n_iteracoes

    # Conexao com banco de dados SQLite
    conn = sqlite3.connect('monitoramento.db')
    cursor = conn.cursor()

    # Criacao da tabela
    cursor.execute('DROP TABLE IF EXISTS log_sensores')
    cursor.execute('''CREATE TABLE log_sensores (id INTEGER PRIMARY KEY AUTOINCREMENT, tempo REAL, temperatura REAL)''')

    # Aplicacao do Metodo de Euler
    t = t0
    y = y0
    for i in range(n_iteracoes + 1):
        # Insercao dos dados calculados no banco
        cursor.execute('INSERT INTO log_sensores (tempo, temperatura) VALUES (?, ?)', (t, y))
        
        # Calculo do proximo passo usando Euler: y(n+1) = y(n) + dt * f(t, y)
        dy = newton_cooling(y, Tamb, k)
        y = y + dy * dt
        t = t + dt

    conn.commit()

    # Verificacao dos dados persistidos
    print("Dados persistidos no banco de dados:")
    cursor.execute('SELECT * FROM log_sensores')
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Tempo: {row[1]:.2f}s | Temperatura: {row[2]:.2f}C")

    conn.close()

if __name__ == "__main__":
    run_simulation()