import os
from dotenv import load_dotenv

from langchain_openai import (
    ChatOpenAI,
    OpenAIEmbeddings
)

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import (
    Chroma
)

# ======================
# CONFIGURAÇÃO
# ======================

load_dotenv()

API = os.getenv(
    "OPENAI_API_KEY"
)

if not API:
    print(
        "\nERRO: Configure OPENAI_API_KEY no .env"
    )
    exit()

PASTA = "documentos"

# ======================
# CRIAR PASTA
# ======================

if not os.path.exists(PASTA):

    os.mkdir(PASTA)

    print(
        "\nPasta documentos criada."
    )

# ======================
# CARREGAR PDFs
# ======================

print("\nLendo documentos...")

docs = []

arquivos = os.listdir(
    PASTA
)

for arquivo in arquivos:

    caminho = os.path.join(
        PASTA,
        arquivo
    )

    if not arquivo.lower().endswith(
        ".pdf"
    ):
        continue

    try:

        if os.path.getsize(
            caminho
        ) == 0:

            print(
                f"Pulando {arquivo} (vazio)"
            )

            continue

        print(
            f"Lendo: {arquivo}"
        )

        loader = PyPDFLoader(
            caminho
        )

        documento = loader.load()

        docs.extend(
            documento
        )

    except Exception as erro:

        print(
            f"Erro em {arquivo}"
        )

        print(
            erro
        )

if len(docs) == 0:

    print(
        "\nNenhum PDF válido encontrado."
    )

    print(
        "Coloque arquivos PDF dentro da pasta documentos/"
    )

    exit()

print(
    f"\n{len(docs)} páginas carregadas"
)

# ======================
# DIVIDIR TEXTO
# ======================

print(
    "\nPreparando documentos..."
)

splitter = (
    RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
)

partes = splitter.split_documents(
    docs
)

print(
    f"{len(partes)} partes criadas"
)

# ======================
# MEMÓRIA
# ======================

print(
    "\nCriando memória..."
)

banco = Chroma.from_documents(
    documents=partes,
    embedding=OpenAIEmbeddings()
)

print(
    "Memória pronta"
)

# ======================
# IA
# ======================

ia = ChatOpenAI(
    model="gpt-5"
)

print(
    "\n=== AGENTE DE ATENDIMENTO ==="
)

print(
    "Digite 'sair' para encerrar"
)

# ======================
# CHAT
# ======================

while True:

    pergunta = input(
        "\nCliente: "
    )

    if (
        pergunta.lower()
        ==
        "sair"
    ):
        break

    try:

        encontrados = (
            banco.similarity_search(
                pergunta,
                k=3
            )
        )

        contexto = "\n\n".join(
            [
                x.page_content
                for x in encontrados
            ]
        )

        prompt = f"""
Você é um atendente virtual.

Responda SOMENTE
com base nos documentos.

Se não existir informação,
fale que não encontrou.

DOCUMENTOS:

{contexto}

PERGUNTA:

{pergunta}
"""

        resposta = (
            ia.invoke(
                prompt
            )
        )

        print(
            "\nIA:"
        )

        print(
            resposta.content
        )

    except Exception as erro:

        print(
            "\nErro:"
        )

        print(
            erro
        )