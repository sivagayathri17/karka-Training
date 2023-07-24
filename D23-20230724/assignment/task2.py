months_gold_rates=[{"month":"jan",
                   "g_rate":1000},
                   {"month":"feb",
                    "g_rate":1500},
                    {"month":"mar",
                     "g_rate":2000}]


num=months_gold_rates[0]["g_rate"]
for months_gold_rate in months_gold_rates:
    rates=months_gold_rate["g_rate"]
    month=months_gold_rate["month"]
    # print(rates)
    if num>=rates:
       num= rates
       month1=month     
print(num) 
# print(month1)
print(f"{month1} : {num}")

    
    


    
       
        
