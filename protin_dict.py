f=open('protein.txt','r')

protein_map=dict()
i=0
for line in f:
    if i%2==0 :
       tRNA=line.strip()
    else:
        protein=line[2:].strip()
        print tRNA+" "+protein
        protein_map[tRNA]=protein
    i+=1

f.close()
