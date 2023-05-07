import re
from io import BytesIO
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from funciones.PrintColores import*

Prueba1 = 'Lugar y Fecha: Guatemala, 01/04/2023 09:31 Usuario: map001 Red social: ChapinChat Hola amigos, nos vemos hoy en el gym… recuerden que después vamos a entrenar para la carrera 2K del próximo sábado. No olvieden su Ropa Deportiva y sus bebidas Hidratantes. Recuerden que hoy por la noche juega la selección de fútbol, nos vemos en Taco Bell a las 7 pm. '



ejemploPalabras = ["fútbol", "balonmano", "baloncesto", "balompié", "football", "basketball", "handball", "estadio", "selección", "champions league", "liga de campeones", "tenis", "natación", "olimpiada", "gym", "gimnasio"]
ejemploMensaje = 'Hola amigos, nos vemos hoy en el gym… recuerden que después vamos a entrenar para la carrera 2K del próximo sábado. No olvieden su Ropa Deportiva y sus bebidas Hidratantes. Recuerden que hoy por la noche juega la selección de fútbol, nos vemos en Taco Bell a las 7 pm. '




def leerXmlPerfiles(xml): 
    listaPerfiles = xml.getElementsByTagName('perfiles')
    listaDescartadas = xml.getElementsByTagName('descartadas')

    listaPerfilesActuales = []

    respuesta = '<?xml version="1.0"?>\n'
    
    textoPerfiles = ''
    textoPerfilesFinal = ''
    textoDescartadas = ''
    textoDescartadasFinal = ''

    contadorPerfiles = 0
    contadorDescartadas = 0
    ############################################################################################################
    for i in listaPerfiles[0].getElementsByTagName('perfil'):
        contadorPerfiles +=1
        ##print('\n' + i.getElementsByTagName('nombre')[0].firstChild.data + '\n')
        textoPerfiles += '<perfil>\n'
        textoPerfiles += '  <nombre>' + i.getElementsByTagName('nombre')[0].firstChild.data + '</nombre>\n'
        textoPerfiles += '  <palabrasClave>\n'


        for j in i.getElementsByTagName('palabra'):
            
            
            textoPerfiles += '      <palabra>' + j.firstChild.data + '</palabra>\n'
            
            ##print(j.firstChild.data)
        textoPerfiles += '  </palabrasClave>\n'
        textoPerfiles += '</perfil>\n'
    
    ########################################################################################################################
    ##print(textoPerfiles)
    XmlPerfiles = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Perfiles.xml')
    XmlPerfilesLineas = XmlPerfiles.readlines()
    XmlPerfilesLineas.pop()
    XmlPerfiles.close()
    for i in XmlPerfilesLineas:
        textoPerfilesFinal += i
    textoPerfilesFinal += textoPerfiles
    textoPerfilesFinal += '</perfiles>'

    XmlPerfiles = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Perfiles.xml' , 'w')
    XmlPerfiles.write(textoPerfilesFinal)
    XmlPerfiles.close()
    
    
    for i in listaDescartadas[0].getElementsByTagName('palabra'):
        contadorDescartadas += 1
        textoDescartadas += '   <palabra>' + i.firstChild.data + '</palabra>\n'

    ##print(textoDescartadas)
    XmlDescartadas = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Descartadas.xml')
    XmlDescartadasLineas = XmlDescartadas.readlines()
    XmlDescartadasLineas.pop()
    XmlDescartadas.close()
    for i in XmlDescartadasLineas:
        textoDescartadasFinal += i
    textoDescartadasFinal += textoDescartadas
    textoDescartadasFinal += '</descartadas>'

    XmlDescartadas = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Descartadas.xml' , 'w')
    XmlDescartadas.write(textoDescartadasFinal)
    XmlDescartadas.close()

    respuesta += "<respuesta>\n"
    respuesta += '  <perfilesNuevos>' + ' Se han añadido ' + str(contadorPerfiles) + ' perfiles ' + '</perfilesNuevos>\n'
    respuesta += '  <descartadas>' + ' Se han creado ' + str(contadorDescartadas) + ' nuevas palabras a descartar ' + '</descartadas>\n'
    respuesta += '</respuesta>\n'

    
    ##print(respuesta)
    return respuesta

def AlmacenarMensaje(Mensaje : str):
    fechaLugar = ''
    Usuario = ''
    RedSocial = ''
    escribiendo = ''
    MensajeFinal = ''

    


    MensajeMinuscula = Mensaje.lower()
    ListaPalabras = MensajeMinuscula.split(' ')
    ListaPalabrasOriginal = Mensaje.split(' ')
    ##print(ListaPalabras)

    contador = 0
    for i in ListaPalabras:
        if i == 'fecha:' or i == 'usuario:' or i == 'social:' or i == 'red':
            escribiendo = i
        elif escribiendo == 'fecha:':
            fechaLugar += ListaPalabrasOriginal[contador].replace('\n','') + ' '
        
        elif escribiendo == 'usuario:':
            Usuario += ListaPalabrasOriginal[contador].replace('\n','') + ' '

        elif escribiendo == 'social:':
            RedSocial += ListaPalabrasOriginal[contador].replace('\n','')
            break
        contador +=1
    
    for i in range(contador):
        ListaPalabras.pop(0)
    
    contador2 = 0
    for i in ListaPalabras:
        MensajeFinal += ListaPalabrasOriginal[contador2 + contador] + ' '
        contador2 +=1

    textoXML = '<mensaje>\n'    
    textoXML += '    <fechaHora>' + fechaLugar + '</fechaHora>\n'
    textoXML += '    <usuario>' + Usuario + '</usuario>\n'
    textoXML += '    <texto>' + MensajeFinal + '</texto>\n'
    textoXML += '</mensaje>\n'   
    
    return textoXML

def leerXmlMensaje(xml):
    listaMensajes = xml.getElementsByTagName('mensaje')
    listaUsuarios = []

    contadorMensajes = 0

    for i in listaMensajes:
        contadorMensajes +=1
        xmlMEnsajes = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Mensajes.xml')
        xmlMensajesLineas = xmlMEnsajes.readlines()
        xmlMensajesLineas.pop()
        ##print(xmlMensajesLineas)
        xmlMEnsajes.close
        textoArchivo = ''
        for j in xmlMensajesLineas:
            textoArchivo += j
        textoArchivo += AlmacenarMensaje(i.firstChild.data.replace('\n',''))
        if usuarioMensaje(i.firstChild.data) in listaUsuarios:
            pass
        else:
            listaUsuarios.append(usuarioMensaje(i.firstChild.data))

        textoArchivo += '</mensajes>\n'

        xmlMEnsajes = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Mensajes.xml' , 'w')
        xmlMEnsajes.write(textoArchivo)
        xmlMEnsajes.close()

    respuesta = '<?xml version="1.0"?>\n'
    respuesta += '<respuesta>\n'
    respuesta += '<usuarios>' + ' Se procesaron mensajes para ' + str(len(listaUsuarios))  + ' usuarios' '</usuarios>\n' 
    respuesta += '<mensajes>'  + ' Se procesaron ' + str(contadorMensajes)  + ' mensajes en total'  '</mensajes>\n' 
    respuesta += '</respuesta>\n'

    return respuesta

def obtenerProbabilidad(listaPerfil, mensaje):
    mensaje = re.sub(r'\s+', ' ', mensaje)
    mensaje = re.sub(r'[^\w\s]', '', mensaje)
    mensaje = re.sub(r'\b\d+\b', '', mensaje)
    palabras = mensaje.lower().split()
    

    Listaeliminar=ListaDescartadas()
    for i in palabras:
        if i.lower() in [eliminar.lower() for eliminar in Listaeliminar]:
            palabras.remove(i)
    
    coincidencias = 0
    for i in palabras:
        for j in listaPerfil:
            if i == j:
                coincidencias +=1
    
    resultado =(coincidencias/len(palabras))*100

    return resultado

def ListaDescartadas():
    XmlDescartadas = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Descartadas.xml')
    ObjetoXML = minidom.parse(XmlDescartadas)
    XmlDescartadas.close()
    lista = []

    palabras = ObjetoXML.getElementsByTagName('palabra')

    for i in palabras:
        lista.append(i.firstChild.data)

    return lista

def tablaUsuario(Usuario : str):
    archivoMensajes = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Mensajes.xml')
    archivoPerfiles = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Perfiles.xml')

    XMLmensajes = minidom.parse(archivoMensajes)
    XMLperfiles = minidom.parse(archivoPerfiles)

    archivoMensajes.close()
    archivoPerfiles.close()

    listaPerfiles = XMLperfiles.getElementsByTagName('perfil')
    listaMensajes = XMLmensajes.getElementsByTagName('mensaje')

    tabla = ""

    for i in listaMensajes:
        prGreen('*' + i.getElementsByTagName('usuario')[0].firstChild.data.replace(" ", "") + '*')
        prGreen('*' + Usuario.replace(" ", "") + '*')
        print('')

        

        if i.getElementsByTagName('usuario')[0].firstChild.data.replace(" ", "") == Usuario.replace(" ", ""):
            tabla += 'Mensaje : ' + i.getElementsByTagName('fechaHora')[0].firstChild.data.replace(" ", "") + '\n'
            for j in listaPerfiles:
                tabla += '_______' + j.getElementsByTagName('nombre')[0].firstChild.data.replace(" ", "") + ' : ' + str(obtenerProbabilidad(ObtenerListaPerfil(j.getElementsByTagName('nombre')[0].firstChild.data),i.getElementsByTagName('texto')[0].firstChild.data)) + '\n'

    return tabla            


def ObtenerListaPerfil(nombre):
    archivoPerfiles = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Perfiles.xml')
    XMLperfiles = minidom.parse(archivoPerfiles)
    archivoPerfiles.close()
    listaPerfiles = XMLperfiles.getElementsByTagName('perfil')

    lista = []

    for i in listaPerfiles:
        if i.getElementsByTagName('nombre')[0].firstChild.data == nombre:
            for j in i.getElementsByTagName('palabra'):
                lista.append(j.firstChild.data)

    return lista

def resetear():
    XmlPerfiles = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Perfiles.xml' , 'w')
    XmlPerfiles.write('''<?xml version="1.0"?> 
<perfiles>
</perfiles>''')
    XmlPerfiles.close()

    XmlMensajes = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Mensajes.xml' , 'w')
    XmlMensajes.write('''<?xml version="1.0"?> 
<mensajes>
</mensajes>
''')
    XmlMensajes.close()

    XmlDescartadas = open('C:/Users/Luisda/Desktop/IPC2_PROYECTO3/backend/funciones/Descartadas.xml' , 'w')
    XmlDescartadas.write('''<?xml version="1.0"?> 
<descartadas> 
</descartadas>
''')
    XmlMensajes.close()

def usuarioMensaje(Mensaje):
    fechaLugar = ''
    Usuario = ''
    RedSocial = ''
    escribiendo = ''
    MensajeFinal = ''

    


    MensajeMinuscula = Mensaje.lower()
    ListaPalabras = MensajeMinuscula.split(' ')
    ListaPalabrasOriginal = Mensaje.split(' ')
    ##print(ListaPalabras)

    contador = 0
    for i in ListaPalabras:
        if i == 'fecha:' or i == 'usuario:' or i == 'social:' or i == 'red':
            escribiendo = i
        elif escribiendo == 'fecha:':
            fechaLugar += ListaPalabrasOriginal[contador].replace('\n','') + ' '
        
        elif escribiendo == 'usuario:':
            return ListaPalabrasOriginal[contador].replace('\n','') 

        elif escribiendo == 'social:':
            RedSocial += ListaPalabrasOriginal[contador].replace('\n','')
            break
        contador +=1





