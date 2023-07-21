import random

def pokemon():
    pokemon = {
        "Nombre": "Zeus",
        "vida": random.randint(130, 190),
        "rayo": 20,
        "tormenta": 30,
        "rayo_critico": 40,
        "Criatura_de_saturno": 50,
        "Campo_electrico": 70,
        "fallo": 0,
        "rayo_curativo":0
        
    }
    pokemon["copias"]=pokemon[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo"])]
    
    pokemon["rayos"] = pokemon[random.choice(["rayo", "rayo_critico"])]
    pokemon["fallo_rayo"] = pokemon[random.choice(["rayos", "fallo"])]
    pokemon["fallo_tormenta"] = pokemon[random.choice(["tormenta", "fallo"])]
    pokemon["fallo_criatura"] = pokemon[random.choice(["Criatura_de_saturno", "fallo"])]
    pokemon["fallo_campo"] = pokemon[random.choice(["Campo_electrico", "fallo"])]
    print("Tu pokemon es el gran ZEUS ")
    print("La vida de tu pokemon es", pokemon["vida"], "\n")
    return pokemon

# Berserk
def berserk():
    berserk = {
        "Nombre": "berserk",
        "vidab": random.randint(120, 200),
        "ira": 25,
        "golpes": 35,
        "ola_golpeante": 50,
        "Furia_berserker": 60,
        "fallob": 0
    }
    berserk["danob"] = berserk[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker"])]
    return berserk

# Espadachin
def espadachin():
    espadachin = {
        "Nombre": "espadachin",
        "vidae": random.randint(120, 170),
        "slash": 20,
        "corte_vertical": 40,
        "triple_slash": 60,
        "desenvaine_rapido": 70,
        "doble_corte": 80,
        "falloe": 0
    }
    espadachin["danoe"] = espadachin[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte"])]
    return espadachin

# Mago

def mago():
    mago = {
        "Nombre": "mago",
        "vidam": random.randint(120, 180),
        "ataque_magico": 30,
        "bestia_magica": 50,
        "fallom": 0,
        "coraza_magica": 5,
        "ataque_de_fuego":60,
        "copia":None
    }
    mago["danom"] = mago[random.choice(["ataque_magico", "bestia_magica", "fallom","copia","ataque_de_fuego"])]
    return mago

# Invocador
def invocador():
    invocador = {
        "Nombre": "invocador",
        "vidai": random.randint(120, 190),
        "perro_infernal": 25,
        "ogro": 50,
        "falloi": 0
    }
    invocador["danoi"] = invocador[random.choice(["perro_infernal", "ogro", "falloi"])]
    return invocador

pokemon = pokemon()
no = ['berserk', 'espadachin', 'mago', 'invocador']
o = random.choice(no)
oponente = None
bool_value = True

# BERSERK
if o == "berserk":
    oponente = berserk()
    print("Oponente", oponente["Nombre"])
    print("La vida del oponente es", oponente["vidab"])
    while bool_value:
        print("\nPoderes\n1- Rayo (20 Daño)\n2- Tormenta (30 Daño)\n3- Trueno curativo (+25 vida)\n4- Criatura de saturno (50 Daño)\n5- Campo electrico (70 Daño)")
        x = int(input("> "))
        if x == 1:
            oponente["vidab"] -= pokemon["fallo_rayo"]
            if pokemon["fallo_rayo"] == pokemon["rayo_critico"]:
                print("¡Has hecho un crítico!")
            elif pokemon["fallo_rayo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidab"])
        elif x == 2:
            oponente["vidab"] -= pokemon["fallo_tormenta"]
            if pokemon["fallo_tormenta"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidab"])
        elif x == 3:
            pokemon["vida"] += 25
            print("+25 de vida")
        elif x == 4:
            if pokemon["fallo_criatura"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidab"] -= pokemon["Criatura_de_saturno"]
                print("Vida del oponente", oponente["vidab"])
        elif x == 5:
            if pokemon["fallo_campo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidab"]
                oponente["vidab"] -= pokemon["Campo_electrico"]
                print("Vida del oponente", oponente["vidab"])

        daño = oponente["danob"]
        if daño == 25:
            print("El oponente ha utilizado (ira) y te ha quitado 25 de vida")
            
        elif daño == 35:
            print("El oponente ha utilizado (golpes) y te ha quitado 35 de vida")
            
        elif daño == 0:
            print("El enemigo ha fallado")
        elif daño == 50:
            print("El oponente ha utilizado (ola golpeante) y te ha quitado 50 de vida")
            
        elif daño == 60:
            print("El oponente ha utilizado su Furia berserker y te ha quitado 60 de vida")

        pokemon["vida"] -= daño
        print("Tu vida es", pokemon["vida"])

        if pokemon["vida"] <= 0:
            print("Perdiste")
            bool_value = False
        elif oponente["vidab"] <= 0:
            print("Ganaste")
            bool_value = False

        oponente["danob"] = oponente[random.choice(["ira", "golpes", "fallob", "Furia_berserker", "ola_golpeante"])]
        pokemon["fallo_rayo"] = pokemon[random.choice(["rayos", "fallo"])]
        pokemon["fallo_tormenta"] = pokemon[random.choice(["tormenta", "fallo"])]
        pokemon["fallo_criatura"] = pokemon[random.choice(["Criatura_de_saturno", "fallo"])]
        pokemon["fallo_campo"] = pokemon[random.choice(["Campo_electrico", "fallo"])]

# Espadachin
elif o == "espadachin":
    oponente = espadachin()
    print("Oponente", oponente["Nombre"])
    print("La vida del oponente es", oponente["vidae"])
    while bool_value:
        print("\nPoderes\n1- Rayo (20 Daño)\n2- Tormenta (30 Daño)\n3- Trueno curativo (+25 vida)\n4- Criatura de saturno (50 Daño)\n5- Campo electrico (70 Daño)")
        x = int(input("> "))
        if x == 1:
            oponente["vidae"] -= pokemon["fallo_rayo"]
            if pokemon["fallo_rayo"] == pokemon["rayo_critico"]:
                print("¡Has hecho un crítico!")
            elif pokemon["fallo_rayo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidae"])
        elif x == 2:
            oponente["vidae"] -= pokemon["fallo_tormenta"]
            if pokemon["fallo_tormenta"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidae"])
        elif x == 3:
            pokemon["vida"] += 25
            print("+25 de vida")
        elif x == 4:
            if pokemon["fallo_criatura"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidae"] -= pokemon["Criatura_de_saturno"]
                print("Vida del oponente", oponente["vidae"])
        elif x == 5:
            if pokemon["fallo_campo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidae"] -= pokemon["Campo_electrico"]
                print("Vida del oponente", oponente["vidae"])

        daño = oponente["danoe"]
        if daño == 20:
            print("El oponente ha utilizado (slash) y te ha quitado 20 de vida")
        elif daño == 40:
            print("El oponente ha utilizado (corte vertical) y te ha quitado 40 de vida")
        elif daño == 0:
            print("El enemigo ha fallado")
        elif daño == 60:
            print("El oponente ha utilizado (triple slash) y te ha quitado 60 de vida")
        elif daño == 70:
            print("El oponente ha utilizado (desenvaine rápido) y te ha quitado 70 de vida")
        elif daño == 80:
            print("El oponente ha utilizado (doble corte) y te ha quitado 80 de vida")
        pokemon["vida"] -= daño
        print("Tu vida es", pokemon["vida"])

        if pokemon["vida"] <= 0:
            print("Perdiste")
            bool_value = False
        elif oponente["vidae"] <= 0:
            print("Ganaste")
            bool_value = False

        oponente["danoe"] = oponente[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte"])]
        pokemon["fallo_rayo"] = pokemon[random.choice(["rayos", "fallo"])]
        pokemon["fallo_tormenta"] = pokemon[random.choice(["tormenta", "fallo"])]
        pokemon["fallo_criatura"] = pokemon[random.choice(["Criatura_de_saturno", "fallo"])]
        pokemon["fallo_campo"] = pokemon[random.choice(["Campo_electrico", "fallo"])]


# Mago

elif o == "mago":
    oponente = mago()
    
    print("Oponente", oponente["Nombre"])
    print("La vida del oponente es", oponente["vidam"])
    while bool_value:
        print("\nPoderes\n1- Rayo(20 Daño)\n2- Tormenta(30 Daño)\n3- Trueno curativo(+25 vida)\n4- Criatura de saturno(50 Daño)\n5- Campo electrico(70 daño)")
        x = int(input("> "))
        copia = pokemon["copias"]
        daño = oponente["danom"]
        if x == 1:
            oponente["vidam"] -= pokemon["fallo_rayo"]
            if pokemon["fallo_rayo"] == pokemon["rayo_critico"]:
                print("¡Has hecho un crítico!")
            elif pokemon["fallo_rayo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidam"])
        elif x == 2:
            oponente["vidam"] -= pokemon["fallo_tormenta"]
            if pokemon["fallo_tormenta"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidam"])
        elif x == 3:
            pokemon["vida"] += 25000000
            print("+25 de vida")
        
        elif x == 4:
            if pokemon["fallo_criatura"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidam"] -= pokemon["Criatura_de_saturno"]
                print("Vida del oponente", oponente["vidam"])
        elif x == 5:
            if pokemon["fallo_campo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidam"] -= pokemon["Campo_electrico"]
            print("Vida del oponente", oponente["vidam"])
           
        oponente["vidam"] += oponente["coraza_magica"]
        print("Mago se ha puesto una coraza mágica (+5 vida)")

        if daño == 30:
            print("El oponente ha utilizado (ataque mágico) y te ha quitado 30 de vida")
            
        elif daño == 50:
            print("El oponente ha utilizado (bestia mágica) y te ha quitado 50 de vida")
        elif daño == 0:
            print("El enemigo ha fallado")
        elif daño == 60 :
            print("El oponente a utilizado (ataque magico) y te a quitado 60 de vida") 
        elif daño == oponente["copia"]:
            daño = copia     
            print("El oponente a copiado un poder tuyo")
            
            if daño == pokemon["rayo_curativo"] :
                print("Trueno curativo")
                oponente["vidam"] += 25
            elif daño == pokemon["rayo"]:
                print("Rayo")
            elif daño == pokemon["tormenta"]:
                print("Tormenta")
            elif daño == pokemon["Criatura_de_saturno"]:
                print("Criatura de saturno")
            elif daño == pokemon["Campo_electrico"]:
                print("Campo electrico")
                                    
        pokemon["vida"] -= daño
        
        print("Tu vida es", pokemon["vida"])
        if pokemon["vida"] <= 0:
            print("Perdiste")
            bool_value = False
        elif oponente["vidam"] <= 0:
            print("Ganaste")
            bool_value = False
            
            
            
        pokemon["copias"]=pokemon[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo"])]
        oponente["danom"] = oponente[random.choice(["ataque_magico", "bestia_magica", "fallom","copia","ataque_de_fuego"])]
        pokemon["fallo_rayo"] = pokemon[random.choice(["rayos", "fallo"])]
        pokemon["fallo_tormenta"] = pokemon[random.choice(["tormenta", "fallo"])]
        pokemon["fallo_criatura"] = pokemon[random.choice(["Criatura_de_saturno", "fallo"])]
        pokemon["fallo_campo"] = pokemon[random.choice(["Campo_electrico", "fallo"])]

# Invocador
elif o == "invocador":
    oponente = invocador()
    print("Oponente", oponente["Nombre"])
    print("La vida del oponente es", oponente["vidai"])
    while bool_value:
        print("\nPoderes\n1- Rayo(20 Daño)\n2- Tormenta(30 Daño)\n3- Trueno curativo(+25 vida)\n4- Criatura de saturno(50 Daño)\n5- Campo electrico(70)")
        x = int(input("> "))
        if x == 1:
            oponente["vidai"] -= pokemon["fallo_rayo"]
            if pokemon["fallo_rayo"] == pokemon["rayo_critico"]:
                print("¡Has hecho un crítico!")
            elif pokemon["fallo_rayo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidai"])
        elif x == 2:
            oponente["vidai"] -= pokemon["fallo_tormenta"]
            if pokemon["fallo_tormenta"] == pokemon["fallo"]:
                print("¡Fallaste!")
            print("Vida del oponente", oponente["vidai"])
        elif x == 3:
            pokemon["vida"] += 25
            print("+25 de vida")
        elif x == 4:
            if pokemon["fallo_criatura"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidai"] -= pokemon["Criatura_de_saturno"]
                print("Vida del oponente", oponente["vidai"])
        elif x == 5:
            if pokemon["fallo_campo"] == pokemon["fallo"]:
                print("¡Fallaste!")
            else:
                oponente["vidai"] -= pokemon["Campo_electrico"]
                print("Vida del oponente", oponente["vidai"])

        daño = oponente["danoi"]
        if daño == 25:
            print("El oponente ha invocado (perro infernal) y te ha quitado 25 de vida")
        elif daño == 50:
            print("El oponente ha invocado (ogro) y te ha quitado 50 de vida")
        elif daño == 0:
            print("El enemigo ha fallado")

        pokemon["vida"] -= daño
        print("Tu vida es", pokemon["vida"])

        if pokemon["vida"] <= 0:
            print("Perdiste")
            bool_value = False
        elif oponente["vidai"] <= 0:
            print("Ganaste")
            bool_value = False

        oponente["danoi"] = oponente[random.choice(["perro_infernal", "ogro", "falloi"])]
        pokemon["fallo_rayo"] = pokemon[random.choice(["rayos", "fallo"])]
        pokemon["fallo_tormenta"] = pokemon[random.choice(["tormenta", "fallo"])]
        pokemon["fallo_criatura"] = pokemon[random.choice(["Criatura_de_saturno", "fallo"])]
        pokemon["fallo_campo"] = pokemon[random.choice(["Campo_electrico", "fallo"])]

print()
print("Batalla terminada")