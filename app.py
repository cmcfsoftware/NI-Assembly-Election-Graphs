from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("map.html")


@app.route('/results/<constituency_name>')
def show_user_profile(constituency_name):

    #get the number of counts for he constituency.
    results_info = []
    years = [int(year) for year in os.listdir("static\\result_graphs")]
    for year in years:
        path = "static\\result_graphs\\{}\\{}".format(year, constituency_name)
        total_counts =  len(os.listdir(path))-2 

        info_dictionary = {
            "year":year,
            "total_counts":total_counts
        }
        results_info.append(info_dictionary)


    path = "static\\result_graphs\\2011\\" + constituency_name
    total_counts =  len(os.listdir(path))-2 # Final Result Doesn't count and pie charts

    response_object = {
        "url_start":"static/result_graphs/",
        "constituency_name":constituency_name,
        "results":results_info,
        "years":years
    }

    return render_template("constituency_graphs.html", response = response_object)


@app.route("/data")
def data_source():
    return render_template("data_source.html")

if __name__ == "__main__":
    app.run(debug=True)