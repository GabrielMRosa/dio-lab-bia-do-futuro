# Base de Conhecimento

## Dados Utilizados


| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Permite que Clara lembre interações anteriores e mantenha contexto nas conversas|
| `perfil_investidor.json` | JSON | Define o nível de risco do cliente para personalizar recomendações |
| `produtos_financeiros.json` | JSON | Contém informações oficiais sobre produtos disponíveis para sugestão |
| `transacoes.csv` | CSV | Registra receitas e despesas para análise de comportamento financeiro |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.


---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV e JSON são carregados no início da sessão do usuário. Quando o cliente inicia a conversa, o sistema busca seus dados financeiros (perfil, transações e histórico) na base e os organiza para uso pelo agente.

Esses dados não ficam fixos no modelo, mas são enviados conforme a necessidade da conversa.


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados relevantes são inseridos dinamicamente no contexto enviado ao modelo de IA.
O system prompt define o comportamento da Clara (tom, regras e limitações).
Já os dados do cliente são incluídos como contexto adicional sempre que for necessário fazer análises, simulações ou recomendações.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```

Dados do Cliente:
- Nome: João Silva
- Perfil de Investidor: Moderado
- Saldo disponível: R$ 5.000
- Meta ativa: Reserva de emergência (R$ 10.000)

Resumo do mês:
- Total de entradas: R$ 3.000
- Total de saídas: R$ 1.850

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Restaurante - R$ 120
- 08/11: Salário + R$ 3.000

Produtos disponíveis:
- CDB Liquidez Diária (baixo risco)
- Fundo Multimercado (risco moderado)
- Ações (alto risco)
```
