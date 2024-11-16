import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних із CSV
file_path = 'comptage_velo_2018.csv'  # Замініть на шлях до вашого файлу

fixed_df = pd.read_csv(file_path,
                       sep=',',
                       parse_dates=['Date'],
                       dayfirst=True,
                       index_col='Date')

# Обчислення загальної кількості велосипедистів за всі локації
fixed_df['Total'] = fixed_df.iloc[:, 1:].sum(axis=1)

# Додавання місяця до DataFrame
fixed_df['Month'] = fixed_df.index.month

monthly_totals = fixed_df.groupby('Month')['Total'].sum()

most_popular_month = monthly_totals.idxmax()
most_popular_count = int(monthly_totals.max())

print(f"Найпопулярніший місяць: {most_popular_month} (Загальна кількість велосипедистів: {most_popular_count})")

monthly_totals.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Кількість велосипедистів за місяцями у 2018 році')
plt.xlabel('Місяць')
plt.ylabel('Загальна кількість велосипедистів')
plt.xticks(range(12),
           ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
            'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'],
           rotation=45)
plt.show()
