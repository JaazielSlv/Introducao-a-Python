p1 = input("Primeira palavra ")
p2 = input("Segunda palavra ")
p3 = input("Terceira palavra ")

if (p1 == "vertebrado") & (p2 == "ave") & (p3 == "carnivoro"): print("Aguia")
elif (p1 == "vertebrado") & (p2 == "ave") & (p3 == "onivoro"): print("pomba")
elif (p1 == "vertebrado") & (p2 == "mamifero") & (p3 == "onivoro"): print("homem")
elif (p1 == "vertebrado") & (p2 == "mamifero") & (p3 == "herbivoro"): print("vaca")
elif (p1 == "inertebrado") & (p2 == "inseto") & (p3 == "hematofago"): print("pulga")
elif (p1 == "inertebrado") & (p2 == "inseto") & (p3 == "herbivoro"): print("lagarta")
elif (p1 == "inertebrado") & (p2 == "anelideo") & (p3 == "hematofago"): print("sanguessuga")
elif (p1 == 'inertebrado') & (p2 == "anelideo") & (p3 == "onivoro"): print("minhoca")
else: print("Palavra Incorreta")



