crickets=[{"name" :"john",
          "countries_num": 1,
          "centuries" :30,
          "half-centuries":10 ,
          "wickets taken":6,
          "batting score":[7,6,3,4,5],
          "hat-trick wickets" :10},

          {"name" :"Emily",
          "countries_num": 2,
          "centuries":12,
          "half-centuries":20 ,
          "wickets taken": 3,
          "batting score":[5,7,3,6,8],
          "hat-trick wickets" : 1},

         {"name" :"michael",
          "countries_num": 3,
          "centuries" :8,
          "half-centuries":30 ,
          "wickets taken": 9,
          "batting score":[10,2,4,5,7],
          "hat-trick wickets" : 3},
           
           {"name" :"sarah",
          "countries_num": 4,
          "centuries":20,
          "half-centuries":40 ,
          "batting score":[30,12,34,8,7],
          "wickets taken":9,
          "hat-trick wickets" : 3},
           
           {"name" :"shiva",
          "countries_num": 5,
          "centuries":5,
          "half-centuries": 50,
          "wickets taken": 3,
          "batting score":[60,2,42,6,28],
          "hat-trick wickets" :8 } ]

def scored(crickets):
    num_of_player=0
    for cricket in crickets:
     if cricket["centuries"]>10:
        num_of_player=num_of_player+1
        print("num of players :",num_of_player)
scored(crickets) 

def hat_wickets(crickets):
   for cricket in crickets:
      if cricket["hat-trick wickets"]>5:
        print("player name :",cricket["name"], " . player countries :",cricket["countries_num"],". Above 5 hat-trick wickets :",cricket["hat-trick wickets"],".")
hat_wickets(crickets)  

def batting(crickets):
   top_batting_score=0
   for i in crickets:
      for one in i["batting score"]:
       if top_batting_score <one:
         top_batting_score=one
         print(f"player name :",crickets["name"], ". Top batting score :",{top_batting_score})
batting(crickets)           


