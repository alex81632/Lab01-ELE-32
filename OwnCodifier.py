def hamming_like_encoder(data):
    # Calcular o número de bits de paridade
    m = 3
    # Calcular o tamanho total da palavra-código
    n = len(data) + m

    # Criar uma tabela de verificação de paridade
    parity_positions = [0, 1, 3]

    # Inicializar a palavra-código com todos os bits como 0
    codeword = [0] * n

    # Preencher os bits de dados na palavra-código
    codeword[2] = data[0]
    codeword[4] = data[1]
    codeword[5] = data[2]
    codeword[6] = data[3]

    # Calcular os bits de paridade
    for i in range(m):
        # Calcular a soma de verificação de paridade para a posição atual
        xor_sum = 0
        for j in range(n):
            if j & (1 << i):
                xor_sum ^= codeword[j - 1]
        codeword[parity_positions[i] - 1] = xor_sum

    return codeword

# Exemplo de uso
data_input = [1, 0, 1, 0]  # 4 bits de dados
encoded_codeword = hamming_like_encoder(data_input)
print("Palavra-código codificada:", encoded_codeword)

def hamming_like_decoder(codeword):
    # Calcular o número de bits de paridade
    m = 3
    # Calcular o tamanho total da palavra-código
    n = len(codeword)

    # Criar uma tabela de verificação de paridade
    parity_positions = [0, 1, 3]

    # Verificar a paridade da palavra-código
    error_position = 0
    for i in range(m):
        xor_sum = 0
        for j in range(n):
            if j & (1 << i):
                xor_sum ^= codeword[j - 1]
        if xor_sum != codeword[parity_positions[i] - 1]:
            error_position += parity_positions[i]

    # Se a posição do erro for diferente de zero, um erro foi detectado
    if error_position != 0:
        print("Erro detectado na posição:", error_position)
    else:
        print("Nenhum erro detectado.")

# Exemplo de uso
received_codeword = [0, 0, 1, 0, 0, 1, 1]  # Palavra-código recebida
hamming_like_decoder(received_codeword)

