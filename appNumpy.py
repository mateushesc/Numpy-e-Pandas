import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leitura
df = pd.read_csv("Salary_data.csv)")
print(df.head())

# Converter dados para array
experience = df['YearsExperience'].to_numpy()
salary = df['Salary'].to_numpy()

print(experience[:5], salary[:5])

# Calculo média dos salários
mean_salary = np.mean(salary)
print(f"Média de salários: {mean_salary}")

# Calculo média da experiência
mean_experienece = np.mean(experience)
print(f"Média de experiência: {mean_experience} em anos")

# Filtro funcionários mais que 5 anos
salary_above_5years = salary[experience > 5]

# Salário médio acima de 5 anos
mean_salary_above5 = np.mean
(salary_above_5years)
print(f"O salário médio funcionários mais que 5 anos: {mean_salary_above5}")

# Criar gráfico barras
plt.figure(figsize(10,6))
plt.bar(experience, salary, color='skyblue')
plt.title("Relação Salário | Experiência")
plt.xlabel('Experiência (em anos):')
plt.ylabel('Salário')
plt.show()

# Aumento 10% salários
salary_increase = salary *1.10

# Mostrar novo salário
print("Salários após aumento(10%):")
print(salary_increase)

# Gráfico comparação salários (originais e com aumento)

plt.figure(figsize(10,6))
plt.bar(experience, salary, color='lightgreen', label='Salário original')
plt.bar(experience, salary_increase, color='orange', alpha=0.7, label="Salário com aumento (10%)")
plt.title('Salário original | Salário com aumento')
plt.xlabel('Experiencia (em anos)')
plt.ylabel('Salário')
plt.legend()
plt.show()