from functools import reduce


def meeting(s):
    name = [i.split(":")[::-1] for i in s.upper().split(";")]
    name.sort(key=lambda x: x[0]+" "+x[1])
    return reduce(lambda acc, x: acc+"("+x[0]+", "+x[1]+")", name, "")


s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))
