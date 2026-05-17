# 🕐 Ponto Fácil

Sistema web de registro de ponto desenvolvido com Python e Flask, como projeto extensionista - IPOG.

---

## 📋 Sobre o Projeto

O **Ponto Fácil** é um sistema simples e funcional para registro de entrada e saída de funcionários, com histórico de registros e filtro por período. Desenvolvido com foco em usabilidade e praticidade para pequenos negócios.

---


## ✅ Funcionalidades

- Cadastro e login de usuários
- Registro de entrada e saída com data e hora automáticos
- Histórico de registros com filtro por período (data início e data fim)
- Confirmação visual ao registrar ponto
- Interface responsiva e amigável

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask** — framework web
- **SQLite** — banco de dados
- **HTML e CSS** — interface do usuário

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/jessika-souzaa/Ponto_facil.git
cd Ponto_facil
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

> No Windows use: `venv\Scripts\activate`

### 3. Instale as dependências

```bash
pip install flask
```

### 4. Inicie o sistema

```bash
python app.py
```

### 5. Acesse no navegador

```
http://127.0.0.1:5000
```

---

## 📁 Estrutura do Projeto

```
ponto_facil/
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── cadastro.html
│   ├── painel.html
│   ├── historico.html
│   └── sucesso.html
├── app.py
├── database.db
└── database.py
``` 

