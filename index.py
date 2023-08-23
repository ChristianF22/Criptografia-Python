#Intalando a biblioteca = pip install cryptography

#Importando as classes e métodos necessários para criptografia AES
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Gere uma chave secreta para AES com 256 bits usando a função urandom
key = os.urandom(32)
print(key)

# Gere um IV (vetor de inicialização) para o modo CBC com 128 bits usando a função urandom
iv = os.urandom(16)
print(iv)

# Crie um objeto Cipher com o algoritmo AES, usando a chave e o IV fornecidos, no modo CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
print(cipher)

# Mensagem em texto simples que será criptografada
message = "Esta é uma mensagem, secretas! "

# Converte a mensagem em texto simples para bytes, para que possa ser manipulada pelo algoritmo
message_bytes = message.encode('utf-8')

print(message_bytes)


# Cria um objeto de preenchimento PKCS7 com blocos de 128 bits
padder = padding.PKCS7(128).padder()

# Preenche a mensagem para ter um tamanho múltiplo do tamanho do bloco (16 bytes para AES)
message_bytes_padded = padder.update(message_bytes) + padder.finalize()
print(message_bytes_padded)


# Criptografar: Cria um objeto encryptor e atualiza com os dados preenchidos, seguido de finalização
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message_bytes_padded) + encryptor.finalize()
print(ciphertext)


# Descriptografar: Cria um objeto decryptor e atualiza com o texto cifrado, seguido de finalização
decryptor = cipher.decryptor()
plaintext_padded = decryptor.update(ciphertext) + decryptor.finalize()
print(plaintext_padded)


# Cria um objeto de remoção de preenchimento PKCS7 com blocos de 128 bits
unpadder = padding.PKCS7(128).unpadder()
# Remove o preenchimento da mensagem descriptografada para restaurar o texto original
plaintext = unpadder.update(plaintext_padded) + unpadder.finalize()
print(plaintext)


#Decodifica os bytes para string
decodetext = plaintext.decode('utf-8')
# Imprime o texto claro
print("Texto claro:", decodetext)