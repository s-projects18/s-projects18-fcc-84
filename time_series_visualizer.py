import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03
# date,value
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date")

# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
# ??? > or: >=
f25 = df['value'] <= df['value'].quantile(0.025)
f75 = df['value'] >= df['value'].quantile(0.075)
cond = (f25 | f75)
df = df.drop(index=df[cond].index)



def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df['value'])
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    ax.set_title('Daily freeCodeCamp Forum Page Views 05/2016-12/2019')
    #plt.xticks(rotation=90)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
    # TODO: both axes are false


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
