correcto2 = True
valor = input("Ingresa T para la respuesta en texto o V para valores de verdad: ")

while correcto2:
    if valor == "T" or valor == "t":
        q=input("p: ")
        p=input("q: ")
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
            elif conector_logico == "XOR":
                print("p ⊕ q: " + str(p) + " o " + str(q) +", pero no ambos al mismo tiempo.")
                correcto = False
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