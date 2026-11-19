import re,sys
L=open('raw/figueiredo_1828_djvu.txt',encoding='utf-8').read().split('\n')
R={'mt':(128058,133378),'mc':(133378,136673),'lc':(136673,142344),'io':(142344,146400),'act':(146400,150500),'ap':(166200,169000)}
def rom(n):
    v=[(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')];s=''
    for a,b in v:
        while n>=a: s+=b;n-=a
    return s
b,c,v0,v1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
a,z=R[b]
hs=[i for i in range(a,z) if re.match(r'^\s*CAP[IÍ]TULO\s+'+rom(c)+r'\.\s*$',L[i])]
if not hs: print('NO HEAD',b,c); sys.exit()
i=hs[0]; j=i+1
while j<z and not re.match(r'^\s*CAP[IÍ]TULO\s+'+rom(c+1)+r'\.\s*$',L[j]): j+=1
seg=[l for l in L[i:j] if l.strip()]
# crude: find line starting with verse v0 and v1+1
def find(n,start=0):
    for k in range(start,len(seg)):
        if re.match(r'^\s*'+' ?'.join(str(n))+r'\s',seg[k]): return k
    return None
s=find(v0) if v0>1 else 0
e=find(v1+1,(s or 0)+1)
print(f'## {b} {c},{v0}-{v1}  (lines {s}-{e} of {len(seg)})')
print('\n'.join(seg[(s or 0):(e if e else (s or 0)+40)]))
