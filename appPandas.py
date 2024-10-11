import pandas as pd
import matplotlib.pyplot as plt

# Leitura
df = pd.read_csv('Netflix TV Shows and Movies.csv')

# Converter dados para array
movies = df[df['type'] == 'MOVIE']
shows = df[df['type'] == 'SHOW']

# Printar 10 itens do início do dataset
print("10 primeiros itens do dataset:")
print(df.head(10))

# Printar 10 itens do final do dataset
print("10 últimos itens do dataset:")
print(df.tail(10))

# Pegar filme com maior imdb e o com menor
max_imdb = df[df['imdb_score'] == df['imdb_score'].max()][['title', 'imdb_score']]
min_imdb = df[df['imdb_score'] == df['imdb_score'].min()][['title', 'imdb_score']]

print("Filme com maior IMDB:")
print(max_imdb)

print("Filme com menor IMDB:")
print(min_imdb)

# Coluna runtime para numérico
df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')

# Calculo duração média
mean_movie_runtime = movies['runtime'].mean()
mean_show_runtime = shows['runtime'].mean()

print(f"A média da duração de filmes é: {mean_movie_runtime:.2f} minutos")
print(f"A média de duração dos shows de TV é: {mean_show_runtime:.2f} minutos")

# Show TV com maior duração por episódio e filme com maior duração
longest_show = shows[shows['runtime'] == shows['runtime'].max()]
longest_movie = movies[movies['runtime'] == movies['runtime'].max()]

if not longest_show.empty:
    print("Show de TV com maior duração por episódio:")
    print(longest_show[['title', 'runtime']])
else:
    print("Não foi possível encontrar shows com duração válida.")

if not longest_movie.empty:
    print("Filme com maior duração:")
    print(longest_movie[['title', 'runtime']])
else:
    print("Não foi possível encontrar filmes com duração válida.")

# Ano com mais filmes avaliados
df = df.dropna(subset=['release_year'])
movies_by_year = movies.groupby('release_year')['imdb_score'].count()

if not movies_by_year.empty:
    max_movies_year = movies_by_year.idxmax()
    print(f"Ano com mais filmes avaliados no IMDB: {max_movies_year}")
else:
    print("Sem dados suficientes para calcular ano com mais filmes.")

# Categorias de idade e quantidade de filmes por categoria
age_certification_counts = df['age_certification'].value_counts()
print("Categorias de idade e quantidade de filmes ou shows por categoria:")
print(age_certification_counts)

# Campos vazios e quantidade de vazios
missing_data = df.isnull().sum()
print("Colunas nulas:")
print(missing_data[missing_data > 0])

# Gráfico média IMDB ao longo do tempo
plt.figure(figsize=(10, 6))
movies_by_year_score = movies.groupby('release_year')['imdb_score'].mean()
shows_by_year_score = shows.groupby('release_year')['imdb_score'].mean()

plt.plot(movies_by_year_score.index, movies_by_year_score.values, label='Filmes', color='b', marker='o')
plt.plot(shows_by_year_score.index, shows_by_year_score.values, label="Shows", color='g', marker='x')

plt.title("Média IMDB ao longo do tempo")
plt.xlabel('Ano de lançamento')
plt.ylabel('Média IMDB')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico proporção de votos em shows e filmes
plt.figure(figsize=(10, 6))
votes_movies = movies['imdb_votes'].sum()
votes_shows = shows['imdb_votes'].sum()

labels = ['Filmes', 'Shows TV']
sizes = [votes_movies, votes_shows]
colors = ['blue', 'green']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Proporção de votos em shows e filmes')
plt.axis('equal')
plt.show()
