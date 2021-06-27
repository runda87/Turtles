
import csv

turtle20_21 = []

with open("data/2020_2021_turtle_data.csv", encoding="utf-8") as csv_file:
    reader = csv. reader(csv_file)
    for line in reader:
        turtle20_21.append(line)


# i = 0
# while i < len(turtle20_21):
#     print(f"{turtle20_21[i][0]} {turtle20_21[i][1]} {turtle20_21[i][2]} {turtle20_21[i][3]} {turtle20_21[i][4]} {turtle20_21[i][5]}")
#     i = i + 1


totals = turtle20_21[1:13]
oct_nest = []
oct_false_crawls_count = []
oct_hit_rocks = []
oct_hatched_nests = []
oct_nest_predation = []
oct_n = 0
oct_fc = 0
oct_hr = 0
oct_hn = 0
oct_np = 0 
for row in totals:     
        oct_nest.append(row[1])
        oct_n= oct_n+int(row[1])

        oct_false_crawls_count.append(row[2])
        oct_fc= oct_fc+int(row[2])

        oct_hit_rocks.append(row[3])
        oct_hr= oct_hr+int(row[3])

        oct_hatched_nests.append(row[4])
        oct_hn= oct_hn+int(row[4])

        oct_nest_predation.append(row[5])
        oct_np= oct_np+int(row[5])


totals = turtle20_21[14:43]
nov_nest = []
nov_false_crawls_count = []
nov_hit_rocks = []
nov_hatched_nests = []
nov_nest_predation = []
nov_n = 0
nov_fc = 0
nov_hr = 0
nov_hn = 0
nov_np = 0 
for row in totals:
        nov_nest.append(row[1])
        nov_n= nov_n+int(row[1])

        nov_false_crawls_count.append(row[2])
        nov_fc= nov_fc+int(row[2])

        nov_hit_rocks.append(row[3])
        nov_hr= nov_hr+int(row[3])

        nov_hatched_nests.append(row[4])
        nov_hn= nov_hn+int(row[4])

        nov_nest_predation.append(row[5])
        nov_np= nov_np+int(row[5])


totals = turtle20_21[42:73]
dec_nest = []
dec_false_crawls_count = []
dec_hit_rocks = []
dec_hatched_nests = []
dec_nest_predation = []
dec_n = 0
dec_fc = 0
dec_hr = 0
dec_hn = 0
dec_np = 0 
for row in totals:
        dec_nest.append(row[1])
        dec_n= dec_n+int(row[1])

        dec_false_crawls_count.append(row[2])
        dec_fc= dec_fc+int(row[2])

        dec_hit_rocks.append(row[3])
        dec_hr= dec_hr+int(row[3])

        dec_hatched_nests.append(row[4])
        dec_hn= dec_hn+int(row[4])

        dec_nest_predation.append(row[5])
        dec_np= dec_np+int(row[5])


totals = turtle20_21[73:103]
jan_nest = []
jan_false_crawls_count = []
jan_hit_rocks = []
jan_hatched_nests = []
jan_nest_predation = []
jan_n = 0
jan_fc = 0
jan_hr = 0
jan_hn = 0
jan_np = 0 
for row in totals:
        jan_nest.append(row[1])
        jan_n= jan_n+int(row[1])

        jan_false_crawls_count.append(row[2])
        jan_fc= jan_fc+int(row[2])

        jan_hit_rocks.append(row[3])
        jan_hr= jan_hr+int(row[3])

        jan_hatched_nests.append(row[4])
        jan_hn= jan_hn+int(row[4])

        jan_nest_predation.append(row[5])
        jan_np= jan_np+int(row[5])


totals = turtle20_21[103:115]
feb_nest = []
feb_false_crawls_count = []
feb_hit_rocks = []
feb_hatched_nests = []
feb_nest_predation = []
feb_n = 0
feb_fc = 0
feb_hr = 0
feb_hn = 0
feb_np = 0 
for row in totals:
        feb_nest.append(row[1])
        feb_n= feb_n+int(row[1])

        feb_false_crawls_count.append(row[2])
        feb_fc= feb_fc+int(row[2])

        feb_hit_rocks.append(row[3])
        feb_hr= feb_hr+int(row[3])

        feb_hatched_nests.append(row[4])
        feb_hn= feb_hn+int(row[4])

        feb_nest_predation.append(row[5])
        feb_np= feb_np+int(row[5])


totals = turtle20_21[114:115]
mar_nest = []
mar_false_crawls_count = []
mar_hit_rocks = []
mar_hatched_nests = []
mar_nest_predation = []
mar_n = 0
mar_fc = 0
mar_hr = 0
mar_hn = 0
mar_np = 0 
for row in totals:
        mar_nest.append(row[1])
        mar_n= mar_n+int(row[1])

        mar_false_crawls_count.append(row[2])
        mar_fc= mar_fc+int(row[2])

        mar_hit_rocks.append(row[3])
        mar_hr= mar_hr+int(row[3])

        mar_hatched_nests.append(row[4])
        mar_hn= mar_hn+int(row[4])

        mar_nest_predation.append(row[5])
        mar_np= mar_np+int(row[5])


total_nests = [oct_n + nov_n + dec_n + jan_n + feb_n + mar_n]
t_nests ="".join(str(total_nests)[1:-1])
total_n= int(t_nests)

total_hatched_nests = [oct_hn + nov_hn + dec_hn + jan_hn + feb_hn + mar_hn]
t_hn ="".join(str(total_hatched_nests)[1:-1])
total_hn = int(t_hn)

total_false_crawls = [oct_fc + nov_fc + dec_fc + jan_fc + feb_fc + mar_fc]
t_fc ="".join(str(total_false_crawls)[1:-1])
total_fc = int(t_fc)

total_hit_rocks = [oct_hr + nov_hr + dec_hr + jan_hr + feb_hr + mar_hr]
t_hr ="".join(str(total_hit_rocks)[1:-1])
total_hr = int(t_hr)

total_nest_predation = [oct_np + nov_np + dec_np + jan_np + feb_np + mar_np]
t_np ="".join(str(total_nest_predation)[1:-1])
total_np = int(t_np)


print()
print()
print(f"2020/2021 Flat Back Turtle Migration at Cemetery Beach ")
print()
print()
print(f"Number of Nests recorded per month (X = 5 nests):")
print(f"October     {oct_n}")
print(f"November    {nov_n}")
print(f"December    {dec_n}")
print(f"January     {jan_n}")
print(f"Feburay     {feb_n}")
print(f"March       {mar_n}")
print()
print()
print(f"Monthly Statistics:")
print(f"Months      Nests   Hatched Nests   False Crawls    Hit Rocks   Nest Predation")
print(f"October     {oct_n}     {oct_hn}        {oct_fc}        {oct_hr}        {oct_np} ")
print(f"November    {nov_n}     {nov_hn}        {nov_fc}        {nov_hr}        {nov_np} ")
print(f"December    {dec_n}     {dec_hn}        {dec_fc}        {dec_hr}        {dec_np} ")
print(f"January     {jan_n}     {jan_hn}        {jan_fc}        {jan_hr}        {jan_np} ")
print(f"Feburay     {feb_n}     {feb_hn}        {feb_fc}        {feb_hr}        {feb_np} ")
print(f"March       {mar_n}     {mar_hn}        {mar_fc}        {mar_hr}        {mar_np} ")
print()
print()
print(f"Overall:")
print(f" Nests - {total_n}")
print(f" Hatched Nests - {total_hn}")
print(f" False Crawls - {total_fc}")
print(f" Hit Rocks - {total_hr}")
print(f" Nest Predation - {total_np}")