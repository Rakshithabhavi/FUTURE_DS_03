import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#  1. Sample Marketing Funnel Dataset
data = {
    'Stage': ['Awareness', 'Interest', 'Consideration', 
               'Intent', 'Purchase'],
    'Visitors': [10000, 6500, 3800, 1900, 850],
    'Channel': ['Social Media', 'Email', 'SEO', 
                'Paid Ads', 'Direct']
}

df = pd.DataFrame(data)

#  2. Conversion Rates 
df['Conversion_Rate'] = (df['Visitors'] / 
                          df['Visitors'].shift(1) * 100).round(2)
df['Conversion_Rate'].iloc[0] = 100.0
df['Drop_Off'] = df['Visitors'].shift(1) - df['Visitors']
df['Drop_Off'].iloc[0] = 0

print("=== Marketing Funnel Analysis ===")
print(df)
print(f"\nOverall Conversion Rate: {(850/10000*100):.1f}%")
print(f"\nBiggest Drop-off Stage: Interest → Consideration")
print(f"Drop-off: {6500-3800} visitors")

# 3. Funnel Chart 
plt.figure(figsize=(10,6))
colors = ['#2196F3','#42A5F5','#64B5F6','#90CAF9','#BBDEFB']
bars = plt.barh(df['Stage'], df['Visitors'], 
                color=colors, edgecolor='white', height=0.6)
plt.title('Marketing Funnel - Visitor Drop-off', 
          fontsize=14, fontweight='bold')
plt.xlabel('Number of Visitors')
plt.ylabel('Funnel Stage')
plt.gca().invert_yaxis()
for bar, val in zip(bars, df['Visitors']):
    plt.text(bar.get_width() + 100, bar.get_y() + 
             bar.get_height()/2, f'{val:,}', 
             va='center', fontsize=10)
plt.tight_layout()
plt.savefig('funnel_chart.png')
plt.show()

#  4. Conversion Rate by Stage 
plt.figure(figsize=(10,5))
stages = ['Awareness→Interest', 'Interest→Consideration', 
          'Consideration→Intent', 'Intent→Purchase']
rates = [65.0, 58.5, 50.0, 44.7]
colors = ['green' if r > 55 else 'orange' 
          if r > 45 else 'red' for r in rates]
plt.bar(stages, rates, color=colors, edgecolor='white')
plt.title('Conversion Rate Between Stages', 
          fontsize=14, fontweight='bold')
plt.xlabel('Stage Transition')
plt.ylabel('Conversion Rate (%)')
plt.xticks(rotation=15)
for i, rate in enumerate(rates):
    plt.text(i, rate + 0.5, f'{rate}%', 
             ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('conversion_rates.png')
plt.show()

# 5. Channel Performance 
plt.figure(figsize=(8,5))
channel_data = {
    'Channel': ['Social Media', 'Email', 'SEO', 
                'Paid Ads', 'Direct'],
    'Leads': [3500, 2800, 2100, 1200, 400],
    'Conversions': [280, 350, 180, 150, 90]
}
ch_df = pd.DataFrame(channel_data)
ch_df['Conv_Rate'] = (ch_df['Conversions'] / 
                       ch_df['Leads'] * 100).round(1)

sns.barplot(x='Channel', y='Conv_Rate', 
            data=ch_df, palette='viridis')
plt.title('Conversion Rate by Channel', 
          fontsize=14, fontweight='bold')
plt.xlabel('Marketing Channel')
plt.ylabel('Conversion Rate (%)')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('channel_performance.png')
plt.show()

#  6. Visitors Trend 
plt.figure(figsize=(10,5))
plt.plot(df['Stage'], df['Visitors'], 
         marker='o', color='blue', 
         linewidth=2, markersize=8)
plt.fill_between(range(len(df['Stage'])), 
                 df['Visitors'], alpha=0.3, color='blue')
plt.title('Visitor Drop-off Trend Across Funnel', 
          fontsize=14, fontweight='bold')
plt.xlabel('Funnel Stage')
plt.ylabel('Number of Visitors')
for i, val in enumerate(df['Visitors']):
    plt.text(i, val + 150, f'{val:,}', 
             ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('visitors_trend.png')
plt.show()

print("\n=== Analysis Complete! Charts Saved! ===")