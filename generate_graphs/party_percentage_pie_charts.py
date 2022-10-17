import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime#
import os


def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    return current_time


def get_categories_and_values(df, column_name):
    column_to_count = df[column_name]
    parties_count = Counter(column_to_count)
    party_categories = list(parties_count.keys())
    party_values = list(parties_count.values())

    return(party_categories,party_values)


def create_and_save_pie_chart(title, values, labels, colours, output_location, dpi=400, graph_width=30, graph_height=20):
    plt.figure(num=1, figsize=(graph_width,graph_height), clear=True)
    plt.title(title)
    plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, colors=colours)

    print("[{}] Outputting file to location: {}".format(current_time(), output_location))
    plt.savefig(output_location, dpi=dpi, bbox_inches="tight")


def get_colour_matcher(parties_csv):
    parties_df = pd.read_csv(parties_csv)
    
    colour_matcher = dict(zip(parties_df["Party_Name"], parties_df["Hex_Col"]))

    return colour_matcher


#File location of parties.csv that contains hex codes for each party's colour. 
colour_matcher = get_colour_matcher("{file-path-here}\\2011_archive_datapackage\\2011_archive\\NI\\parties.csv")


year = 2011

output_directory = "file-path-here"

#Directory containing all constituencies for a specific year 
constituency_directory = "{file-path-here}\\2011_archive_datapackage\\2011_archive\\constituency"

#Getting a list of all constituency (names)
constituencies = os.listdir(constituency_directory)

for constituency in constituencies:
    constituency_name = constituency

    #Dealing with current and output directories
    current_directory = os.path.join(constituency_directory, constituency)

    graph_output_directory = os.path.join(output_directory, constituency)
    full_graph_output_directory = os.path.join(graph_output_directory, "Party_Pie_Distributions")
    os.mkdir(full_graph_output_directory)


    #*****************First Graph********************************
    constituency_candidates_path = os.path.join(current_directory, "Candidate.csv")
    constituency_candidate_df = pd.read_csv(constituency_candidates_path)

    party_categories, party_values = get_categories_and_values(constituency_candidate_df, "Party_Name")

    colours = [colour_matcher[party] for party in party_categories]
    title = "Pie chart showing distribution of candidate parties for {} {} election".format(constituency_name, year)

    file_name = "{}_all_candidates_parties.png".format(constituency_name)
    output_file_path = os.path.join(full_graph_output_directory, file_name)

    create_and_save_pie_chart(title, party_values, party_categories, colours, output_file_path)

    #*****************Second Graph********************************
    constituency_elected_candidates_path = os.path.join(current_directory, "Count.csv")
    constituency_elected_candidate_df = pd.read_csv(constituency_elected_candidates_path)


    #Getting those elected
    max_count = max(constituency_elected_candidate_df["Count_Number"])

    last_count = constituency_elected_candidate_df.loc[constituency_elected_candidate_df["Count_Number"] == max_count]

    constituency_elected_candidate_df = last_count.loc[last_count["Status"]=="Elected"]


    party_categories, party_values = get_categories_and_values(constituency_elected_candidate_df, "Party_Name")

    title = "Pie chart showing distribution of elected candidate parties for {} {} election".format(constituency_name, year)

    file_name = "{}_elected_candidates_parties.png".format(constituency_name)
    output_file_path = os.path.join(full_graph_output_directory, file_name)
    colours = [colour_matcher[party] for party in party_categories]


    create_and_save_pie_chart(title, party_values, party_categories, colours, output_file_path)
