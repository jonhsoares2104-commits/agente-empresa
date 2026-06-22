# Agente de Atendimento IA

Sistema de atendimento automático com IA em Python.

Este projeto lê documentos PDF da empresa e responde perguntas dos clientes usando inteligência artificial.

## Funcionalidades

* Leitura automática de PDFs
* Busca de informações nos documentos
* Atendimento automático
* Respostas baseadas no conteúdo da empresa
* Sistema RAG (Retrieval Augmented Generation)

## Tecnologias

* Python
* LangChain
* OpenAI
* ChromaDB
* PyPDF
* Dotenv

## Instalação

Clone o projeto:

```bash
git clone https://github.com/SEU_USUARIO/agente-empresa.git
```

Entre na pasta:

```bash
cd agente-empresa
```

Instale dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env`:

```env
OPENAI_API_KEY=sua_chave
```

## Estrutura

```text
agente-empresa/
│
├── app.py
├── requirements.txt
├── .env
└── documentos/
    └── empresa.pdf
```

## Como usar

Coloque arquivos PDF dentro da pasta:

```text
documentos/
```

Execute:

```bash
python app.py
```

Exemplo:

```text
Cliente:
Qual o horário?

IA:
Segundo os documentos, o horário é das 08:00 às 18:00.
```

## Licença

Licença MIT.
