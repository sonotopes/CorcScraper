import pandas as pd
import csv
import matplotlib.pyplot as plt


def model(raw_data):
    """Models and standardizes data into averages by neighborhood"""
    with open(raw_data) as csv_file:
        df = pd.read_csv(csv_file)
        df = df.sort_values(by=['type'])

        avg_dict = {row['location']: [] for index, row in df.loc[:, ['location']].iterrows()}

        # Data is being added, and this object is then converted to pdf format.
        for index, row in df.loc[:, ['location', 'price']].iterrows():
            price = str(row['price'])
            if price.isdigit():
                avg_dict[row['location']].append(int(row['price']))

        for key in avg_dict:
            avg_dict[key] = int(round((sum(avg_dict[key]) / len(avg_dict[key])), -1))
        print(avg_dict)

        keys = list(avg_dict.keys())
        values = list(avg_dict.values())
        df_dict = {'Location': keys,
                   'Average Price': values,
                   }
        avg_df = pd.DataFrame(df_dict)

        avg_df.plot(x="Location", y="Average Price", kind="bar", rot=90, fontsize=1.5)

        plt.savefig('avg_price_rental_properties.pdf')

        plt.show()
