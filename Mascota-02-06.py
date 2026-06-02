print("***************************************************")
print("*         CUESTIONARIO DE TU MASCOTA              *")
print("***************************************************")
print("")
nomb = input("Ingresa tu nombre -> ")
print("Hola! ", nomb, "Iniciemos con un cuestionario sobre tu mascota!!")
print("")
nom_masc = input("¿Como se llama tu mascota?-> ")
print("")
print(" >Guau, ", nom_masc," es muy buen nombre c:")
print("") 
tipo = input("¿Que tipo de animal es? (perro - gato - otro) -> ").lower()
if tipo == "perro":
    print(" >Los perros son muy fieles y excelentes compañeros.")
elif tipo == "gato":
    print(" >Los gatos son animales muy independientes y limpios.")
else:
    print(" >Que mascota tan original tienes .")
print("")
edad = int(input("¿Cuantos Años tiene tu mascota? :o-> "))
if edad <= 2:
    print(" >Tu mascota es un bebe :D")
elif edad >= 10:
    print(" >Tu viejito es todo un viejito :D")
else:   
    print(" >Es tooodo un adulto, wuaaau :o ")
print("")
obt = input("¿lo adoptaste/recogiste o lo compraste? (lo adopte - lo recogi - otro ) -> ").lower()
if obt == "lo adopte":
    print(" >Que interesante :o.")
elif obt == "lo recogi":
    print(" >Guauu, eso es muy bueno, ayudando a los mas necesitados :D")
else:
    print(" >Bueno, debes tener tus motivos, recuerda adoptar, ellos te necesitan :D")
print("")
jugar = input("¿Le gusta jugar con juguetes? (si - no) -> ").lower()
if jugar == "si":
    print(" >Que alegre, se nota que tiene mucha energia para divertirse c:.")
else:
    print(" >Entiendo, seguro prefiere pasar el tiempo descansando o durmiendo. zZZ")
print("")
comida = input("Por ultimo... ¿ya comio el dia de hoy? (si - no) -> ").lower()
if comida == "si":
    print(" >Excelente, entonces ya tiene la pancita llena y esta feliz :D.")
else:
    print(" >Recuerda darle de comer pronto para que no pase hambre c:.")
print("")
print("***************************************************")
print("*       ¡GRACIAS POR COMPLETAR EL CUESTIONARIO!   *")
print("***************************************************")
