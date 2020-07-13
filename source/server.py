
from flask import Flask
from flask import session,render_template ,request, send_file 
import xgboost as xgb
import pandas as pd
import pickle
from simpletransformers.classification import ClassificationModel 

# overwrite default training args
train_args = {
    'reprocess_input_data': True,
    'overwrite_output_dir': True,
    'evaluate_during_training': False,
    'max_seq_length': 512,
    'num_train_epochs': 2,
    'evaluate_during_training_steps': 50,
    #'wandb_project': 'sts-b-medium',
    'train_batch_size': 16,
    'regression': False,
}

# load vocabulory
skill_vocabulory = []
with open('./source_data_files/skills_vocabulory.txt', 'r') as filehandle:
    for line in filehandle:
        currentSkill = line[:-1]
        skill_vocabulory.append(currentSkill)

# defining app and session
app = Flask(__name__)
app.secret_key = "kaushik-app"

# load XGBoost model for broad role classification
xgb_model = pickle.load(open('xgb_broad_model', 'rb'))

# load fine tuned BERT model for deep role classification
model = ClassificationModel('bert', 'bert_model/', num_labels=3,  args=train_args, use_cuda = False)

# navigating to base page when link opened on web browser
@app.route('/')
def hello_world():
    return render_template("index.html")

# navigating to skills page where recruiter (user) can input skills
@app.route('/skills',methods=["POST"])
def skillsPage():
    popular_skills = ['python', 'powerpoint', 'aws','data analysis','social networking', 'marketing', 'research', 'accounting']
    session['skill_count'] = int (request.form["skillsCount"])
    return render_template("skills.html",skillCount=int(request.form["skillsCount"]),skillTags=skill_vocabulory, popularSkills=popular_skills)

# navigate to listing page to see the broad role classificaation
@app.route("/listing",methods=["POST"])
def listings():
    
    # preprocess input data for broad role classification
    skill_count = session['skill_count']
    df_test = pd.DataFrame(columns = skill_vocabulory)
    print (skill_count)
    skill_list = []
    print (skill_list)
    for i in range(skill_count):
        print (i)
        skill_list.append([request.form["skill"+str(i+1)],request.form["endorsemennt"+str(i+1)]])
    print (skill_list)
    session['skill_list'] = skill_list
    total_endorse = 0
    for i in range(skill_count):
        total_endorse += int(skill_list[i][1])
    for j in range(len(skill_list)):
        df_test.loc[0,skill_list[j][0]] = round(int(skill_list[j][1]) / total_endorse, 3)
        print (round(int(skill_list[j][1]) / total_endorse, 3))
    df_test = df_test.fillna(0)
    df_test = xgb.DMatrix(data=df_test)
    label_ano = ["Accounts","Arts, Design and Writing","Engineering","Human Resources","Marketing and Sales"]

    # predict using pretrained XGBoost
    pred = xgb_model.predict(df_test)[0]

    print (label_ano[int(pred)]) 
    session['broad_count'] = 359
    return render_template("listing.html", pred = [{"name":label_ano[int(pred)],"fileName":"./source_data_files/engineering.csv","count":session['broad_count']}],label_ano = label_ano)
    
# Download CSV  
@app.route("/file/<fileName>")
def file(fileName):
    return send_file(fileName,as_attachment=True)

# navigate user to the below route when user selects advance model
@app.route("/skillsDescription",methods=["GET"])
def skillsDescription():
    return render_template("skillsDescription.html", skill_list = session["skill_list"])

# navigate to advance page to see the deep role classificaation
@app.route("/advance",methods=["POST"])
def advance():

    description = ""
    file_name = ""
    sample_count = 0

    for i in range(session["skill_count"]):
        description += str(request.form["skillsDescription"+str(i+1)]) + " "
    print ("*****")
    print (description)
    print ("*****")

    # predict using finne tuned BERT
    pred = int(model.predict([description])[0][0])
    label = None
    print (pred)
    if pred == 0:
        label = "Data Scientist"
        file_name = "./source_data_files/data_scientist.csv"
        sample_count = 137
    if pred == 1:
        label = "Network Engineer"
        file_name = "./source_data_files/network_engineer.csv"
        sample_count = 138
    if pred == 2:
        label = "Software Engineer"
        file_name = "./source_data_files/software_engineer.csv"
        sample_count = 215
    print (label)
    
    return render_template("advance.html", filename = file_name, broad_count = session['broad_count'], deep_count = sample_count)


if __name__ == '__main__':

    # app.run('0.0.0.0',8000, debug=True, threaded=False)
    app.run('0.0.0.0',8000, debug=True, threaded=True, processes = 10)
