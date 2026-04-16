from werkzeug.security import generate_password_hash

def gerar():
    senha = input("Digite a senha: ")
    hash_senha = generate_password_hash(senha, method='pbkdf2:sha256', salt_length=5)
    print("\nSenha criptografada:\n")
    print(hash_senha)

if __name__ == "__main__":
    gerar()