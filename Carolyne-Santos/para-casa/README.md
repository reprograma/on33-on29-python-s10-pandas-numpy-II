# 📈📉📊🎲 Análise com Python - Pandas e Numpy II

## 📚 Descrição da Atividade

Exercicio para casa semana 12. Analise o dataset Employee.

## 📋 Passo a Passo

## 🟦 Atividade 1 - Use o arquivo `Employee.csv` para análise:

 ### - Bibliotecas Utilizadas:

# Bibliotecas

        # Biblioteca
        import pandas as pd
        import matplotlib.pyplot as plt

        # Carregando o arquivo 'Employee.csv'
        df = pd.read_csv(r"C:\Users\carol\OneDrive\Área de Trabalho\Reprograma\on33-python-s12-pandas-numpy-II\material\Employee.csv")

        # Visualizar df
        print(df.head())

## 🟦 Atividade 2 - Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos:

        # Visualizar Colunas
        print(df.columns)

        # Colunas
        # ['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC',
        #       'All Time Rank', 'Track Score', 'Spotify Streams',
        #       'Spotify Playlist Count', 'Spotify Playlist Reach',
        #       'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts',
        #       'TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach',
        #       'Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins',
        #       'Deezer Playlist Count', 'Deezer Playlist Reach',
        #       'Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations',
        #       'Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity',
        #       'Explicit Track']

        # Visualizar typos
        print(df.dtypes)

        # Selecionar as colunas numéricas:
        colunas_numericas = ["All Time Rank", "Track Score", "Spotify Streams", "Spotify Playlist Count", 
                            "Spotify Playlist Reach", "Spotify Popularity", "YouTube Views", "YouTube Likes", 
                            "TikTok Posts", "TikTok Likes", "TikTok Views", "YouTube Playlist Reach",
                            "Apple Music Playlist Count", "AirPlay Spins", "SiriusXM Spins", "Deezer Playlist Count", 
                            "Deezer Playlist Reach", "Amazon Playlist Count", "Pandora Streams",
                                "Pandora Track Stations", "Soundcloud Streams", "Shazam Counts", 
                                "TIDAL Popularity", "Explicit Track"]

        # Converter as colunas numéricas para Float64
        for colunas in colunas_numericas:
            df[colunas] = df[colunas].replace(",", "", regex=True).astype("Float64")

## 🟦 Atividade 3 - Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos:

        # Visualizar o formato dos dados da coluna 'Release Date'
        df["Release Date"] = pd.to_datetime(df["Release Date"], format="mixed")

        # Visualizar typos
        print(df.dtypes)

## 🟦 Atividade 4 - Agrupe os empregados por gênero e idade e crie um gráfico para cada caso:

        # Nova coluna 'Streaming Popularity' 
        df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)

## 🟦 Atividade 5 - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade:

        # Nova coluna 'Total Streams' 
        df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)

## 🟦 Atividade 6 - Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe):

        # Faixas filtradas
        faixas_filtradas = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]

## 🟦 Atividade 7 - Conte quantos empregados existem por `PaymentTier`:

        # Salvar df em formato json
        faixas_filtradas.to_json('faixas_filtradas.json', index=False)

## 🟦 Atividade 8 - Substitua os valores da coluna `EverBenched` para `True` ou `False`:

        # Carregando o arquivo 'faixas_filtradas.json', chamei de 'faixas'
        faixas = pd.read_json('C:/Users/carol/OneDrive/Área de Trabalho/Reprograma/on33-python-s11-pandas-numpy-I/Carolyne-Santos/para-casa/faixas_filtradas.json')

        # Visualizar
        print(faixas.head())

## 🟦 Atividade 9 - Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`:  


  
## 👩🏻‍🏫 Professora Manuelly Suzik.


 [![LinkdIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/manuellysuzik/)
</br>
 [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/manuellysuzik)</br>
