import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'ROE': [7.4, 7.8, 5.9, 7.1, 6.8, 7.6, 7.9, 8.3, 7.2, 6.9, 7.9],
                   'COF': [6.3, 4.2, 6.2, 8.1, 8.4, 7.5, 6.5, 7.8, 6.9, 7.1, 7.2],
                   'rating': ['AAA', 'BB+', 'BB+', 'AAA', 'BBB-', 'AA', 'AAA', 'AAA', 'BBB-', 'AAA', 'BB+']})

print('\n   Construct a BoxPlot using column cost of funding (COF).')
bp = plt.boxplot(df['COF'],
                 vert=True,
                 patch_artist=False,
                 showmeans=True,
                 showfliers=True,
                 tick_labels=['COF'])
plt.show()
print('Visualize a comparing statistics of COF and ROE.')
bp_comparing = plt.boxplot([df['COF'], df['ROE']],
                     vert=True,  # box location (True by default)
                     patch_artist=False,  # filling the box with color (False by default)
                     showmeans=True, # show the mean (False by default)
                     showfliers=True, # show the fliers (True by default)
                     tick_labels=['COF', 'ROE'])  # inscriptions
plt.show()

print('\n   Construct pandas boxplot columns COF and ROE using grouping by rating')
pb_pandas = df.boxplot(column=['COF', 'ROE'], by='rating', grid=False, color='black')
plt.show()