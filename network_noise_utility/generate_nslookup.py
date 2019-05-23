
import os, random, time

os.system("echo test")

final_list = []
with open("nslookup.txt", 'r') as n:
    for l in n:
        l2 = l.strip()
        if l2 and len(l2) > 0:
            l3 = []
            l3 = l2.split(" ")
            l4 = ""
            print l3[-1]
            for s in l3:
                if s not in l3[-1]:
                    l4 = l4+s+"_"
                else:
                    l4 = l4+s
            print l4
            final_list.append(l4.lower())

i = 0
random.shuffle(final_list)
print "=================================="
while True:
    for item in final_list:
        #print i
        i+=1
# creates text file with name pulled from text file and writes these lines inside.
#    with open(item, 'w') as p:
#        p.write ("echo " +item+"\n")
#        p.write("sleep 3"+"\n")
#        p.write("echo BYE!\n")
#        p.write("echo exit\n")


        command = "nslookup "+item+""
        os.system(command)
    #print command
        time.sleep(random.uniform(1,5))
