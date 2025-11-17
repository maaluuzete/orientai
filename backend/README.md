# Backend - OrientAI

## Rodar localmente

1. Criar e ativar o ambiente virtual, instalar dependências e rodar o servidor:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
## Como funciona
2. API
    - Função recomendacao(data)
        Esta é a função principal da aplicação responsável por *analisar os dados do aluno* e *gerar recomendações personalizadas de cursos e áreas*.
    - GET/
        Rota de teste.
        Retorna uma mensagem avisando que a API está funcionando.  
    - POST /api/recommend
        Rota principal que retorna as recomendações.
        Recebe os dados de um aluno e retorna as recomendações de cursos e áreas.
        Variáveis utilizadas:
            * `USE_MOCK`, Ativa o modo de respostas simuladas, sem a IA real.
            * `HFURL`, URL da API de IA externa.
            * `HFKEY`, Chave de autenticação da API de IA.