from calendar import Calendar 
import funcy as F

horizontal_line = "|" + "-" * 188 + "|"
weekdays = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

#print(horizontal_line)
print("|" + "".join(F.lmap(lambda s: " "*12 + s +  " "*11 + "|", weekdays)))
print(horizontal_line)

# 2020/3
cal = Calendar()
#dates = list(cal.itermonthdates(2020,3))[7:]
dates = list(cal.itermonthdates(2020,5))[28:] + list(cal.itermonthdates(2020,6))[:28]
#dates = list(cal.itermonthdates(2020,6))#[7:]
#assert len(dates) == 35
date_strs = F.lmap(lambda d: d.strftime("%m/%d"), dates)
weeks = F.lpartition(7, date_strs)

row_y = 0
for line_y in range(59):
    in_box_y = line_y % 12
    if in_box_y == 0:
        week = weeks[row_y]
        inner_line = "".join(F.map(lambda d: d + " " * 15 + "study |", week))
        s = "|" + inner_line
        row_y += 1
    elif in_box_y == 1: s = "|" + (         " " * 26            + "|") * 7;
    elif in_box_y == 2: s = "|" + ("w-up" + " " * 16 + "paper " + "|") * 7;
    elif in_box_y == 3: s = "|" + (         " " * 26            + "|") * 7;
    elif in_box_y == 4: s = "|" + ("weig" + " " * 16 + " data " + "|") * 7;
    elif in_box_y == 5: s = "|" + (         " " * 26            + "|") * 7;
    elif in_box_y == 6: s = "|" + ("exer" + " " * 16 + "nnlab " + "|") * 7;
    elif in_box_y == 7: s = "|" + (         " " * 26            + "|") * 7;
    elif in_box_y == 8: s = "|" + ("diet" + " " * 16 + " icom " + "|") * 7;
    elif in_box_y == 9: s = "|" + (         " " * 26            + "|") * 7;
    elif in_box_y ==10: s = "|" + (" bed" + " " * 6  + " etc            "   + "|") * 7;
    elif in_box_y ==11: s = horizontal_line
    print(s);         
print(horizontal_line)
