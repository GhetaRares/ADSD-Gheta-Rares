articol = "Realizatorul Mihai Gâdea a prezentat luni seară, la Sinteza Zilei, un sondaj despre care a spus că a fost realizat la comanda USR, și arată că în turul 2 al alegerilor prezidențiale ar urma să se confrunte Marcel Ciolacu și George Simion."
lungime = len(articol)
prima_parte = articol[:lungime // 2]
a_doua_parte = articol[lungime // 2:]
prima_parte = prima_parte.strip().upper()
a_doua_parte = a_doua_parte[ ::-1]
a_doua_parte = a_doua_parte.capitalize()
punctuatie = ['.' , ',' , '!' , '?']
for caracter in punctuatie: a_doua_parte = a_doua_parte.replace(caracter,' ')
rezultat_final = prima_parte + ' ' + a_doua_parte
print(rezultat_final)