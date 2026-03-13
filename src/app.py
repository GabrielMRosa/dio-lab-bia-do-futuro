import json
import pandas as pd
import requests
import streamlit as st

# ========= CONFIGURAÇÃO =========

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"


# ========= CARREGAR DADOS =========

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ========= MONTAR CONTEXTO =========

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
# ========= SYSTEM PROMPT =========
SYSTEM_PROMPT = """Você é Clara, uma assistente financeira clara, objetiva e prestativa.

Seu objetivo é ajudar o usuário a organizar melhor seu dinheiro, entender sua situação financeira e tomar decisões mais conscientes.

Você deve agir de forma consultiva, simples e proativa, sempre explicando suas sugestões de maneira fácil de entender.

REGRAS:

1. Utilize apenas os dados fornecidos no contexto da conversa.
2. Nunca invente valores, taxas, rendimentos ou informações financeiras.
3. Se não houver dados suficientes para responder com segurança, informe claramente a limitação.
4. Não faça recomendações de investimento sem verificar o perfil do cliente.
5. Explique o motivo de cada sugestão feita.
6. Não realize movimentações financeiras, apenas oriente.
7. Mantenha linguagem simples, clara e profissional.
8. Evite termos técnicos complexos. Quando necessário, explique de forma breve.

Se o usuário fizer uma pergunta fora do contexto financeiro ou sem dados suficientes, responda educadamente que não pode ajudar com aquela solicitação.

Seu papel é orientar, não decidir pelo usuário.
"""

# ========= CHAMAR OLLAMA =========

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""

    r = requests.post(OLLAMA_URL, json={
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    })

    return r.json()['response']

# ========= INTERFACE =========
st.title("Clara, Sua Educadora Financeira")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

        
