#proyecto guadalahacks
##Autores: Itahí Vallejo, Diana Aparicio, Gilberto López y Braulio Barba.
##Fecha de creación: 18 de mayo de 2024

#Este código fue originalmente realizado en Google Colab para poder conectar con mayor facilidad a Google sheets y crear las hojas de datos que se crearían.

#importar y leer base de datos
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

#volun = pd.DataFrame(columns=["Nombre","Apellido", "Contacto", "Edad","Nivel educativo","Área de interés",
#"Modalidad","Disponibilidad","Estado"])
volun=pd.read_excel("/content/drive/MyDrive/VolunNet/Basevoluntarios.xlsx","bvoluntario" )

#org = pd.DataFrame(columns=["Organización","Contacto", "Edad","Nivel educativo","Área de interés","Modalidad","Estado"])
org=pd.read_excel("/content/drive/MyDrive/VolunNet/Baseorganizacion.xlsx","breclutador" )

#Función para ingresar datos en la base de datos de voluntarios
estados_mexico = ['estado de mexico', 'jalisco', 'michoacan', 'baja california', 'yucatan', 'chiapas',
                  'guerrero', 'sonora', 'nuevo leon', 'sinaloa', 'ciudad de mexico', 'hidalgo', 'tamaulipas',
                  'nayarit', 'quintana roo', 'tlaxcala', 'coahuila', 'tabasco', 'morelos', 'guanajuato', 'veracruz',
                  'puebla', 'san luis potosi', 'baja california sur', 'durango', 'zacatecas', 'aguascalientes', 'colima', 'campeche']

#Función para guardar el registro de los voluntarios
def info_vol():
    print("Nos complace saber que te interesa algún programa de voluntariado, a continuación te pedimos responer una serie de preguntas para crearte un perfil")
    name_vol = input("Pon tu nombre(s): ")
    name_vol = name_vol.lower()
    lastname_vol = input("Pon tu(s) apellido(s): ")
    mail_vol = input("Proporciónanos un correo electrónico de contacto: ")
    edad_vol = int(input("¿En qué rango de edad te encuentras? \n 1. 18-29 \n 2. 30-45 \n 3. 46-60 \n 4. 60+ \n "))
    educa_vol = int(input("¿Cuál es tu nivel educativo actual? \n 1. Basico (primaria) \n 2. Medio (secundaria-preparatoria) \n 3. Superior (preparatoria técnica-licenciatura-posgrado) \n "))

    interes_vol = int(input("Elige el área en la que deseas ser voluntario \n 1. Ciencias de la salud \n 2. Ciencias sociales \n 3. Ingenierías y ciencias naturales \n 4. Negocios y emprendimiento \n 5. Estudios creativos \n Si te interesa más de una, presiona 6 \n "))
    while 0>interes_vol or interes_vol >7:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            interes_vol  = int(input("Elige el área en la que deseas ser voluntario \n 1. Ciencias de la salud \n 2. Ciencias sociales \n 3. Ingenierías y ciencias naturales \n 4. Negocios y emprendimiento \n 5. Estudios creativos \n Si te interesa más de una, presiona 6 \n "))

    if interes_vol  == 6:
        interes_vol_nvo = [0,0,0,0,0]
        interes_vol_nvo [0] = int(input("¿Te interesan las ciencias de la salud? \n 1. Si \n 0. No \n "))

        while interes_vol_nvo [0] != 0 and interes_vol_nvo [0]!=1:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            interes_vol  = int(input("¿Te interesan las ciencias de la salud? \n 1. Si \n 0. No \n "))
        interes_vol_nvo [1] = int(input("¿Te interesan las ciencias socales? \n 2. Si \n 0. No \n "))

        while interes_vol_nvo [1]!=0 and interes_vol_nvo [1]!=2:
            print("Ups, esa opción no está disponible. n\ Inténtalo otra vez por favor")
            interes_vol = int(input("¿Te interesan las ciencias socales? \n 2. Si \n 0. No n\ "))
        interes_vol [2] = int(input("¿Te interesa el área de ingeniería y ciencias naturales? n\ 3. Si \n 0. No \n "))

        while interes_vol_nvo [2]!=0 and interes_vol_nvo [2]!=3:
            print("Ups, esa opción no está disponible. n\ Inténtalo otra vez por favor")
            interes_vol = int(input("¿Te interesa el área de ingeniería y ciencias naturales? \n 3. Si \n 0. No \n "))
        interes_vol [3] = int(input("¿Te interesan los negocios y emprendimiento? \n 4. Si \n 0. No \n "))

        while interes_vol_nvo [3]!=0 and interes_vol_nvo [3]!=4:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            interes_vol = int(input("¿Te interesan los negocios y emprendimiento? \n 4. Si \n 0. No \n "))

        while interes_vol_nvo [4]!=0 and interes_vol_nvo [4]!=3:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            interes_vol = int(input("¿Te interesan los estudios creativos como las artes? \n 3. Si \n 0. No \n "))
        interes_vol = interes_vol_nvo

    mod_vol = int(input("¿En qué modalidad puedes ser parte del voluntariado? \n 1. Presencial \n 2. Virtual \n 3. Híbrido"))
    disp_vol = int(input("Selecciona la cantidad de horas que puedes aportar semanalmente: \n 1. 2-6 hrs \n 2. 6-10 hrs \n 10+ hrs \n  "))
    estado_vol = str(input("¿En qué estado de la república buscas ser voluntaio? Escribe el estado sin acentos: "))
    if estado_vol.lower() in estados_mexico:
        estado_vol = estado_vol
    else:
        print("Tu respuesta no se encotró en la base de los estado, te pedimos reescribir el nombre completo del estado sin acentos")
        estado_vol = str(input("¿En qué estado de la república buscas ser voluntaio?: "))


    vol_registro = {"Nombre": name_vol,"Apellido": lastname_vol, "Correo": mail_vol, "Edad": edad_vol,"Nivel educativo": educa_vol,
                    "Área de interés": interes_vol, "Modalidad":mod_vol,"Disponibilidad": disp_vol,"Estado": estado_vol}
    return vol_registro

#Función para guardar el registro de las organizaciones
def info_org():
    print("Perfecto, empecemos con preguntas básicas acerca de su organización")
    name_org = str(input("¿Cuál es el nombre de la organización? "))
    correo_org = str(input("Proporciónanos un correo para contactarles: "))
    nacional = int(input("¿Ofrece voluntariado a nivel nacional? \n 1. Si \n 0. No \n"))
    while nacional != 0 and nacional != 1:
        print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
        nacional = int(input("¿Ofrecen voluntariado a nivel nacional? \n 1. Si \n 0. No \n"))
    if nacional == 1:
        estado_org = estados_mexico
    else:
        estado_org = str(input("¿En qué estado ofrecen el voluntariado? (favor de solo poner uno, si ofrece más de 1 haga el proceso de nuevo)"))
        e = 0
        while e == 0:
            if estado_org.lower() in estados_mexico:
                e = 1
            else:
                print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
                estado_org = str(input("¿En qué estado ofrecen el voluntariado? "))
    rango_edad_org = int(input("¿Qué rango de edad les interesa en los voluntarios? \n 1. 18 - 29 \n 2. 30 - 45 \n 3. 46 - 60 \n 4. 60 + \n 5. Más de uno de estos grupos\n 6. No tienen preferencia"))
    while 0>=rango_edad_org or rango_edad_org>6:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            rango_edad_org = int(input("¿Qué rango de edad les interesa en los voluntarios? \n 1. 18-29 \n 2. 30-45 \n 3. 46-60 \n 4. 60 + \n 5. Más de uno de estos grupos \n 6. No tienen preferencia \n"))
    if rango_edad_org == 5:
        rango_edad_nuevo = [0,0,0,0]
        rango_edad_nuevo[0] = int(input("¿Te interesa el grupo entre 18 y 29 años? \n 1. Si n\ 0. No"))
        while rango_edad_nuevo[0] != 0 and rango_edad_nuevo[0]!=1:
            print("Ups, esa opción no está disponible. n\ Inténtalo otra vez por favor")
            rango_edad_org = int(input("¿Te interesa el grupo entre 18 y 29 años? \n 1. Si n\ 0. No"))
        rango_edad_nuevo[1] = int(input("¿Te interesa el grupo entre 30 y 45 años? n\ 2. Si n\ 0. No"))
        while rango_edad_nuevo[1]!=0 and rango_edad_nuevo[1]!=2:
            print("Ups, esa opción no está disponible. n\ Inténtalo otra vez por favor")
            rango_edad_org = int(input("¿Te interesa el grupo entre 30 y 45 años? n\ 2. Si n\ 0. No"))
        rango_edad_nuevo[2] = int(input("¿Te interesa el grupo entre 46 y 60 años? n\ 3. Si n\ 0. No"))
        while rango_edad_nuevo[2]!=0 and rango_edad_nuevo[2]!=3:
            print("Ups, esa opción no está disponible. n\ Inténtalo otra vez por favor")
            rango_edad_org = int(input("¿Te interesa el grupo entre 45 y 60 años? n\ 3. Si n\ 0. No"))
        rango_edad_nuevo[3] = int(input("¿Te interesa el grupo de 60 años en adelante? n\ 4. Si n\ 0. No"))
        while rango_edad_nuevo[3]!=0 and rango_edad_nuevo[3]!=4:
            print("Ups, esa opción no está disponible. n\ Inténtalo otra vez por favor")
            rango_edad_org = int(input("¿Te interesa el grupo de 60 años en adelante? n\ 4. Si n\ 0. No"))
        rango_edad_org = rango_edad_nuevo

    nivel_educativo_org = int(input("¿Cuál es el nivel educativo mínimo que necesitan/les interesa? \n 1. Basico (primaria) \n 2. Medio (secundaria-preparatoria) \n 3. Superior (preparatoria técnica-licenciatura-posgrado) \n "))
    while nivel_educativo_org <= 0 or nivel_educativo_org >= 4:
        print("Ups, esa opción no está disponible. n\ Inténtalo otra vez por favor")
        nivel_educativo_org = int(input("¿Cuál es el nivel educativo mínimo que necesitan/les interesa? \n 1. Basico (primaria) \n 2. Medio (secundaria-preparatoria) \n Superior (preparatoria técnica-licenciatura-posgrado) \n "))
    print("¿Qué modalidad(es) ofrecerán a los voluntarios: ")
    pres_org = int(input("Presencial: \n 1. Si \n 0. No \n"))
    hib_org = int(input("Híbrido: \n 1. Si \n 0. No \n"))
    virt_org = int(input("Virtual: \n 1. Si \n 0. No \n"))
    area_org = int(input("¿Qué áreas de interés presentan para los voluntarios? \n 1. Ciencias de la salud \n 2. Ciencias sociales \n 3. Ingeniería y ciencias naturales \n 4. Negocios y emprendimiento \n 5. Estudios creativos \n 6. Más de una opción"))

    while 0>=area_org or area_org>6:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            area_org = int(input("¿Qué áreas de interés presentan para los voluntarios? \n 1. Ciencias de la salud \n 2. Ciencias sociales \n 3. Ingeniería y ciencias naturales \n 4. Negocios y emprendimiento \n 5. Estudios creativos \n 6. Más de una opción \n"))
    if area_org == 6:
        area_nuevo = [0,0,0,0,0]
        area_nuevo[0] = int(input("¿Ofreces el área de ciencias de la salud? \n 1. Si \n 0. No"))
        while area_nuevo[0] != 0 and area_nuevo[0]!=1:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            area_org = int(input("¿Ofreces el área de ciencias de la salud? \n 1. Si \n 0. No"))
        area_nuevo[1] = int(input("¿Ofreces el área de ciencias sociales? \n 2. Si \n 0. No"))
        while area_nuevo[1]!=0 and area_nuevo[1]!=2:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            area_org = int(input("¿Ofreces el área de ciencias sociales? \n 2. Si \n 0. No"))
        area_nuevo[2] = int(input("¿Ofreces el área de ingeniería y ciencias naturales? \n 3. Si \n 0. No"))
        while area_nuevo[2]!=0 and area_nuevo[2]!=3:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            area_org = int(input("¿Ofreces el área de ingeniería y ciencias naturales? \n 3. Si \n 0. No"))
        area_nuevo[3] = int(input("¿Ofreces el área de negocios y emprendimiento? \n 4. Si \n 0. No"))
        while area_nuevo[3]!=0 and area_nuevo[3]!=4:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            area_org = int(input("¿Ofreces el área de negocios y emprendimiento? \n 4. Si \n 0. No"))
        area_nuevo[4] = int(input("¿Ofreces el área de estudios creativos? \n 5. Si \n 0. No"))
        while area_nuevo[4]!=0 and area_nuevo[4]!=5:
            print("Ups, esa opción no está disponible. \n Inténtalo otra vez por favor")
            area_org = int(input("¿Ofreces el área de estudios creativos? \n 5. Si \n 0. No"))
        area_org = area_nuevo
    modalidades_org = [pres_org, hib_org, virt_org]

    org_registro = {"Organización":name_org,"Contacto":correo_org, "Edad":rango_edad_org,"Nivel educativo" :nivel_educativo_org,
                    "Área de interés":area_org,"Modalidad": modalidades_org,"Estado":estado_org}
    return org_registro


#A través de esta función se obtiene el tipo de registro que desee ingresar el usuario y se divide por tipos para mandar a llamar alguna de las dos dunciones anteriores y que guarde la indicada.
def main():
    print("Bienvenido a VolunNet")
    rol = 0
    while rol == 0:
        rol = int(input("¿Te gustaría darte de alta como voluntario o como organización? \n 1. Voluntario \n 2. Organización"))
        if rol == 1:
            vol_registro = info_vol()
            return vol_registro,"v"
        elif rol == 2:
            org_registro = info_org()
            return org_registro,"o"
        else:
            print("Esa no es una opción válida, porfavor vuelve a intentarlo")
            return None,"e"
    print("¡Gracias por tu registro! Te contactaremos pronto con más información")

#Definición de los diferentes tipos de registro
registro,tipo=main()
if tipo=="v":
  voluntario=registro
elif tipo == "o":
  organizacion =registro
else:
   None

vnew_row=pd.Series(voluntario)
volun = pd.concat([volun, vnew_row.to_frame().T])

onew_row=pd.Series(organizacion)
org = pd.concat([org, onew_row.to_frame().T])

volun.head()
org.head()

# Conversión de los DataFrames a Datasheets en Google Sheets usando Google Drive
volun.to_excel("/content/drive/MyDrive/VolunNet/Basevoluntarios.xlsx","bvoluntario" )
org.to_excel("/content/drive/MyDrive/VolunNet/Baseorganizacion.xlsx","breclutador" )

#Se crean dos nuevos DataFrames únicamente tomando los datos que se quieren comparar para hacer el match entre empresa y voluntario
new_volun=volun.loc[:,["Nombre","Contacto","Edad","Nivel educativo","Área de interés","Modalidad","Estado"]]
new_org=org.loc[:,["Organización","Contacto","Edad","Nivel educativo","Área de interés","Modalidad","Estados"]]

#Parte que revisa que existan coincidencias en los 3 parámetros prioritarios: Estado, Area de interes y Edad
coincidencias = []
for i in range(len(new_volun)):
    for j in range(len(new_org)):
        if (new_volun.iloc[i, 6] == new_org.iloc[j, 6] and
            new_volun.iloc[i, 4] == new_org.iloc[j, 4] and
            new_volun.iloc[i, 2] == new_org.iloc[j, 2]):
            coincidencias.append([new_volun.iloc[i, 0], new_org.iloc[j, 0], new_org.iloc[j, 1]])

##Funcion de recomendacion con respecto al nombre
#Se imprime el nombre de la empresa y contacto con la que el usuario hizo "match"
nombre_vol = input("¿Cuál es tu nombre?: ")
nombre_vol = nombre_vol.lower()
cont = 0
print(nombre_vol.upper() + ", parece ser que coincides con: \n")
for i in range (len(coincidencias)):
    if nombre_vol == coincidencias[i][0]:
        cont+=1
        print(coincidencias[i][1])
        print("Contacto: "+ coincidencias[i][2])

if cont == 0:
  print("Por el momento no se han registrado organizaciones que tengan los requisitos que agregaste, revisa dentro de unos días nuevamente por favor.")