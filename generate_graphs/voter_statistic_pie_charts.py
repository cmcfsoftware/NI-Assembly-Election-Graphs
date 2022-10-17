import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_pie_axis(axis, values, labels, title="", autopct='%.2f%%', startangle=90, explode=(0.1,0)):
    #print(labels)
    axis.pie(values, labels=labels, autopct=autopct, startangle=startangle, explode=explode)
    axis.set_title(title)

constituency_name_map = {
    "Belfast East": "belfast-east",
    "Belfast North": "belfast-north",
    "Belfast South": "belfast-south",
    "Belfast West": "belfast-west",
    "East Antrim": "east-antrim",
    "East Londonderry": "east-londonderry",
    "Fermanagh and South Tyrone": "fermanagh-south-tyrone",
    "Foyle": "foyle",
    "Lagan Valley": "lagan-valley",
    "Mid Ulster": "mid-ulster",
    "Newry and Armagh": "newry-armagh",
    "North Antrim": "north-antrim",
    "North Down": "north-down",
    "South Antrim": "south-antrim",
    "South Down": "south-down",
    "Strangford": "strangford",
    "Upper Bann": "upper-bann",
    "West Tyrone": "west-tyrone"
}


df = pd.read_csv("C:\\Users\\New SSD\\Desktop\\Election_Graphs\\2017_archive_datapackage\\2017_archive_datapackage\\NI\\all-constituency-info.csv")
year = 2011

output_directory = "C:\\Users\\New SSD\\Desktop\\Assembly_Election_Graphs\\voting_pie_charts\\2011"

source_path = "C:\\Users\\New SSD\\Desktop\\Election_Graphs\\2011_archive_datapackage\\2011_archive\\constituency"

constituencies = os.listdir(source_path)


#The format of the CSV containing voting data changes each year so the best way to loop though should be changed each time

for file_constituency in constituencies:
    path_to_data = os.path.join(source_path, file_constituency, "ConstituencyCount.csv")
    df = pd.read_csv(path_to_data)
    constituency = df

#for i in range(len(df)-1):
   
    #constituency = df.iloc[i]

    constituency_name = constituency["Constituency_Name"][0]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    full_title = 'Pie charts showing voter statistics for {} {}'.format(constituency_name, year)
    fig.suptitle(full_title)
    fig.set_figwidth(17)
    


    #Voter eligibility chart
    total_electorate = int(constituency["Total_Electorate"])
    ineligible_to_vote = int(constituency["Voting_Age_Pop"]) - total_electorate

    eligibility_values = [total_electorate, ineligible_to_vote]
    eligibility_labels = ["Total Electorate ({})".format(total_electorate), "Ineligible to vote ({})".format(ineligible_to_vote)]
    eligibility_title = "Population Voting Eligiblilty"
    plot_pie_axis(ax1, eligibility_values, eligibility_labels, eligibility_title)


    #Voter Turnout chart
    total_polled_votes = int(constituency["Total_Poll"])
    total_abstentions = int(constituency["Total_Electorate"]) - total_polled_votes

    turnout_values = [total_polled_votes, total_abstentions]
    turnout_labels = ["Total Polled ({})".format(total_polled_votes), "Abstentions ({})".format(total_abstentions)]
    turnout_title = "Voters and Abstentions"
    plot_pie_axis(ax2, turnout_values, turnout_labels, turnout_title)


    #Spoiled vote chart
    valid_votes = int(constituency["Valid_Poll"])
    spoiled_votes = int(constituency["Spoiled"])

    validity_values = [valid_votes, spoiled_votes]
    validity_labels = ["Valid ({})".format(valid_votes), "Spoiled ({})".format(spoiled_votes)]
    validity_title = "Valid and Spoiled Votes"
    plot_pie_axis(ax3, validity_values, validity_labels, validity_title)

    
    file_name = constituency_name_map[constituency_name] + "_voter_stats.png"
    file_output_path = os.path.join(output_directory, file_name)
    plt.savefig(file_output_path, dpi=400, bbox_inches='tight')
    fig.clf()


