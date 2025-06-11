text = input("Matni kiriting: ")
letter = "Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M"
hisob = 0

for i in text:
    if i in letter:
      hisob += 1
print(f"Katta harflar soni {hisob}")