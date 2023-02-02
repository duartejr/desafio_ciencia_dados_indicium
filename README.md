# Desafio de Ciência de dados da Indicium

Objetivo:

 Identificar quais máquinas apresentam potencial de falha tendo como base dados extraídos através de sensores durante o processo de manufatura. 
 Para isso são fornecidos dois datasets: um dataset chamado desafio_manutencao_preditiva_treino composto por 6667 linhas, 9 colunas de informação (features) 
 e a variável a ser prevista (“failure_type”). 
 
 Descrição dos arquivos do projeto:
 
 ( O arquivo `01_analise_exploratoria.ipynb` contém a análise exploratória dos dados.
 * O arquivo `02_modelagem.ipynb` contém o processe de construção do modelo de seleção. Quatro modelos foram testados e no final escolhido o de melhor desempenho.
 * O arquivo `03_otimizacao_modelo.ipynb' contém as tentativas e melhorar o desempenho do modelo selecionado.
 * O arquivo `04_pipeline_modelo.ipynb`contém a construção da pipeline de execução do modelo.
 * O arquivo `05_modelo_previsao_falhas.py` é respnsável por executar o modelo de classificação.
 * O arquivo `modelo_pred_falhas.pkl` é o arquivo serial do modelo de classificação criado.
 * O arquivo `label_encoder.pkl` é o encoder utilizado para a conversão das tipos de falhas em valores numéricos.
 * O arquivo `requirements.txt` contém a lista de pacotes necessários para executar o modelo. A versão do Python utilizada foi a 3.10.9
 * Os arquivos `desafio_manutencao_preditiva_treino.csv` e `desafio_manutencao_preditiva_teste.csv` são os dados de treino e teste do modelo.
 * O arquivo `predicted.csv` é a resposta do modelo.
 
 
 Como usar o modelo.
 
 Para utiliza o modelo de previsão basta chamá-lo no terminal passando o caminho do arquivo com os dados.
 Exemplo:
 No se temrinal digite:
 `python 05_modelo_cassificacao_falhas.py desafio_manutencao_preditiva_teste.csv`
 
 Pressione enter e o modelo será executado. Como resultado será gerado o arquivo `predicted.csv` no mesmo diretório em que está o script do modelo.
