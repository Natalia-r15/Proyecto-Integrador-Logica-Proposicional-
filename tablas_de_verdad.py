correcto2 = True
valor = input("Ingresa T para la respuesta en texto o V para valores de verdad: ")

while correcto2:
    if valor == "T" or valor == "t":
        p=input("p: ")
        q=input("q: ")
        conector_logico=(input("Ingresa el nombre de conector lógico que deseas (conjuncion, disyuncion, negacion, "
                               "condicional, bicondicional o XOR: "))
        correcto = True
        while correcto:
            if conector_logico == "conjuncion" or conector_logico == "Conjuncion":
                print("p ∧ q: " + str(p) + " y " + str(q)+ ".")
                correcto = False
            elif conector_logico == "disyuncion" or conector_logico == "Disyuncion":
                print("p ∨ q: " + str(p) + " o " + str(q) + ".")
                correcto = False
            elif conector_logico == "condicional" or conector_logico == "Condicional":
                print("p → q: si " + str(p) + " entonces " + str(q) + ".")
                correcto = False
            elif conector_logico == "bicondicional" or conector_logico == "Bicondicional":
                print("p ↔ q: " + str(p) + " si y sólo si " + str(q)+ ".")
                correcto = False
            elif conector_logico == "XOR" or conector_logico == "xor":
                print("p ⊕ q: " + str(p) + " o " + str(q) +", pero no ambos al mismo tiempo.")
                correcto = False
            elif conector_logico == "negacion" or conector_logico == "Negacion":
                correcto = False
                variable = input("Ingrese la variable que desea negar (p o q): ")
                if variable == "p" or variable == "P":
                    print("¬p: no " + str(p))
                elif variable == "q" or variable == "Q":
                    print("¬q: no " + str(q))
            else:
                print("La palabra no es válida, intente de nuevo.")
                conector_logico=(input("Ingresa el nombre de conector lógico que deseas: "))

        correcto2 = False

    elif valor == "V" or valor == "v":
        p = input("p (V para verdad y F para falso): ")
        c = True
        while c:
            if p == "F" or p == "f" or p == "v" or p == "V":
                c = False
            else:
                print("El valor no es válido, intente de nuevo.")
                p = input("p (V para verdad y F para falso): ")

        q = input("q (V para verdad y F para falso): ")
        while q not in ["f", "v", "F", "V"]:
            print("El valor no es válido, intente de nuevo.")
            q = input("q (V para verdad y F para falso): ")

        conector_logico = (input("Ingresa el nombre de conector lógico que deseas (conjuncion, disyuncion, negacion, "
                                 "condicional, bicondicional o XOR: "))
        correcto3 = True
        while correcto3:
            if conector_logico == "conjuncion" or conector_logico == "Conjuncion":
                correcto3 = False
                if p == "v" or p == "V":
                    if q == "v" or q == "V":
                        print("p ∧ q: V")
                    else:
                        print("p ∧ q: F")
                else:
                    if q == "v" or q == "V":
                        print("p ∧ q: F")
                    else:
                        print("p ∧ q: F")
            elif conector_logico == "negacion" or conector_logico == "Negacion":
                correcto3 = False
                variable2 = input("Ingrese la variable que desea negar (p o q): ")
                if variable2 == "p" or variable2 == "P":
                    if p == "v" or p == "V":
                        print("¬p: F")
                    elif p == "f" or p == "F":
                        print("¬p: V")
                elif variable2 == "q" or variable2 == "Q":
                    if q == "v" or q == "V":
                        print("¬q: F")
                    elif q == "f" or q == "F":
                        print("¬q: V")
            elif conector_logico == "disyuncion" or conector_logico == "Disyuncion":
                correcto3 = False
                if p == "v" or p == "V":
                    if q == "v" or q == "V":
                        print("p ∨ q: V")
                    else:
                        print("p ∨ q: V")
                else:
                    if q == "v" or q == "V":
                        print("p ∨ q: V")
                    else:
                        print("p ∨ q: F")
            elif conector_logico == "condicional" or conector_logico == "Condicional":
                correcto3 = False
                if p == "v" or p == "V":
                    if q == "v" or q == "V":
                        print("p → q: V")
                    else:
                        print("p → q: F")
                else:
                    if q == "v" or q == "V":
                        print("p → q: V")
                    else:
                        print("p → q: V")
            elif conector_logico == "bicondicional" or conector_logico == "Bicondicional":
                correcto3 = False
                if p == "v" or p == "V":
                    if q == "v" or q == "V":
                        print("p ↔ q: V")
                    else:
                        print("p ↔ q: F")
                else:
                    if q == "v" or q == "V":
                        print("p ↔ q: F")
                    else:
                        print("p ↔ q: V")
            elif conector_logico == "XOR" or conector_logico == "xor":
                correcto3 = False
                if p == "v" or p == "V":
                    if q == "v" or q == "V":
                        print("p ⊕ q: F")
                    else:
                        print("p ⊕ q: V")
                else:
                    if q == "v" or q == "V":
                        print("p ⊕ q: V")
                    else:
                        print("p ⊕ q: F")
            else:
                print("La palabra no es válida, intente de nuevo.")
                conector_logico = (input("Ingresa el nombre de conector lógico que deseas: "))
        break

    else:
        print("La letra no es válida, intente de nuevo.")
        valor = input("Ingresa T para la respuesta en texto o V para valores de verdad: ")