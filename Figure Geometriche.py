print("Calcola il Perimetro")
forma = int(input ("Premi 1 per quadrato, 2 per rettangolo, 3 per cerchio: "))

if forma == 1 :
# Perimetro del quadrato
 lato = float (input ("Inserisci lato: "))
 print(f"Il perimetro del quadrato è: {lato*4}")

elif forma == 2 :
# Perimetro del rettangolo
 base = float (input ("Inserisci base: "))
 altezza = float (input ("Inserisci altezza: "))
 print(f" Il perimetro del rettangolo è: {base*2 + altezza*2} ")

elif forma == 3 :
# Perimetro Cerchio
 raggio = float (input("Inserisci il raggio: "))
 print(f" la circonferenza del cerchio è: {2*3.14*raggio}")

else: 
 print("Non hai selezionato i numeri della lista. questo terminale si autodistruggerà fra 3..2..1..Skatush!XD")


