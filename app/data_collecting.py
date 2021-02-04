import pandas as pd
import random
import numpy as np

class dataCollecting:

    def return_activities_places(self, what, location, animation, city):

        if what == "sport":
            if location == "interior":
                if animation == "foule":

                    print("Rien pour le moment, on sait qu'il y a le laser game")
                
                elif animation == "solo":

                    print("Rien pour le moment, salle de fitness à ajouter")
            
            elif location =="exterior":
                if animation == "foule":

                    df = pd.read_csv("assets/festivMF.csv")
                
                elif animation == "solo":

                    files["Data/hannut_centre_equestre.csv", '"Data/marche_pt_vert.csv"']
                    i = random.randint(len(files))
                    df = pd.read_csv(files[i])
        
        elif what == "musee":
            if location == "interior":
                if animation == "foule":

                    files['assets/brasserieMF.csv', 'assets/cinemaMF.csv']
                    i = random.randint(len(files))
                    df = pd.read_csv(files[i])
                
                elif animation == "solo":

                    files['assets/museesMF.csv', 'Data/hannut_femme_detente.csv']
                    i = random.randint(len(files))
                    df = pd.read_csv(files[i])
            
            elif location =="exterior":
                if animation == "foule":
                    print('rien pour le moment, on pourra mettre les marchés, evenement culturelle, marché artisanal')
                
                elif animation == "solo":
                    df = pd.read_csv('assets/patrimonesMF.csv')
        return df


    
    def create_list_csv_by_city(self, file_name, city_name):
        """This function will sort the database according to the city, so it will take only places which are in the city
        and return it"""

        #We couldn't make it for this hackathon because we hadn't enough data and especially good data
        pass

    def choose_a_place(self, df, persona):
        """This function will choose place according to criteria, but since for now we didn't have enough response
        we make a mock to be able to finish our project. This function will give point according to the persona
        and will put in descending order"""

        score = np.array([[5, 0, 3, 3, 3], 
                          [3, 5, 4, 4, 1],
                          [2, 3, 5, 4, 4],
                          [3, 3, 3, 5, 3],
                          [3, 1, 3, 4, 5]])

        if persona == "famille":
            if df['type'] == "famille":
                df['score'] = 5
            elif df["type"] == "solo":
                df['score'] = 0
            elif df['type'] == "friends":
                df['score'] = 3
            elif df['type'] == "tourist":
                df['score'] = 3
            elif df['type'] == "couple":
                df['score'] = 3