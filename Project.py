import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff 
import csv 
import statistics 
import random

df = pd.read_csv("ProjectData.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
population_median = statistics.median(data)
population_mode =  statistics.mode(data)
population_stdev = statistics.stdev(data)

print('Mean, Median, Mode and Standard Distribution of population are', population_mean, population_median, population_mode, population_stdev)

fig = ff.create_distplot([data], ["Reading Time"], show_hist = False)
fig.show()


def expirement():
    sampled_data = []

    for i in range(0, 30):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        sampled_data.append(value)
    
    mean_sampledata = statistics.mean(sampled_data)

    return mean_sampledata

mean_of_sampling_expirement = []

for i in range(0, 100):
    mean_sampledata = expirement()
    mean_of_sampling_expirement.append(mean_sampledata)

def sampling():
    meanofsampling = statistics.mean(mean_of_sampling_expirement)
    medianofsampling = statistics.median(mean_of_sampling_expirement)
    modeofsampling = statistics.mode(mean_of_sampling_expirement)
    stdevofsampling = statistics.stdev(mean_of_sampling_expirement)

    print('Mean, Median, Mode and Standard Distribution of sampling distribution are', meanofsampling, medianofsampling, modeofsampling, stdevofsampling)

    fig = ff.create_distplot([mean_of_sampling_expirement], ["Sampling Distribution"], show_hist = False)
    fig.show()

sampling()