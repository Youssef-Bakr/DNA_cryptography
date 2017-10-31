
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




f=open('ascii.txt','r')
char_map=dict()

for line in f:
    line=line.strip().split('\t')
    char_map[line[0]]=line[1]
    print line[0]+"\t"+line[1]

f.close()




def complement(DNA):
    _DNA=""
    for char in DNA:
        if char == 'A':
            _DNA+='T'
        elif char == 'T':
            _DNA+='A'
        elif char == 'C':
            _DNA+='G'
        elif char == 'G':
            _DNA+='C'

    return _DNA




def complement_tRNA(tRNA):
    mRNA=""
    for char in tRNA:
        if char == 'A':
            mRNA+='U'
        elif char == 'U':
            mRNA+='A'
        elif char == 'C':
            mRNA+='G'
        elif char == 'G':
            mRNA+='C'

    return mRNA

def DNA2Binary(DNA):
    binary=""
    for ch in DNA:
        if ch=='A':
            binary+="00"
        elif ch=='T':
            binary+="01"
        elif ch=="C":
            binary+="10"
        else:
            binary+="11"

    return binary
        
      

def convert(plain):
    DNA=""
    for ch in plain:
        DNA+=char_map[ch]

    return DNA



def convert2mRNA(DNA):
    _mRNA=DNA.replace("T","U")
    return _mRNA
   

def convert2DNA(mRNA):
    DNA=mRNA.replace("U","T")
    return DNA
   


def rightShift(DNA):
    return DNA[-1:] + DNA[:-1]   


def XNOR_and_convert2DNA(binary,intron):
    dict1={'00':'A', '01':'T', '10':'C', '11':'G'}

    _intron=""
    for i in range(len(binary)/4):
        _intron+=intron

    print binary
    print _intron

    xnor=""
    
    for i in range(len(binary)):
        if binary[i]==_intron[i] :
            xnor+="1"
        else:
            xnor+="0"

    print xnor

    DNA=""
    
    for i in range(len(xnor)/2):
        DNA+=dict1[xnor[i*2:i*2+2]]

    print DNA
    return DNA
    




cipher=input("\n\nEnter cipher text: ")
intron=input("\n\nEnter intron sequence: ")
n=input("\nEnter num. of itereations: ")

intron1=intron[:4]
intron2=intron[4:]

print "\nintron1 :" + intron1
print "intron2 :" + intron2


print("\nCIPHER TEXT\n")
if len(plai)%2==0:
    cipher1=cipher[:len(cipher)/2]
    cipher2=cipher[len(cipher)/2:]
else:
    cipher1=cipher[:len(cipher)/2 + 1]
    cipher2=cipher[len(cipher)/2+1:] + "#"

print cipher1
print cipher2
    

print("\nDNA\n")
tRNA1=convert_to_tRNA(cipher1)
print tRNA1
tRNA2=convert_to_tTRNA(cipher2)
print tRNA2


print("\nmRNA:")
mRNA1 = convert2mRNA(DNA1)
print mRNA1
mRNA2 = convert2mRNA(DNA2)
print mRNA2



print("\nmRNA:")
DNA1 = convert2DNA(tRNA1)
print mRNA1
DNA2 = convert2DNA(tRNA2)
print mRNA2


    

for i in range(n):

    print("\n\nIteration : "+str(i))

    binary1 = DNA2Binary(DNA1)
    binary2 = DNA2Binary(DNA2)
    print "\nbinary sequence1 : "+ binary1
    print "binary sequence2 : "+ binary2


    DNA1=XNOR_and_convert2DNA(binary1,intron1)
    DNA2=XNOR_and_convert2DNA(binary2,intron2)


    print("\nL-Shift:")
    DNA1 = leftShift(DNA1)
    print DNA1
    DNA2 = leftShift(DNA2)
    print DNA2

    
    print("\nmRNA:")
    mRNA1 = convert2mRNA(DNA1)
    print mRNA1
    mRNA2 = convert2mRNA(DNA2)
    print mRNA2

    print("\ntRNA:")
    tRNA1 = complement_tRNA(mRNA1)
    print tRNA1
    tRNA2 = complement_tRNA(mRNA2)
    print tRNA2

    print("\nDNA:")
    DNA1 = convert2DNA(tRNA1)
    print DNA1
    DNA2 = convert2DNA(tRNA2)
    print DNA2




_PT=DNA1+DNA2
_PT=convert2mRNA(_PT)
_PT=complement_tRNA(_PT)


print ("\n\nIntermediate result : " + (_PT))

PT=""

for i in range(len(_PT)/4):
    PT+=char_map[_PT[i*4:i*4+4]]


print ("\n\nPLAIN TEXT : " + PT)


