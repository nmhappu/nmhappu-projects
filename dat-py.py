import pickle
s = {}
nw_file = open("m.txt","wb")
cx = "y"
while cx == "y":
    r = int(input("Enter the roll no:"))
    name = input("Enter your name:")
    mark = int(input("Enter your marks:"))
    s["Roll No:"] = r
    s["Name"] = name
    s["Marks"] = mark
    pickle.dump[s]