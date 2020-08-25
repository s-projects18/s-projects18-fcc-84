import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from matplotlib import dates as mpl_dates

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03
# date,value
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date", parse_dates=True)

# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
f25 = df['value'] <= df['value'].quantile(0.025)
f75 = df['value'] >= df['value'].quantile(0.975)
cond = (f25 | f75)
df = df.drop(index=df[cond].index)



def draw_line_plot():
    # Draw line plot
    # info: plt has no special lineplot(), but seaborn has
    # use plot_date() instead of plot()
    fig, ax = plt.subplots()
    fig.set_figheight(6)
    fig.set_figwidth(14)

    ax.plot_date(df.index, df['value'], linestyle="solid", marker=None, color="red")
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    #plt.xticks(rotation=90)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(6*30))

     # standard string formatter options
    date_format = mpl_dates.DateFormatter('%Y-%m')
    ax.xaxis.set_major_formatter(date_format)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # It should show average daily page views for each month grouped by year
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.strftime('%B')
    df_grp = df_bar.groupby(['year', 'Month'])
    # series
    df_grp['value'].apply(lambda x: x.mean())

    # Draw bar plot
    #darkgrid, whitegrid, dark, white, ticks
    sns.set_style("ticks")
    list_month=['January','February','March','April','May','June','July','August','September','October','November','December']
    # , palette="rocket"
    g = sns.catplot(x="year", kind="bar", hue="Month", y="value", data=df_bar, hue_order=list_month, ci=None, legend=False, palette="hls")

    fig = g.fig
    ax = g.ax    
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', title="Month")
    plt.setp(ax.get_legend().get_texts(), fontsize='8')
    plt.setp(ax.get_legend().get_title(), fontsize='8')
    plt.tight_layout()
    
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
