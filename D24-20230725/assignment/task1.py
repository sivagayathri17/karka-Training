rates=[{"month":"jan",
        "g_rate":1500,
        "j_lists":[{"name":"chain",
                    "making_cost":12},
                    {"name":"ring",
                    "making_cost":8}]},
        {"month":"feb",
        "g_rate":2000,
        "j_lists":[{"name":"chain",
                    "making_cost":10},
                    {"name":"ring",
                    "making_cost":6}]
                    }]
data=[]

for rate in rates:
    g_rate=(rate["g_rate"])
    lists=(rate["j_lists"])
    month=rate["month"]
    
    dic={}
    dic["month"]=month
    dic["gold_ rate"]=g_rate
    for list in lists:
        m_lists=(list["making_cost"])
        # print(m_lists)
        name=(list["name"])
        
        cost=g_rate*(m_lists/100)
        add_cost=cost+g_rate
        dic[name]=add_cost
        # print(cost)
        # print(add_cost)
        # print(f"month:{month} \n gold rate :{g_rate}\n {name}rate :{add_cost}\n ")
    data.append(dic)
print(data)    
        



