from tkinter import * 

from tkinter import messagebox 

import random 

import imdb 

from bs4 import BeautifulSoup as SOUP 

import re 

import requests as HTTP 

import pandas as pd 

import webbrowser 

m = Tk() 

canvas=Canvas(m, height=600, width=750) 

canvas.pack() 

frame_başlık=Frame(m, bg="purple") 

frame_başlık.place(relx=0, rely=0, relwidth=1, relheight=0.2) 

frame_seçim=Frame(m, bg="white") 

frame_seçim.place(relx=0, rely=0.2, relwidth=1, relheight=0.8) 

  

Label(frame_başlık, bg='purple', text="WHAT DO YOU WANT ME TO SUGGEST?",font='Verdana 18 bold', fg='white').place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2) 

def emoo(): 

    def main(emotion): 

  

        last_message="" 

  

         

        if emotion == "Sad" or emotion== "sad": 

  

            urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

        elif(emotion == "Disgust" or emotion== "disgust"): 

  

            urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc' 

  

          

  

        elif(emotion == "Anger" or emotion=="anger"): 

  

            urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

        elif(emotion == "Anticipation" or emotion== "anticipation"): 

  

            urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc' 

  

          

  

  

        elif(emotion == "Fear" or emotion== "fear"): 

  

            urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

        elif(emotion == "Enjoyment" or emotion== "enjoyment"): 

  

            urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

        elif(emotion == "Trust" or emotion== "trust"): 

  

            urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

        elif(emotion == "Surprise" or emotion=="surprise"): 

  

            urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc' 

  

          

        else: 

  

            last_message+= "Please choose one of these: Sad, Anger, Disgust, Anticipation, Fear, Enjoyment, Trust, Surprise" 

            messagebox.showinfo("Constraints", last_message) 

             

             

  

            emotion = input("Enter the emotion: ") 

                 

  

            if emotion == "Sad" or emotion== "sad": 

                urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

            elif emotion == "Disgust" or emotion== "disgust": 

                urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc' 

  

          

  

            elif emotion == "Anger" or emotion=="anger": 

                urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

            elif emotion == "Anticipation" or emotion== "anticipation": 

                urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc' 

  

          

  

  

            elif emotion == "Fear" or emotion== "fear": 

                urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

            elif emotion == "Enjoyment" or emotion== "enjoyment": 

                urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

            elif emotion == "Trust" or emotion== "trust": 

                urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc' 

  

          

  

             

            elif emotion == "Surprise" or emotion=="surprise": 

                urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc' 

  

            response = HTTP.get(urlhere) 

            data = response.text 

  

          

  

  

            soup = SOUP(data, "lxml") 

  

          

  

             

            title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 

            return title 

  

  

  

         

            if __name__ == '__main__': 

  

  

                t=[] 

                emotion = input("Enter the emotion: ") 

                a = main(emotion) 

                 

                 

            for i in a: 

                tmp = str(i).split('>') 

  

          

  

                if(len(tmp) == 3): 

                    t.append(tmp[1][:-3]) 

  

          

  

            k=int(input("Please write how many movie suggestions you would like to receive"))        

            x=[] 

            while k>50:

                
                print("please do not enter a number greater than 50")

                k=int(input("Please write how many movie suggestions you would like to receive"))


            while len(x)!=k:

                b=random.choice(t)

                if b not in x:

                    x.append(b)

  

            print(x) 
 

  

            print(x) 

  

  

  

  

                 

  

          

  

             

        response = HTTP.get(urlhere) 

        data = response.text 

  

          

  

  

        soup = SOUP(data, "lxml") 

  

          

  

             

        title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 

        return title 

  

  

  

         

    if __name__ == '__main__': 

  

  

  

        t=[] 

        emotion = input("Enter the emotion: ") 

        a = main(emotion) 

         

    for i in a: 

        tmp = str(i).split('>') 

  

          

  

        if(len(tmp) == 3): 

  

            t.append(tmp[1][:-3]) 

  

          

  

    k=int(input("Please write how many movie suggestions you would like to receive")) 

    x=[]

    while k>50:


        print("please do not enter a number greater than 50")


        k=int(input("Please write how many movie suggestions you would like to receive"))

  

    while len(x)<k:
        b=random.choice(t)
        if b not in x:

            x.append(b) 

  

    
    print(x)

  

  

  

  

         

def simi(): 

    df=pd.read_csv(r"C:\Users\acer\Desktop\movie_dataset.csv") 

    df.columns 

    features=['keywords','cast','genres','director'] 

  

  

    for feature in features: 

        df[feature] = df[feature].fillna('') 

     

  

    def combine_features(row): 

        try: 

            return row['keywords']+" "+row['cast']+" "+row["genres"]+" "+row["director"] 

        except: 

            print ("Error:", row) 

  

  

    df["combined_features"] = df.apply(combine_features,axis=1) 

  

    from sklearn.feature_extraction.text import CountVectorizer 

    from sklearn.metrics.pairwise import cosine_similarity 

  

    cv = CountVectorizer() 

    count_matrix = cv.fit_transform(df["combined_features"]) 

  

    cosine_sim = cosine_similarity(count_matrix) 

  

    cosine_sim.shape 

  

  

  

    def get_title_from_index(index): 

  

        return df[df.index == index]["title"].values[0] 

  

    def get_index_from_title(title): 

  

        return df[df.title == title]["index"].values[0] 

  

  

    def show_data(): 

  
        
        txt.delete(0.0, 'end') 

        movie =ent.get() 

        movie_user_likes =movie         

        movie_index = get_index_from_title(movie_user_likes) 

         

                 

        i=int(movie_index) 

        Similar_movies = list( enumerate(cosine_sim[i])) 

                 

        sorted_similar_movies = sorted(Similar_movies,key = lambda x:x[1], reverse = True) 

                 

                 

        i=0; 

        j=0; 

        List =[None]*10 

        for element in sorted_similar_movies: 

  

            s=get_title_from_index(element[0]) 

            List[j]=s 

            j=j+1; 

             

             

            i=i+1; 

  

            if i>=10: 

                break 

             

             

        for x in range(len(List) -1, -1, -1): 

  

            t="\n" 

            txt.insert(0.0, List[x]) 

            txt.insert(0.0, t) 

            

     

        

    

    root=Tk() 

    root.geometry("420x300") 

                

    l1 = Label(root, text="Enter Movie name: ") 

    l2 = Label(root, text="Top Ten Suggtion For You: ") 

                

    ent =Entry(root) 

             

    l1.grid(row=0) 

    l2.grid(row=2) 

                

    ent.grid(row=0, column=1) 

                

             

                

                

                

                

    txt=Text(root,width=50,height=13, wrap=WORD) 

    txt.grid(row=3, columnspan=2, sticky=W) 

                

    btn=Button(root, text="Search", bg="purple", fg="white", command=show_data) 

    btn.grid(row=1, columnspan=2) 

    root.mainloop() 

def randm(): 

  

  

    movie={"The Shawshank Redemption": "0111161","The Godfather": "0068646","The Dark Knight": "0468569", 

           "The Lord of the Rings: The Return of the King":"0167260","Schindler's List":"0108052", 

           "12 Angry Men":"0050083","Pulp Fiction":"0110912","Inception":"1375666","Forrest Gump":"0109830", 

           "The Lord of the Rings: The Two Towers":"0167261","Fight Club":"0137523","Toy Story":"0114709", 

           "Il buono, il brutto, il cattivo":"0060196","Everything Everywhere All at Once":"6710474", 

           "The Matrix":"0133093","Goodfellas":"0099685","The Empire Strikes Back":"0080684","Citizen Kane":"0033467", 

           "One Flew Over the Cuckoo's Nest":"0073486","Interstellar":"0816692","Modern Times":"0027977","Seppuku":"0056058", 

           "Cidade de Deus":"0317248","Sen to Chihiro no kamikakushi":"0245429","The Shining":"0081505", 

           "Saving Private Ryan":"0120815","The Green Mile":"0120689","La vita è bella":"0118799","Se7en":"0114369", 

           "Terminator 2: Judgment Day":"0103064","The Silence of the Lambs":"0102926","The Godfather": "Part II:0071562", 

           "Star Wars":"0076759","Seppuku":"0056058","Original title: Shichinin no samurai":"0047478", 

           "It's a Wonderful Life":"0038650","Gisaengchung":"6751668","Das Leben der Anderen":"0405094", 

           "Whiplash":"2582802","Intouchables":"1675434","The Prestige":"0482571","The Departed":"0407887", 

           "The Pianist":"0253474","Gladiator":"0172495","American History X":"0120586","The departed":"0407887", 

           "The Prestige":"0482571","Casablanca":"0034583","Whiplash":"2582802","The Intouchables":"1675434", 

           "Hotaru no haka":"0095327","Rear Window":"0047396","Alien":"0078748","City Lights":"0021749","Nuovo Cinema Paradiso":"0095765", 

           "Everything Everywhere All at Once":"6710474","Raiders of the Lost Ark":"0082971","Django Unchained":"1853728","WALL·E":"0910970", 

           "Sunset Blvd.":"0043014","Paths of Glory":"0050825","C'era una volta il West":"0064116", 

           "The Shining":"0081505","The Great Dictator":"0032553","Witness for the Prosecution":"0051201","Avengers: Infinity War":"4154756", 

           "Das Leben der Anderen":"0405094","Das Boot":"0082096","Raiders of the Lost Ark":"0082971", 

           "Amadeus":"0086879","Aliens":"0090605","Braveheart":"0112573","Mononoke-hime":"0119698", 

           "American Beauty":"0169547","Memento":"0209144","Oldeuboi":"0364569","Eine Stadt sucht einen Mörder":"0022100", 

           "Singin' in the Rain":"0045152","Vertigo":"0052357","North by Northwest":"0053125","Lawrence of Arabia":"0056172", 

           "2001: A Space Odyssey":"0062622","Star Wars: Episode VI - Return of the Jedi":"0086190", 

           "Once Upon a Time in America":"0087843","Reservoir Dogs":"0105236","The Lord of the Rings: The Fellowship of the Ring":"0120737", 

           "Good Will Hunting":"0119217","Requiem for a Dream":"0180093","Memento":"0209144","Apocalypse Now":"0078788", 

           "Le fabuleux destin d'Amélie Poulain":"0211915","Eternal Sunshine of the Spotless Mind":"0338013", 

           "Inglourious Basterds":"0361748","Toy Story 3":"0435761","Jagten":"2106476","The Great Dictator":"0032553", 

           "Sunset Blvd.":"0043014","Paths of Glory":"0050825","Witness for the Prosecution":"0051201", 

           "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb":"0057012","Tengoku to jigoku":"0057565",} 

  

  

    e= list(movie.keys()) 

  

     

    ia = imdb.IMDb() 

  

  

  

    code = movie[random.choice(e)] 

  

  

  

  

    movie = ia.get_movie(code) 

    print(movie) 

    print("===============") 

    cast = movie['art department'] 

  

  

  

  

    actor = cast[1] 

  

  

    print(actor) 

  

  

  

  

  

  

  

  

  

  

     

  

    movie1 = ia.get_movie(code, info =['plot']) 

  

  

  

  

    movie1.infoset2keys 

  

  

  

  

    print(movie1['plot']) 

  

  

  

  

  

  

    ia = imdb.IMDb() 

  

  

  

  

  

  

  

  

  

    movie2 = ia.get_movie(code) 

  

  

  

  

    cast = movie2['cast'] 

  

  

  

  

    print(cast[0]) 

  

  

  

  

    role = cast[0].currentRole 

  

  

  

  

    print(role) 

  

def ranmus(): 

    musicurl=["https://www.youtube.com/watch?v=hTWKbfoikeg&list=PLA1D6023F6FF2684B&index=1", 

              "https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=PLA1D6023F6FF2684B&index=2", 

              "https://www.youtube.com/watch?v=fzofPH7k2H0&list=PLA1D6023F6FF2684B&index=3", 

              "https://www.youtube.com/watch?v=OMOGaugKpzs&list=PLA1D6023F6FF2684B&index=5", 

              "https://www.youtube.com/watch?v=SBmAPYkPeYU&list=PLA1D6023F6FF2684B&index=6", 

              "https://www.youtube.com/watch?v=COiIC3A0ROM&list=PLA1D6023F6FF2684B&index=7", 

              "https://www.youtube.com/watch?v=JBfjU3_XOaA&list=PLA1D6023F6FF2684B&index=8", 

              "https://www.youtube.com/watch?v=ftjEcrrf7r0&list=PLA1D6023F6FF2684B&index=9", 

              "https://www.youtube.com/watch?v=RJM-H7kzHrU&list=PLA1D6023F6FF2684B&index=10", 

              "https://www.youtube.com/watch?v=dN3GbF9Bx6E&list=PLA1D6023F6FF2684B&index=11", 

              "https://www.youtube.com/watch?v=6ul-cZyuYq4&list=PLA1D6023F6FF2684B&index=12", 

              "https://www.youtube.com/watch?v=fQ0PwEOgups&list=PLA1D6023F6FF2684B&index=13", 

              "https://www.youtube.com/watch?v=QzhbGaCwBzs&list=PLA1D6023F6FF2684B&index=14", 

              "https://www.youtube.com/watch?v=hajBdDM2qdg&list=PLA1D6023F6FF2684B&index=15", 

              "https://www.youtube.com/watch?v=hajBdDM2qdg&list=PLA1D6023F6FF2684B&index=15", 

              "https://www.youtube.com/watch?v=hajBdDM2qdg&list=PLA1D6023F6FF2684B&index=15", 

              "https://www.youtube.com/watch?v=IxuThNgl3YA&list=PLA1D6023F6FF2684B&index=16", 

              "https://www.youtube.com/watch?v=rMbATaj7Il8&list=PLA1D6023F6FF2684B&index=17", 

              "https://www.youtube.com/watch?v=z0XAI-PFQcA&list=PLA1D6023F6FF2684B&index=18", 

              "https://www.youtube.com/watch?v=1IdEhvuNxV8&list=PLA1D6023F6FF2684B&index=19", 

              "https://www.youtube.com/watch?v=HQmmM_qwG4k&list=PLA1D6023F6FF2684B&index=20", 

              "https://www.youtube.com/watch?v=K56soYl0U1w&list=PLA1D6023F6FF2684B&index=21", 

              "https://www.youtube.com/watch?v=hspw6J8NJ7s&list=PLA1D6023F6FF2684B&index=22", 

              "https://www.youtube.com/watch?v=pl3vxEudif8&list=PLA1D6023F6FF2684B&index=23", 

              "https://www.youtube.com/watch?v=EfK-WX2pa8c&list=PLA1D6023F6FF2684B&index=24", 

              "https://www.youtube.com/watch?v=TG8Ect3Xn7w&list=PLA1D6023F6FF2684B&index=25", 

              "https://www.youtube.com/watch?v=hsU6_eSG4k4&list=PLA1D6023F6FF2684B&index=27", 

              "https://www.youtube.com/watch?v=eWNykOk2ckE&list=PLA1D6023F6FF2684B&index=28", 

              "https://www.youtube.com/watch?v=SHhrZgojY1Q&list=PLA1D6023F6FF2684B&index=29", 

              "https://www.youtube.com/watch?v=r8hjtFq3vE0&list=PLA1D6023F6FF2684B&index=30", 

              "https://www.youtube.com/watch?v=fmnvAyxuHs0&list=PLA1D6023F6FF2684B&index=31", 

              "https://www.youtube.com/watch?v=DuDeBcpLITQ&list=PLA1D6023F6FF2684B&index=32", 

              "https://www.youtube.com/watch?v=Th3ycKQV_4k&list=PLA1D6023F6FF2684B&index=33", 

              "https://www.youtube.com/watch?v=hwZNL7QVJjE&list=PLA1D6023F6FF2684B&index=34", 

              "https://www.youtube.com/watch?v=FGVGFfj7POA&list=PLA1D6023F6FF2684B&index=35", 

              "https://www.youtube.com/watch?v=vrQ4saKGI5k&list=PLA1D6023F6FF2684B&index=36", 

              "https://www.youtube.com/watch?v=jmHNfWRw-qg&list=PLA1D6023F6FF2684B&index=37", 

              "https://www.youtube.com/watch?v=rNS6D4hSQdA&list=PLA1D6023F6FF2684B&index=38", 

              "https://www.youtube.com/watch?v=MRb1-SAAIzs&list=PLA1D6023F6FF2684B&index=40", 

              "https://www.youtube.com/watch?v=qZ6OrrkeVFo&list=PLA1D6023F6FF2684B&index=42", 

              "https://www.youtube.com/watch?v=DIoKr9VDg3A&list=PLA1D6023F6FF2684B&index=44", 

              "https://www.youtube.com/watch?v=q31WY0Aobro&list=PLA1D6023F6FF2684B&index=45", 

              "https://www.youtube.com/watch?v=32C703sNwyw&list=PLA1D6023F6FF2684B&index=49", 

              "https://www.youtube.com/watch?v=TJAfLE39ZZ8", 

              "https://www.youtube.com/watch?v=6EA-MIYY1bg", 

              "https://www.youtube.com/watch?v=PVjiKRfKpPI", 

              "https://www.youtube.com/watch?v=wDjeBNv6ip0", 

              "https://www.youtube.com/watch?v=vbvyNnw8Qjg", 

              "https://www.youtube.com/watch?v=vbvyNnw8Qjg", 

              "https://www.youtube.com/watch?v=sBspSJWRT2E", 

              "https://www.youtube.com/watch?v=uT3SBzmDxGk",] 

  

  

  

  

  

  

  

  

  

  

     

  

     

  

  

  

    webbrowser.open(random.choice(musicurl)) 

  

  

def act(): 

  

  

    cry=["https://www.youtube.com/watch?v=LOZuxwVk7TU", 

         "https://www.youtube.com/watch?v=nfWlot6h_JM", 

         "https://www.youtube.com/watch?v=ixkoVwKQaJg", 

         "https://www.youtube.com/watch?v=ZbZSe6N_BXs", 

         "https://www.youtube.com/watch?v=Mbj26vHDMII", 

         "https://www.youtube.com/watch?v=jO2viLEW-1A", 

         "https://www.youtube.com/watch?v=E07s5ZYygMg", 

         "https://www.youtube.com/watch?v=x3bfa3DZ8JM", 

         "https://www.youtube.com/watch?v=2p3zZoraK9g", 

         "https://www.youtube.com/watch?v=6swmTBVI83k" 

         "https://www.youtube.com/watch?v=gn0SUZtsr40", 

         "https://www.youtube.com/watch?v=Kua2dDhqzZw", 

         "https://www.youtube.com/watch?v=oy3SWNVfSUc", 

         "https://www.youtube.com/watch?v=dKlgCk3IGBg", 

         "https://www.youtube.com/watch?v=OAYuMygPkbI", 

         "https://www.youtube.com/watch?v=CveANi17YfU&list=PL3-sRm8xAzY-w9GS19pLXMyFRTuJcuUjy", 

         "https://www.youtube.com/watch?v=CWCMGIG1Y54&list=PL3-sRm8xAzY-w9GS19pLXMyFRTuJcuUjy&index=10", 

         "https://www.youtube.com/watch?v=1r79eaANM_o", 

         "https://www.youtube.com/watch?v=Ojp71GGm-LQ", 

         "https://www.youtube.com/watch?v=Fp8msa5uYsc", 

         "https://www.youtube.com/watch?v=gn0SUZtsr40", 

         "https://www.youtube.com/watch?v=esgt_LWbsVU", 

         "https://www.youtube.com/watch?v=7l2554CnxlQ", 

         "https://www.youtube.com/watch?v=O1IAn0nYiIU", 

         "https://www.youtube.com/watch?v=9NL_b9e4UFE", 

         "https://www.youtube.com/watch?v=OZitHMj25EA", 

         "https://www.youtube.com/watch?v=YyFIKj6yH5Q", 

         "https://www.youtube.com/watch?v=1UCl2cMElds", 

         "https://www.youtube.com/watch?v=VdZps59BGsI", 

         "https://www.youtube.com/watch?v=Hhm9YqZ1_OU", 

         "https://www.youtube.com/watch?v=RgKKgzVhMgY", 

         "https://www.youtube.com/watch?v=pzIBq08Mv7Y", 

         "https://www.youtube.com/watch?v=NjaucnidhkM", 

         "https://www.youtube.com/watch?v=NUUT2oSufdE", 

         "https://www.youtube.com/watch?v=SWbRdCMLjlQ", 

         "https://www.youtube.com/watch?v=5p_CGZHIgaU", 

         "https://www.youtube.com/watch?v=lYNMQBKDhwg", 

         "https://www.youtube.com/watch?v=OrvrHdISmP4", 

         "https://www.youtube.com/watch?v=lEh4_hhZBvo", 

         "https://www.youtube.com/watch?v=LBP4tL9PchU", 

         "https://www.youtube.com/watch?v=yCmSfBMSCi4", 

         "https://www.youtube.com/watch?v=BaRLonlJDOI"] 

  

  

         

    sleep=["https://www.youtube.com/watch?v=Fb1-Diyzvtw", 

           "https://www.youtube.com/watch?v=7OEeWmQuEMg", 

           "https://www.youtube.com/watch?v=jJPMnTXl63E", 

           "https://www.youtube.com/watch?v=LeI63QngLDw", 

           "https://www.youtube.com/watch?v=npbYBDENc_4", 

           "https://www.youtube.com/watch?v=YWOcOChpqdY", 

           "https://www.youtube.com/watch?v=yvhfxMVVNgQ", 

           "https://www.youtube.com/watch?v=k4V3Mo61fJM", 

           "https://www.youtube.com/watch?v=wGF7PswOENQ", 

           "https://www.youtube.com/watch?v=GzKFEx-wsJo", 

           "https://www.youtube.com/watch?v=qN4ooNx77u0", 

           "https://www.youtube.com/watch?v=U7vgH0wTaMs&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0", 

           "https://www.youtube.com/watch?v=pMN7DW4EWLs&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=2", 

           "https://www.youtube.com/watch?v=ulGIdsNaegY&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=3", 

           "https://www.youtube.com/watch?v=ODxBEPD6zJs&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=4", 

           "https://www.youtube.com/watch?v=NDZ8CxplR5c&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=5", 

           "https://www.youtube.com/watch?v=h76tsl-C42c&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=6", 

           "https://www.youtube.com/watch?v=uD8P4OCWuRE&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=7", 

           "https://www.youtube.com/watch?v=bDr5vcVLjNQ&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=8", 

           "https://www.youtube.com/watch?v=ccf0UOjPbig&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=9", 

           "https://www.youtube.com/watch?v=HzrdXSdSyo4&list=OLAK5uy_lAhoYXP7n4eVtA8B9Rmk3buviLCohDHC0&index=10", 

           "https://www.youtube.com/watch?v=mcdO9UP0hp8"] 

  

  

         

    chill=["https://www.youtube.com/watch?v=esh8mNoPxGE", 

           "https://www.youtube.com/watch?v=BFhsW0LxkOQ", 

           "https://www.youtube.com/watch?v=3AyMjyHu1bA", 

           "https://www.youtube.com/watch?v=dPhwbZBvW2o", 

           "https://www.youtube.com/watch?v=XXYlFuWEuKI", 

           "https://www.youtube.com/watch?v=jO2viLEW-1A", 

           "https://www.youtube.com/watch?v=x3bfa3DZ8JM", 

           "https://www.youtube.com/watch?v=OUFuaMj6z-w", 

           "https://www.youtube.com/watch?v=8CEJoCr_9UI", 

           "https://www.youtube.com/watch?v=NKzd_YiW9AQ"] 

         

  

     

    dance=["https://www.youtube.com/watch?v=c5l4CGQozWY", 

           "https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PL64E6BD94546734D8", 

           "https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PL64E6BD94546734D8&index=2", 

           "https://www.youtube.com/watch?v=NUsoVlDFqZg&list=PL64E6BD94546734D8&index=8", 

           "https://www.youtube.com/watch?v=pRpeEdMmmQ0&list=PL64E6BD94546734D8&index=9", 

           "https://www.youtube.com/watch?v=wnJ6LuUFpMo&list=PL64E6BD94546734D8&index=10", 

           "https://www.youtube.com/watch?v=hHUbLv4ThOo", 

           "https://www.youtube.com/watch?v=ebXbLfLACGM", 

           "https://www.youtube.com/watch?v=NOubzHCUt48", 

           "https://www.youtube.com/watch?v=6swmTBVI83k", 

           "https://www.youtube.com/watch?v=Z9eMk051dYg"] 

  

         

  

    workout=["https://www.youtube.com/watch?v=fPO76Jlnz6c", 

             "https://www.youtube.com/watch?v=mk48xRzuNvA", 

             "https://www.youtube.com/watch?v=MJD39Aja1Is", 

             "https://www.youtube.com/watch?v=b3bkpyNiv8Y", 

             "https://www.youtube.com/watch?v=tlnMVb2XVVk", 

             "https://www.youtube.com/watch?v=8CdcCD5V-d8", 

             "https://www.youtube.com/watch?v=jJvDnYdD8JQ", 

             "https://www.youtube.com/watch?v=5l2uJQKbrY4", 

             "https://www.youtube.com/watch?v=9Ko-nEYJ1GE", 

             "https://www.youtube.com/watch?v=LH4Y1ZUUx2g", 

             "https://www.youtube.com/watch?v=Obim8BYGnOE", 

             "https://www.youtube.com/watch?v=HsazP8VAx1c" 

             "https://www.youtube.com/watch?v=v5keWHgf3tk" 

             "https://www.youtube.com/watch?v=0WvrI_fuHBo", 

             "https://www.youtube.com/watch?v=Kbj2Zss-5GY", 

             "https://www.youtube.com/watch?v=x4D3fY6Pb0k", 

             "https://www.youtube.com/watch?v=ltcHzgUc944", 

             "https://www.youtube.com/watch?v=T25OsCc_-bE"] 

  

  

         

    look_sky=["https://www.youtube.com/watch?v=NLbg1UK_d1I", 

              "https://www.youtube.com/watch?v=EI1ZiiIEoU0", 

              "https://www.youtube.com/watch?v=tAGnKpE4NCI", 

              "https://www.youtube.com/watch?v=_hyAOYMUVDs", 

              "https://www.youtube.com/watch?v=Y8DFgALRJ_c", 

              "https://www.youtube.com/watch?v=C54MOn6n_Ao", 

              "https://www.youtube.com/watch?v=RVRPCnl3-HI", 

              "https://www.youtube.com/watch?v=iTLUb5UmeJo", 

              "https://www.youtube.com/watch?v=h5oHhGlWKf0", 

              "https://www.youtube.com/watch?v=-k_bdVJZseU", 

              "https://www.youtube.com/watch?v=hZY5DBmgC_A", 

              "https://www.youtube.com/watch?v=cQpBXn6MYS0", 

              "https://www.youtube.com/watch?v=VYCOg-yglNM", 

              "https://www.youtube.com/watch?v=hJ2t1z3qMPc", 

              "https://www.youtube.com/watch?v=1wYNFfgrXTI", 

              "https://www.youtube.com/watch?v=V5MxQSFsxS4", 

              "https://www.youtube.com/watch?v=PtsMi4dtl1o", 

              "https://www.youtube.com/watch?v=7RW8n4iXZbA", 

              "https://www.youtube.com/watch?v=pVGzzvW3e8E", 

              "https://www.youtube.com/watch?v=7RW8n4iXZbA", 

              "https://www.youtube.com/watch?v=xvzsS70D-iA", 

              "https://www.youtube.com/watch?v=h_GbtBt9pag", 

              "https://www.youtube.com/watch?v=EFJ7kDva7JE", 

              "https://www.youtube.com/watch?v=BaRLonlJDOI", 

              "https://www.youtube.com/watch?v=iLENL7hgy3Y"] 

           

           

           

           

  

  

  

    v=input("Please Choose one of these: cry, sleep, study, dance, workout, falling stars")

    while v!="Chill" and v!="chill" and v!="Falling stars" and v!="falling stars" and v!="workout" and v!="Workout" and v!="Dance" and v!="dance" and v!="Sleep" and v!="sleep" and v!="Study" and v!="study" and v!="Cry" and v!="cry":
        v=input("Please Choose one of these: cry, sleep, study, dance, workout, falling stars")
        
                

  

     

    if v=="Cry" or v=="cry": 

        webbrowser.open(random.choice(cry)) 

  

             

    elif v=="Sleep" or v=="sleep" or v=="Study" or v=="study": 

        webbrowser.open(random.choice(sleep)) 

  

  

    elif v=="Dance" or v=="dance": 

        webbrowser.open(random.choice(dance)) 

  

             

    elif v=="workout"or v=="Workout": 

        webbrowser.open(random.choice(workout)) 

  

             

    elif v=="Falling stars" or v=="falling stars": 

        webbrowser.open(random.choice(look_sky)) 

  

  

    elif v=="Chill" or v=="chill": 

            webbrowser.open(random.choice(chill))         

  

  



  

def lang(): 

  

    english=["https://www.youtube.com/watch?v=HCjNJDNzw8Y", 

             "https://www.youtube.com/watch?v=QK-Z1K67uaA", 

             "https://www.youtube.com/watch?v=5NV6Rdv1a3I", 

             "https://www.youtube.com/watch?v=FM7MFYoylVs", 

             "https://www.youtube.com/watch?v=3AtDnEC4zak", 

             "https://www.youtube.com/watch?v=e-ORhEE9VVg", 

             "https://www.youtube.com/watch?v=lm9cuQdZ_84&list=UUW6LbxBBIhzU9Fn6NjwBN9Q&index=23", 

             "https://www.youtube.com/watch?v=y1QZTu5Z-KU&list=UUW6LbxBBIhzU9Fn6NjwBN9Q&index=29", 

             "https://www.youtube.com/watch?v=IkOfHvRVmiQ&list=UUW6LbxBBIhzU9Fn6NjwBN9Q&index=35", 

             "https://www.youtube.com/watch?v=UJuWZYP28WY&list=UUW6LbxBBIhzU9Fn6NjwBN9Q&index=96", 

             "https://www.youtube.com/watch?v=1C816p-KTNk"] 

  

  

  

    french=["https://www.youtube.com/watch?v=mcdO9UP0hp8", 

            "https://www.youtube.com/watch?v=oiKj0Z_Xnjc&list=PLm1WqxbDXbNCHPH-IXRW0HUacK-xzBr6L", 

            "https://www.youtube.com/watch?v=K5KAc5CoCuk&list=PLm1WqxbDXbNCHPH-IXRW0HUacK-xzBr6L&index=3", 

            "https://www.youtube.com/watch?v=kFzViYkZAz4&list=PLm1WqxbDXbNCHPH-IXRW0HUacK-xzBr6L&index=8", 

            "https://www.youtube.com/watch?v=CAMWdvo71ls", 

            "https://www.youtube.com/watch?v=0TFNGRYMz1U", 

            "https://www.youtube.com/watch?v=JIoj1RYvz1Y", 

            "https://www.youtube.com/watch?v=u7YfOz7g780", 

            "https://www.youtube.com/watch?v=zpnHNoINHoE", 

            "https://www.youtube.com/watch?v=Xe9h4GV2LlY"] 

  

  

  

    spanish=["https://www.youtube.com/watch?v=C4cmJ7QqBMI", 

             "https://www.youtube.com/watch?v=JETyhLQFJW4", 

             "https://www.youtube.com/watch?v=h0Tb9VtVzVE", 

             "https://www.youtube.com/watch?v=pyvqFSGtRM8", 

             "https://www.youtube.com/watch?v=O8BLUzAxNmQ", 

             "https://www.youtube.com/watch?v=ReyXd8aIe3w", 

             "https://www.youtube.com/watch?v=LRUUrEYi31E", 

             "https://www.youtube.com/watch?v=FF1RCLwOCsc", 

             "https://www.youtube.com/watch?v=U6phuhL1YbY", 

             "https://www.youtube.com/watch?v=g-mh4JTOhVw"] 

  

  

  

         

    korean=["https://www.youtube.com/watch?v=0lapF4DQPKQ", 

            "https://www.youtube.com/watch?v=6j928wBZ_Bo", 

            "https://www.youtube.com/watch?v=qGjAWJ2zWWI", 

            "https://www.youtube.com/watch?v=ioNng23DkIM", 

            "https://www.youtube.com/watch?v=ITnT4L988G0", 

            "https://www.youtube.com/watch?v=KM8jo1yCVKc", 

            "https://www.youtube.com/watch?v=Oc4dFGwurT4", 

            "https://www.youtube.com/watch?v=TgOu00Mf3kI", 

            "https://www.youtube.com/watch?v=o-RRkgFylZk", 

            "https://www.youtube.com/watch?v=ZeerrnuLi5E", 

            "https://www.youtube.com/watch?v=tDukIfFzX18", 

            "https://www.youtube.com/watch?v=kVKCQZcCi0M"] 

  

         

  

         

    turkish=["https://www.youtube.com/watch?v=gvcr98QJuFU", 

             "https://www.youtube.com/watch?v=IlHwV0NJ7b0", 

             "https://www.youtube.com/watch?v=oBlHEBLbZJM", 

             "https://www.youtube.com/watch?v=Sad1uVkA_Sk", 

             "https://www.youtube.com/watch?v=4Hd5pdDhF1E", 

             "https://www.youtube.com/watch?v=AYPu4MJGrZU", 

             "https://www.youtube.com/watch?v=gdFVBaZ3EXo", 

             "https://www.youtube.com/watch?v=5My9Jy2hX3o", 

             "https://www.youtube.com/watch?v=sMAnwI_J8iI", 

             "https://www.youtube.com/watch?v=N--rm2BY5Ac", 

             "https://www.youtube.com/watch?v=NjaucnidhkM", 

             "https://www.youtube.com/watch?v=NUUT2oSufdE", 

             "https://www.youtube.com/watch?v=SWbRdCMLjlQ", 

             "https://www.youtube.com/watch?v=24xU6h0kvEs", 

             "https://www.youtube.com/watch?v=cqGuoXn6TeI", 

             "https://www.youtube.com/watch?v=18rJ43ehPEg", 

             "https://www.youtube.com/watch?v=xvzsS70D-iA", 

             "https://www.youtube.com/watch?v=h_GbtBt9pag", 

             "https://www.youtube.com/watch?v=5p_CGZHIgaU", 

             "https://www.youtube.com/watch?v=OZitHMj25EA", 

             "https://www.youtube.com/watch?v=6qRQm2QXDAs", 

             "https://www.youtube.com/watch?v=ilWMorTyclc", 

             "https://www.youtube.com/watch?v=BaRLonlJDOI", 

             "https://www.youtube.com/watch?v=wmZmRxKSCtE", 

             "https://www.youtube.com/watch?v=U2h0SMpdZR4"]
    

    
    m=input("Please choose one of these: Türkçe, English, Korean, French, Spanish")

  

  

    while m!= "spanish" and m!="spanish" and m!= "Korean" and m!= "korean" and m!= "French" and m!= "french" and m!= "Türkçe" and m!="türkçe" and m!= "English" and m!="english":


        m=input("Please choose one of these: Türkçe, English, Korean, French, Spanish") 

  

         

    if m== "English" or m=="english": 

        webbrowser.open(random.choice(english)) 

  

  

  

    elif m== "Türkçe" or m=="türkçe": 

        webbrowser.open(random.choice(turkish)) 

  

         

  

  

    elif m== "French" or m== "french": 

        webbrowser.open(random.choice(french)) 

  

  

  

  

    elif m== "Korean" or m== "korean": 

        webbrowser.open(random.choice(korean)) 

  

  

  

  

    elif m== "Spanish" or m=="spanish": 

        webbrowser.open(random.choice(spanish))

  

def ranbook(): 

  

  

    e=open("All.txt", "r") 

    r=Tk() 

    canvas=Canvas(r, height=600, width=600) 

    canvas.pack() 

    frame_end=Frame(r, bg="purple") 

    frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

    Label(frame_end, bg='purple', text=random.choice(e.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

def typ():
    q=["biographies","Biographies","Fantastic","fantastic", "Fairytale", "fairytale","Children"
       ,"children", "sport", "Sport", "economy", "Economy", "science", "Science", "Philosophy", "philosophy","History","history"]

  

    last_message="" 

    s=input("Please Choose type") 

  

    while s not in q:

            last_message+= "Please choose one of these: Biographies, Fantastic, Fairytale, Children, Sport, Economy, Science, Philosophy, History"
            messagebox.showinfo("Constraints", last_message)
            s=input("Please Choose type")
            

    if s==q[16] or s==q[17]: 

        a=open("history.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

             

    elif s==q[15] or s==q[14]: 

        a=open("philosophy.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

             

    elif s==q[13] or s==q[12]: 

        a=open("science.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

             

    elif s==q[11] or s==q[10]: 

        a=open("economy.txt","r") 

         

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

             

    elif s==q[9] or s==q[8]: 

        a=open("Sport.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

             

    elif s==q[7] or s==q[6]: 

        a=open("Children.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

             

    elif s==q[5] or s==q[4]: 

        a=open("Fairytale.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

          

             

    elif s==q[3] or s==q[2]: 

        a=open("Fantastic.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

         

  

    elif s==q[1] or s==q[0]: 

        a=open("biographies.txt","r") 

  

        r=Tk() 

        canvas=Canvas(r, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(r, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(a.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

  

  

  

     

     

def aut():
    q=["Peter Handke", "peter handke", "Louise Glück", "louise glück", "Harold Pinter", "harold pinter", "Stefan Zweig", "stefan zweig", "Dostoyevski", "dostoyevski",
       "Tolstoy", "tolstoy", "Alexander Pushkin", "alexander pushkin", "Jules Verne", "jules verne", "Oğuz Atay", "oğuz atay","Goethe","goethe", "Jack London", "jack london",
       "Victor Hugo", "victor hugo", "Oscar Wilde", "oscar wilde", "George Orwell", "george orwell"]
       

  

  

    ü=input("Please enter author name") 

    last_message= ""
    while ü not in q:
        last_message += "Please choose one of these: Louise Glück, Peter Handke, Harold Pinter, Stefan Zweig, Dostoyevski, Tolstoy, Alexander Pushkin, Jules Verne, Oğuz Atay, Goethe, Jack London ,Victor Hugo, Oscar Wilde, George Orwell" 

        messagebox.showinfo("Constraints", last_message)
        ü=input("Please enter author name")
        

    if ü==q[0] or ü==q[1]: 

        d=open("peterhandke (1).txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

           

               

    elif ü==q[2] or ü==q[3]: 

        d=open("louiseglück (1).txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

         

  

    elif ü==q[4] or ü==q[5]: 

        d=open("haroldpinter.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

         

  

    elif ü==q[6] or ü==q[7]: 

        d=open("stefanzweig.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

         

  

    elif ü==q[8] or ü==q[9]: 

        d=open("dostoyevski.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

         

  

    elif ü==q[10] or ü==q[11]: 

        d=open("tolstoy.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

         

  

    elif ü==q[12] or ü==q[13]: 

        d=open("pushkin.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

         

  

    elif ü==q[14] or ü==q[15]: 

        d=open("verne.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

  

    elif  ü==q[16] or ü==q[17]: 

        d=open("oguzatay.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

  

    elif ü==q[18] or ü==q[19]: 

        d=open("goethe.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

  

    elif ü==q[20] or ü==q[21]: 

        d=open("jacklondon.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

  

    elif ü==q[22] or ü==q[23]: 

        d=open("hugo.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

    elif ü==q[24] or ü==q[25]: 

        d=open("oscarwilde.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

  

    elif ü==q[26] or ü==q[27]: 

        d=open("orwell.txt","r") 

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

        frame_end=Frame(e, bg="purple") 

        frame_end.place(relx=0, rely=0, relwidth=1, relheight=1) 

        Label(frame_end, bg='purple', text=random.choice(d.readlines()), font='Verdana 12 bold', fg='white').place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

     

  

     

     

def submit(): 

  

    if v.get()==1: 

  

  

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

  

        frame_up=Frame(e, bg="purple") 

        frame_up.place(relx=0, rely=0, relwidth=1, relheight=0.2) 

  

        frame_down=Frame(e, bg="white") 

        frame_down.place(relx=0, rely=0.2, relwidth=1, relheight=0.8) 

  

        Label(frame_up, bg='purple', text="CHOOSE THE TYPE OF SUGGESTION",font='Verdana 18 bold', fg='white').pack(pady=40) 

  

         

  

        ran=Radiobutton(frame_down, text="RANDOM IN TOP 100",  bg="purple", fg="white", cursor="heart", activebackground = "green", command= randm, font="Verdana 10  bold").place(relx=0.0200, rely=0.2, relwidth=0.30, relheight=0.6) 

  

        emo=Radiobutton(frame_down, text="BASED ON EMOTION",  bg="purple", command= emoo, cursor="heart", activebackground = "green", fg="white", font="Verdana 10 bold").place(relx=0.350, rely=0.2, relwidth=0.30, relheight=0.6) 

  

        sim=Radiobutton(frame_down, text="SIMILAR TO ...",  bg="purple", fg="white",command= simi, cursor="heart", activebackground = "green" , font="Verdana 10 bold").place(relx=0.6750, rely=0.2, relwidth=0.30, relheight=0.6) 

  
        e.mainloop
  

  

    elif v.get()==2: 

  

  

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

  

        frame_up=Frame(e, bg="purple") 

        frame_up.place(relx=0, rely=0, relwidth=1, relheight=0.2) 

  

        frame_down=Frame(e, bg="white") 

        frame_down.place(relx=0, rely=0.2, relwidth=1, relheight=0.8) 

  

        Label(frame_up, bg='purple', text="CHOOSE THE TYPE OF SUGGESTION",font='Verdana 18 bold', fg='white').pack(pady=40) 

  

         

        ran=Radiobutton(frame_down, text="RANDOM IN SPOTIFY",  bg="purple", fg="white", activebackground = "green", cursor="heart", command= ranmus, font="Verdana 8 bold").place(relx=0.0200, rely=0.2, relwidth=0.30, relheight=0.6) 

  

        emo=Radiobutton(frame_down, text="ACCORDING TO ACTION",  bg="purple", command= act, fg="white", cursor="heart", activebackground = "green" , font="Verdana 8 bold").place(relx=0.350, rely=0.2, relwidth=0.30, relheight=0.6) 

  

        sim=Radiobutton(frame_down, text="IN ANOTHER LANGUAGE",  bg="purple", fg="white",command= lang , cursor="heart", activebackground = "green" , font="Verdana 8 bold").place(relx=0.6750, rely=0.2, relwidth=0.30, relheight=0.6) 

  
        e.mainloop
  

    elif v.get()==3: 

  

  

        e=Tk() 

        canvas=Canvas(e, height=600, width=600) 

        canvas.pack() 

  

        frame_up=Frame(e, bg="purple") 

        frame_up.place(relx=0, rely=0, relwidth=1, relheight=0.2) 

  

        frame_down=Frame(e, bg="white") 

        frame_down.place(relx=0, rely=0.2, relwidth=1, relheight=0.8) 

  

        Label(frame_up, bg='purple', text="CHOOSE THE TYPE OF SUGGESTION",font='Verdana 18 bold', fg='white').pack(pady=40) 

  

         

        ran=Radiobutton(frame_down, text="RANDOM",  bg="purple", fg="white",activebackground = "green", command= ranbook, cursor="heart", font="Verdana 10  bold").place(relx=0.0200, rely=0.2, relwidth=0.30, relheight=0.6) 

  

        emo=Radiobutton(frame_down, text="GENRE",  bg="purple", command= typ, fg="white",activebackground = "green", cursor="heart", font="Verdana 10 bold").place(relx=0.350, rely=0.2, relwidth=0.30, relheight=0.6) 

  

        sim=Radiobutton(frame_down, text="AUTHOR",  bg="purple", fg="white",activebackground = "green" ,command= aut, cursor="heart", font="Verdana 10 bold").place(relx=0.6750, rely=0.2, relwidth=0.30, relheight=0.6) 

        e.mainloop

v=IntVar()     

Mo= Radiobutton(frame_seçim, text="MOVIE", variable= v, value=1, bg="purple", fg="white",activebackground = "green", cursor="star", font="Verdana 30 bold").place(relx=0.0200, rely=0.2, relwidth=0.30, relheight=0.6) 

  

Mu= Radiobutton(frame_seçim, text="MUSIC", variable= v, value=2, bg="purple", fg="white",activebackground = "green", cursor="star", font="Verdana 30 bold").place(relx=0.350, rely=0.2, relwidth=0.30, relheight=0.6) 

  

Bo= Radiobutton(frame_seçim, text="BOOK", variable= v, value=3, bg="purple", fg="white",activebackground = "green", cursor="star", font="Verdana 30 bold").place(relx=0.6750, rely=0.2, relwidth=0.30, relheight=0.6) 

  

sub= Button(frame_seçim, text="submit", command=submit, bg="white", fg="purple", font="Verdana 10 bold").place(relx=0.3, rely=0.8, relwidth=0.40, relheight=0.19) 

  

m.mainloop() 

 



 

