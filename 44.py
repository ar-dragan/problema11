n=int(input('Dati numarul de elemente din vector='))
while n>10:
    n=int(input('Introduceti un numar mai mic decat 10: '))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[::5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
print(a[::-1])
print('c)  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d)  afişează pe ecran doar componentele pare;')
p=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        p.extend([y])
print(p)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
print(round(sum(p)/len(p),2))
print('f)  afişează pe ecran doar componentele impare;')
im=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        ia=a[i]
        im.extend([ia])
print(im)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input("x="))
y=int(input("y="))
v=[]
for i in a:
    if ((i>x)and(i%y!=0)):
        z=i
        v.extend([z])
print(v)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
kl=[]
for i in a:
    if ((i>x)and(i<y)):
        y=i
        kl.extend([y])
print(kl)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
e=[]
for i in im:
    if i<0:
        e.extend([a.index(i)])
print(e)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
j=[]
for i in range(0,len(a)):
    if a[i]>9 and a[i]<100:
        o=i
        j.extend([o])
print(j)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
e=[]
for i in range(0,len(a)):
    y=a[i]
    e.extend([y])
t=min(e)
e[0]=t
print(e)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
v=[]
for i in range(0,len(a)):
    y=a[i]
    v.extend([y])
t=min(v)
v[v.index(min(v))]=v[0]
print(v)

print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print('lista din componentele pare este',c)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
d=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        y=a[i]
        d.extend([y])
print('lista din componentele divizibile cu 3 este',d)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori;')
o=[]
for i in a:
    if i>0:
        k=0
        for j in range(1,i+1):
            if (i%j==0):
               k+=1
        if k<=4:
            o.extend([i])
print(o)