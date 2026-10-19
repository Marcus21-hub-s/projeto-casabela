# 🛋️️ CasaBela - Catálogo Online de Móveis 🛋️

Um sistema web desenvolvido para a loja **CasaBela**, com foco na apresentação de um catálogo online de móveis. O projeto permite a visualização geral dos itens disponíveis e navegação detalhada por produto, além de interface de administração para gerenciamento do acervo.

> **Projeto Acadêmico / Prático**
> Desenvolvido para a disciplina de Frameworks Back-End, utilizando **Django**.

---

Grupo:
- Gabriel Andrade: 01803645
- Marcus Vinícius: 01813459
- Mayara Rayanne: 01852552
- Irlania Felix: 01808910
- Micaías Alexandre: 01825976
- Welson Dias: 01809689

## Funcionalidades

- [x] **Catálogo Geral:** Listagem de móveis com filtro e suporte a imagens/thumbnails.
- [x] **Página de Detalhes:** Exibição completa de informações do móvel (descrição, dimensões, material, preço, fotos).
- [x] **Painel Administrativo:** Interface do Django Admin para criação, edição e remoção de produtos e categorias.
- [x] **Navegação Responsiva:** Layout adaptável para dispositivos móveis e desktops.

---

## Tecnologias

- **Linguagem:** Python
- **Framework Back-End:** Django
- **Banco de Dados:** SQLite (Desenvolvimento)
- **Front-End:** HTML5, CSS3 / Bootstrap
- **Gerenciamento de Dependências:** `pip` / `venv`

---

## 📌 Funcionalidades Requisitadas e Implementadas

1. **Estrutura Django:** Projeto Django (`casabela`) configurado com a aplicação `moveis`.
2. **Modelo de Dados (`Movel`):** Implementação do model no `models.py` e execução das respetivas migrações (`makemigrations` e `migrate`).
3. **Painel de Administração:** Registo do modelo no `admin.py` e cadastro de pelo menos 8 móveis de exemplo através do Django Admin.
4. **Listagem Geral (`index.html`):** View que procura todos os registos (`Model.objects.all()`) e exibe-os numa tabela HTML com colunas para cada campo.
5. **Página de Detalhes (`detalhe.html`):** Rota dinâmica (`/moveis/<int:id>`) e view que obtém um único registo (`Model.objects.get(id=id)`) exibindo todos os seus dados.
6. **Navegação Dinâmica:** Links nos nomes dos itens da tabela a redirecionar para a página de detalhes através do tag `{% url %}`.
7. **Estilização Personalizada:** Aplicação de ficheiro de estilos estático (`static/css/estilos.css`) em todas as páginas.
8. **Imagens Estáticas:** Inclusão de imagens em `static/images/` exibidas nos templates utilizando o tag `{% static %}`.
9. **Ficheiro JavaScript:** Script em `static/js/script.js` com função executada via botão no template.
10. **Testes de Ambiente:** Testes de funcionamento em modo de desenvolvimento (`DEBUG = True`) e produção (`DEBUG = False`, com execução prévia do `collectstatic`).

---

## 🗃️ Especificação do Model `Movel`

O modelo `Movel` foi definido em `moveis/models.py` com os seguintes campos:

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | `CharField` | Nome do móvel |
| `preco` | `DecimalField` | Preço de venda |
| `estoque` | `IntegerField` | Quantidade em stock |
| `material` | `CharField` | Material (ex.: madeira, metal, mdf) |

---

## Estrutura do Projeto

```text
projeto-casabela/
│
├── casabela/                  # Configurações globais do projeto Django
├── moveis/                    # App, templates, estáticos e migrações
├── manage.py                  # Comandos de gerenciamento do Django
├── README.md                  # Documentação do repositório
└── .gitignore                 # Arquivos locais não versionados
```
