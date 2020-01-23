# Ai-Spreadsheet-Converter
Um Script para converter planilhas em treinamento de inteligência artificial no software bothub.it

Para melhor utilização deste script, você deverá ter instalado em sua máquina o python versão 3.8 ou superior;

1- Requisitos:<br>
	Repository uuid do seu repositório no bothub;<br>
	Authorization token da sua conta no bothub; 
    


2- Uso:<br>
    1- Para utilizar este repositório, é necessário ter uma planilha no modelo (.csv) separado por vírgula, na qual a primeira linha será <strong>text, intent</strong> <br>
    e as demais terão como primeiro argumento o texto e segundo a intenção no qual ele deverá ser implementado, como no exemplo a seguir:
    
        text, intent
        financeiro onde trabalhar,financeiro
        onde fica financeiro,financeiro
        onde um gestor financeiro pode trabalhar,financeiro
        mercado financeiro onde investir,financeiro

    2- logo após ter o arquivo .csv em seu computador copie para a pasta /spreadsheets e renomeie para inicial.csv
    3- para finalizar rode o comando abaixo:
        
        $python3 main.py --service 'examples' --repository_uuid '{{Seu repository_uuid}}' --auth_token '{{Seu Authorization Token}}'
