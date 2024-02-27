import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec 
from matplotlib.table import Table
import json

with open('data.json', 'r') as file:
    data = json.load(file)

column1_values = [entry['column1'] for entry in data]
column2_values = [entry['column2'] for entry in data]

fig = plt.figure(figsize=(10, 6))
gs = GridSpec(1, 2, width_ratios=[1, 4])

ax1 = plt.subplot(gs[0])
ax1.axis('off')
table_data = [['Zeitraum', 'Maximum (m³/s)']]

table_data.extend([[col1, col2] for col1, col2 in zip(column1_values, column2_values)])

table = Table(ax1, loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.5, 1.5)
for i, row in enumerate(table_data):
    for j, val in enumerate(row):
        cell_text = table.add_cell(i, j, width=0.2, height=0.3, text=val, loc='center', facecolor='lightgray')

ax2 = plt.subplot(gs[1])
ax2.plot(column1_values, column2_values, marker='o', linestyle='-', color='b')
ax2.set_xlabel('Zeitraum')
ax2.set_ylabel('Maximum (m³/s)')

ax2.set_xticks(range(len(column1_values)))
ax2.set_xticklabels(column1_values, rotation=45, ha='right')

plt.tight_layout()
plt.show()
