#1

#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while True:
#    if vastus!=o_vastus:
  #   print("Viga! Siseta Õige vastus on ...",)
  #   vastus=int(input("Siseta vastus ..."))
  #   k+=1
 #   else:
 #      break
#print("Õige vastus! Katsed´oli ...",k )
#print()



#2
#print("Ülesanne 2")
#x=0

#while True:

    #if x%2==1:

        #print(x, end=" ")
    #x+=1
    #if x==30: break

    #x+=1
    #if x==30: break
#print("For:")
#for x in range (0,30,1):
    #if x%2==1: print (x, end=" ")






print("***NUMBRIDEGA MÄNGUD***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a  #eemaldatud võrdub
    paaris=0   #eemaldatud võrdub ja ruumid
    paaritu=0   #eemaldatud võrdub ja ruumid
    while b > 0:   #parandatud:
            if b % 2 == 0:  #lisatud teine ​​=
                    paaris += 1   #vahetatud + märk
            else:
                    paaritu += 1   #vahetatud + märk
            b = b // 10  #alla kolis if
       #eemaldatud lisarida
    print("Paarisarvud:",paaris)  #pane kooloni järele koma
    print("paarituid numbreid:",paaritu)  #pane kooloni järele koma
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0: #pane koolon
        number = a % 10
        a = a // 10
        b = b * 10
        b += number  #eemaldas ruumi
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Syracuse hüpoteesi testimine"))  #lisatud sulg
    print()
    if c % 2 == 0:  #lisatud võrdsed
        print("с - paarisarv. Jagage 2.")
    else:
        print("с - paaritu number. Korrutage 3 lisage 1 ja jagage 2-.")
    while c != 1:
            if c % 2 == 0:  #lisatud võrdsed
                    c = c / 2   #eemaldatud võrdub
            else:
                    c = (3*c + 1) / 2
            print(c, end=" ")  #lisatud tsitaate
    print()
    print("Hüpotees on õige")  #lisatud tsitaate
