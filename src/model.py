import pickle
from flask import Flask,render_template,request,url_for
#models
df = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
recomended_movies = []
movies_list = []
for i in df["title"].values:        
        movies_list.append(i)
        
def process_post(movie):
    
    movie_index = df[df['title']==movie].index[0]    
    distance = sorted(enumerate(similarity[movie_index]),reverse=True,key=lambda x:x[1])[1:5]
         
    for i in distance:
        recomended_movies.append(df.loc[i[0]].title)       
    
    return recomended_movies
                                                                         

app = Flask(__name__,template_folder="/storage/emulated/0/movie_recomend_system/src/templates") 

#home page
@app.route("/",methods=["POST","GET"])
def home_page():
    if request.method=="POST":
        movie_ = request.form.get("movies")
        if process_post(movie_):
            return render_template("home.html",recomended_movies=recomended_movies)
    else:
        return render_template("home.html",movies_list=movies_list)
  
       


        
            
    

if __name__ == "__main__":
    app.run(debug=True)



