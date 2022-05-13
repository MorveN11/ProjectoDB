from src.Utils import Utility

names1l = "Mauricio,Jesús,Jaime,Aarón,Rubén,Ian,Guillermo,Erik,Mohamed,Julen,Luis,Pau,Unai,Rafael,Joel,Alberto,Pedro,Raúl,Aitor,Santiago,Rayan,Pol,Nil,Noah,Jan,Asier,Fernando,Alonso,Matías,Biel,Andrés,Axel,Ismael,Martí,Arnau,Imran,Luka,Ignacio,Aleix,Alan,Elías,Omar,Isaac,Youssef,Jon,Teo,Mauro,Óscar,Cristian,Leonardo"
names2l =  "Martín,Lucas,Mateo,Leo,Daniel,Alejandro,Pablo,Adrián,David,Diego,Marcos,Izan,Javier,Álex,Bruno,Oliver,Miguel,Thiago,Marc,Carlos,Ángel,Juan,Gonzalo,Sergio,Nicolás,Dylan,Gabriel,Jorge,José,Adam,Liam,Eric,Samuel,Darío,Héctor,Luca,Iker,Amir,Rodrigo,Saúl,Víctor,Francisco,Iván"
names1 = Utility.joinNames(names1l)
names2 = Utility.joinNames(names2l)
names2 = Utility.appendNones(names2)
lastNames1 = [
"Torrico", "Trujillo", "Oropeza",
"Terán", "Davila", "Rojas",
"Baldelomar", "Gutierrez", "Zapata",
"Lopez", "Cortes", "Cortez",
"Flores", "Berdeja", "Moya",
"Rocha", "Condori", "Mejia",
"Arce", "Paredes", "Suarez",
"Oporto", "Villegas", "Vallejos",
"Cabezas", "Guzman", "Roman",
"Aramayo", "Gonzales", "Coca",
"Loza", "Mariscal", "Fuentes",
"Rosales", "Maldonado", "Ormeño",
"Hurtado", "Ayma", "Soliz",
"Almaraz", "Garcia", "Agramont",
"Torrez", "Soto", "Viscarra",
"Choque", "Ortiz", "Murillo",
"Añez", "Carballo"]
lastNames2 = [
"Fernandez", "Rodriguez", "Garcia",
"Perez", "Gomez", "Martinez",
"Sanchez", "Hernandez","Carvajal",
"Acero", "Villa", "Cruz",
"Rocha", "Ruiz", "Lopez",
"Torrez", "Guzman", "Muñoz",
"Vega", "Daza", "Revollo",
"Toledo", "Camara", "Mallo",
"España", "Siles", "Maldonado",
"Ugarte", "Cuellar", "Villanueva"]
lastNames2 = Utility.appendNones(lastNames2)


def __init__(self):
    self.names1 = names1
    self.names2 = names2
    self.lastName1 = lastNames1
    self.lastName2 = lastNames2
