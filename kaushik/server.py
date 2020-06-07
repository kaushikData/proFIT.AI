from flask import Flask
from flask import render_template ,request
import xgboost as xgb
import pandas as pd
import pickle

skill_vocabulory = []
with open('skills_vocabulory.txt', 'r') as filehandle:
    for line in filehandle:
        currentSkill = line[:-1]
        skill_vocabulory.append(currentSkill)

app = Flask(__name__)
skill_count = 0
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/skills',methods=["POST"])
def skillsPage():
    popular_skills = ['python', 'powerpoint', 'aws','data analysis','social networking', 'marketing', 'research', 'accounting']
    global skill_count 
    skill_count = int (request.form["skillsCount"])
    return render_template("skills.html",skillCount=int(request.form["skillsCount"]),skillTags=skill_vocabulory, popularSkills=popular_skills)

@app.route("/listing",methods=["POST"])
def listings():
    xgb_model = pickle.load(open('xgb_broad_model', 'rb'))
    
    df_test = pd.DataFrame(columns = skill_vocabulory)

    print (skill_count)
    
    skills_list = []

    for i in range(skill_count):
        print (i)
        skills_list.append([request.form["skill"+str(i+1)],request.form["endorsemennt"+str(i+1)]])
    print (skills_list)

    total_endorse = 0
    for i in range(skill_count):
        total_endorse += int(skills_list[i][1])



    for j in range(len(skills_list)):
        df_test.loc[0,skills_list[j][0]] = round(int(skills_list[j][1]) / total_endorse, 3)
        print (round(int(skills_list[j][1]) / total_endorse, 3))
    
    df_test = df_test.fillna(0)
    df_test = xgb.DMatrix(data=df_test)
    label_ano = ["Accounts","Design and Arts","Engineering","Human Resources","Marketing and Sales","Technical Writing"]
    pred = xgb_model.predict(df_test)[0]
    print (label_ano[int(pred)])
    return render_template("listing.html", pred = label_ano[int(pred)],label_ano = label_ano)