import pandas as pd
import numpy as np
import requests


# Dataset
df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

# Qual o tamanho desse dataset?
print("O tamanho do dataset é {}".format(df.shape))

# Qual a média da coluna windspeed?
print("A média da coluna windspeed é {}".format(df["windspeed"].mean()))

#  Qual a média da coluna temp?
print("A média da coluna temp é {}". format(df["temp"].mean()))

#  Quantos registros existem para o ano de 2011?
df["datetime"] = pd.to_datetime(df["datetime"])
df_2011 = df[df["datetime"] >= "2011-01-01"]
df_2011 = df_2011[df_2011["datetime"] <= "2011-12-31"]
print("Existem {} registros em 2011".format(df_2011["datetime"].count()))

#  Quantos registros existem para o ano de 2012?
df["datetime"] = pd.to_datetime(df["datetime"])
df_2012 = df[df["datetime"] >= "2012-01-01"]
df_2012 = df_2012[df_2012["datetime"] <= "2012-12-31"]
print("Existem {} registros em 2012".format(df_2012["datetime"].count()))

# Quantas locações de bicicletas foram efetuadas em 2011?
print("Foram realizados {} aluguéis.".format(df_2011["total_count"].sum()))

# Quantas locações de bicicletas foram efetuadas em 2012?
print("Foram realizados {} aluguéis.".format(df_2012["total_count"].sum()))

# Qual estação do ano contém a maior média de locações de bicicletas?
# season: estação do ano (1: inverno, 2: primavera, 3: verão, 4: outono). Relativo ao hemisfério norte;
season_dict = {}
for x in range (1, 5):
    df_season = df[df["season"] == x]
    season_dict[x] = df_season["total_count"].mean()
df_season = pd.DataFrame(list(season_dict.items()),columns = ['Estação','Média'])
print(df_season)
print("\nA maior média é de {} aluguéis de bicicleta.".format(max(df_season["Média"])))

# Qual estação do ano contém a menor média de locações de bicicletas?
# season: estação do ano (1: inverno, 2: primavera, 3: verão, 4: outono). Relativo ao hemisfério norte;
print("A menor média é de {} aluguéis de bicicleta.".format(min(df_season["Média"])))

#  Qual horário do dia contém a maior média de locações de bicicletas?
hour_dict = {}
for x in range (24):
    df_hour = df[df["hour"] == x]
    hour_dict[x] = df_hour["total_count"].mean()
df_hour = pd.DataFrame(list(hour_dict.items()),columns = ['Hora','Média'])
print(df_hour)
print("\nA maior média é de {} aluguéis de bicicleta.".format(max(df_hour["Média"])))

#  Qual horário do dia contém a menor média de locações de bicicletas?
print("A menor média é de {} aluguéis de bicicleta.".format(min(df_hour["Média"])))

#  Que dia da semana contém a maior média de locações de bicicletas?
# weekday: dia da semana (0: domingo, 1: segunda-feira, …, 6: sábado);
week_dict = {}
for x in range (7):
    df_week = df[df["weekday"] == x]
    week_dict[x] = df_week["total_count"].mean()
df_week = pd.DataFrame(list(week_dict.items()),columns = ["Dia da Semana","Média"])
print(df_week)
print("\nA maior média é de {} aluguéis de bicicleta.".format(max(df_week["Média"])))

#  Que dia da semana contém a menor média de locações de bicicletas?
# weekday: dia da semana (0: domingo, 1: segunda-feira, …, 6: sábado);
print("A menor média é de {} aluguéis de bicicleta.".format(min(df_week["Média"])))

#  Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?
df_quarta = df[df["weekday"] == 3]
hour_dict = {}
for x in range (24):
    df_hour = df_quarta[df_quarta["hour"] == x]
    hour_dict[x] = df_hour["total_count"].mean()
df_hour = pd.DataFrame(list(hour_dict.items()),columns = ['Hora','Média'])
print(df_hour)
print("\nA maior média é de {} aluguéis de bicicleta nas quartas-feiras.".format(max(df_hour["Média"])))

# Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?
df_sabado = df[df["weekday"] == 6]
hour_dict = {}
for x in range (24):
    df_hour = df_sabado[df_sabado["hour"] == x]
    hour_dict[x] = df_hour["total_count"].mean()
df_hour = pd.DataFrame(list(hour_dict.items()),columns = ['Hora','Média'])
print(df_hour)
print("\nA maior média é de {} aluguéis de bicicleta nas quartas-feiras.".format(max(df_hour["Média"])))