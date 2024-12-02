from openai import OpenAI

client = OpenAI(
    api_key='API_Key'
)


def get_carro_ai_bio(modelo, marca, ano_fabricacao):
    menssage = '''
    Me mostre uma descriçao de venda para o carro {} {} {} em apenas 250 caracteres. fale coisas especificas deste modelo.

    '''
    
    menssage = menssage.format(modelo, marca, ano_fabricacao)
    resposta = client.chat.completions.create(

        messages=[
            {
                'role': 'user',
                'content': menssage
            }
        ],
        model='gpt-3.5-turbo',
        max_tokens=100,
        
    )
    return resposta['choices'][0]['text']