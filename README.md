# Sistema de Autenticação

## O que foi feito

Criei um sistema de login e autenticação em Flask seguindo o padrão MVC. O projeto tem login seguro, controle de acesso e algumas regras de segurança.

## O que funciona

- Login com email e senha
- Senha guardada com hash (não fica visível no banco)
- Se errar a senha 3 vezes, o usuário fica bloqueado
- Login só funciona entre 08h da manhã e 18h (até as 6 da tarde)
- Na primeira vez que loga, é obrigado a trocar a senha
- Dashboard que só abre se tiver logado
- Logout que limpa a sessão

## Como rodar

1. Abra PowerShell na pasta do projeto

2. Rode o setup do banco:
```powershell
python setup_db.py
```

3. Inicie o servidor:
```powershell
python app.py
```

4. Abra no navegador:
```
http://localhost:5001
```

## Usuário para testar

- Email: `admin@gmail.com`
- Senha: `teste`

Na primeira vez vai pedir para mudar a senha.

## Organização do código

- `app.py` - arquivo principal do Flask
- `config.py` - configurações (banco, senha da app)
- `models/usuario_model.py` - funções que mexem com o banco de dados
- `controllers/auth_controller.py` - lógica de login e redirecionamentos
- `views/templates/` - páginas HTML
- `static/style.css` - estilo das páginas

## Technologias usadas

- Flask (framework web)
- SQLite (banco de dados)
- Werkzeug (para criptografar senha)
