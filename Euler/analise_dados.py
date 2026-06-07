import sqlite3

def calcular_estatisticas():
    # 1. Estabelece conexão com o banco de dados SQLite
    # Certifique-se de que o nome do arquivo seja o mesmo usado no monitoramento.py
    conn = sqlite3.connect('monitoramento.db')
    cursor = conn.cursor()

    try:
        # 2. Execução da query SQL para média térmica
        query_avg = "SELECT AVG(temperatura) FROM log_sensores"
        cursor.execute(query_avg)
        
        # fetchone() retorna uma tupla, pegamos o primeiro elemento [0]
        media_termica = cursor.fetchone()[0]

        # 3. Query adicional: Amplitude térmica (Máxima e Mínima)
        cursor.execute("SELECT MIN(temperatura), MAX(temperatura) FROM log_sensores")
        t_min, t_max = cursor.fetchone()

        print("--- Relatório de Análise de Dados (Projeto Karina) ---")
        print(f"Média Térmica do Período: {media_termica:.2f}°C")
        print(f"Temperatura Máxima Registrada: {t_max:.2f}°C")
        print(f"Temperatura Mínima Registrada: {t_min:.2f}°C")
        print("-" * 50)

    except sqlite3.OperationalError as e:
        print(f"Erro: A tabela ou o banco de dados não foram encontrados. {e}")
    
    finally:
        # 4. Encerra a conexão para liberar o arquivo .db
        conn.close()

if __name__ == "__main__":
    calcular_estatisticas()