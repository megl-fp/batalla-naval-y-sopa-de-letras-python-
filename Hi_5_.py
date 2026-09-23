import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint
import copy

def menu_principal(root):
    def LlamarSopa():
        # Configuración del canvas
        canvas_menuS.destroy()
        sopaLetras(root)
    
    def LlamarBatalla():
        # Configuración del canvas
        canvas_menuS.destroy()
        BatallaNaval(root)
        
    # cerrar el juego, boton salir le llama.
    def exit_game():
        root.quit()

    
    # Obtener el tamaño de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Configuración del canvas
    global canvas_menuS
    canvas_menuS = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas_menuS.pack(fill="both", expand=True)

    # Cargar la imagen de fondo usando Pillow
    ruta_imagen = r"pantalla_principal.png"
    imagen_fondo = Image.open(ruta_imagen)
    imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    # Guardar una referencia de la imagen
    canvas_menuS.image = imagen_fondo_tk

    # Mostrar la imagen de fondo en el canvas
    canvas_menuS.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)

    # Crear boton Sopa de letras
    boton_sopa = tk.Button(canvas_menuS, text="Sopa de Letras", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=LlamarSopa)
    canvas_menuS.create_window(screen_width * 0.25, screen_height * 0.3, window=boton_sopa)

    # Crear boton Batalla Naval
    boton_batalla = tk.Button(canvas_menuS, text="Batalla Naval", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=LlamarBatalla)
    canvas_menuS.create_window(screen_width * 0.25, screen_height * 0.5, window=boton_batalla)

    # Crear boton para salir
    boton_salir = tk.Button(canvas_menuS, text="Salir", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=exit_game)
    canvas_menuS.create_window(screen_width * 0.25, screen_height * 0.7, window=boton_salir)
    

def sopaLetras(root):
    def ingresar_hora():
        def verificar_hora():
            global tiempo_segundo  # tiempo_segundo debe ser global
            tiempo_minutos = entry.get()
            
            if len(tiempo_minutos) != 5:
                return False
            
            if tiempo_minutos[2] != ":":
                return False
            minutos = tiempo_minutos[:2]
            segundos = tiempo_minutos[3:]

            if not (minutos.isdigit() and segundos.isdigit()):
                return False
            minutos = int(minutos)
            segundos = int(segundos)

            if minutos == 0 and segundos == 0:
                return False
            
            if 0 <= minutos < 60 and 0 <= segundos < 60:
                tiempo_segundo = minutos * 60 + segundos
                return True
            return False
        
        def modificarHora():
            if verificar_hora():
                canvasModificarHora.destroy()
                boton_tiempo.config(text=f"Tiempo: {pasar_seg_min()}")
            else:
                # Crear un label para mensaje de error (usando el canvas)
                label_mensaje = tk.Label(canvasModificarHora, text="Formato incorrecto")
                canvasModificarHora.create_window(250, 250, window=label_mensaje, anchor="center")
                # Programar la destrucción del label después de 2000 milisegundos (2 segundos)
                canvasModificarHora.after(2000, label_mensaje.destroy)

        # Configuración del canvas Ingresar Hora
        canvasModificarHora = tk.Canvas(canvas_menuS, bg="yellow", width=500, height=500)
        canvas_menuS.create_window(400, 350, window=canvasModificarHora)  # Posicionar canvasModificarHora dentro de canvas principal

        # Crear una etiqueta de Ingresar Hora (usando el canvas de ModificarHora)
        label_ingresarHora = tk.Label(canvasModificarHora, text="Ingresa el tiempo (formato mm:ss)")
        canvasModificarHora.create_window(250, 100, window=label_ingresarHora, anchor="center")
                
        # Crear una entrada para agregar palabras
        entry = tk.Entry(canvasModificarHora, width=10, font=("Cooper Black", 14), borderwidth=10)
        canvasModificarHora.create_window(250, 200, window=entry)
        entry.bind("<Return>", lambda event: modificarHora())

        # Crear el botón verificar tiempo
        boton_verificar = tk.Button(canvasModificarHora, text="Ingresar Hora", command=modificarHora)
        canvasModificarHora.create_window(250, 300, window=boton_verificar)  # Posicionar el botón en el canvas principal

    def pasar_seg_min():
        tiempo_minutos = ""
        min = tiempo_segundo // 60
        seg = tiempo_segundo % 60

        if min < 10:
            tiempo_minutos += f"0{min}:"
        else:
            tiempo_minutos += f"{min}:"

        if seg < 10:
            tiempo_minutos += f"0{seg}"
        else:
            tiempo_minutos += f"{seg}"
        return tiempo_minutos

    def Iniciar_Sopa(root):
        global sopaDeLetras
        palabras = []
        sopaDeLetras = llenar_sopa()
        mostrar_matriz(sopaDeLetras , tiempo_segundo , root)

    def Instruccion_Sopa(root):
        def Llamar_Sopa_desde_Ins():
            canvas_Intruccion.destroy()
            menuSopa(root)

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Configuración del canvas
        canvas_Intruccion = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas_Intruccion.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"intruccion_Sopa.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

        # Guardar una referencia de la imagen
        canvas_Intruccion.image = imagen_fondo_tk

        # Mostrar la imagen de fondo en el canvas
        canvas_Intruccion.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)
        

        # Crear boton para salir
        boton_salir = tk.Button(canvas_Intruccion, text="Salir", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command = Llamar_Sopa_desde_Ins)
        canvas_Intruccion.create_window(screen_width * 0.25, screen_height * 0.7, window=boton_salir)

    def menuSopa(root):
        def LlamarMenu_Principal():
            canvas_menuS.destroy()
            menu_principal(root)

        def Llamar_iniciar_juegoSopa():
            canvas_menuS.destroy()
            Iniciar_Sopa(root)
        
        def Llamar_Instrucciones():
            canvas_menuS.destroy()
            Instruccion_Sopa(root)

        # Variable global para el tiempo
        global tiempo_segundo , boton_tiempo
        tiempo_segundo = 120

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Configuración del canvas
        global canvas_menuS
        canvas_menuS = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas_menuS.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"menu_Sopa_.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

        # Guardar una referencia de la imagen
        canvas_menuS.image = imagen_fondo_tk

        # Mostrar la imagen de fondo en el canvas
        canvas_menuS.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)
        
        # Crear boton iniciar Sopa
        boton_iniciar_sopa = tk.Button(canvas_menuS, text="Iniciar", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=Llamar_iniciar_juegoSopa)
        canvas_menuS.create_window(screen_width * 0.25, screen_height * 0.3, window=boton_iniciar_sopa)

        # Crear boton Tiempo 
        boton_tiempo = tk.Button(canvas_menuS, text=f"Tiempo: {pasar_seg_min()}", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=ingresar_hora)
        canvas_menuS.create_window(screen_width * 0.25, screen_height * 0.4, window=boton_tiempo)

        # Crear boton Instruccion
        boton_instruccion = tk.Button(canvas_menuS, text="Intrucciones ", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=Llamar_Instrucciones)
        canvas_menuS.create_window(screen_width * 0.25, screen_height * 0.5, window=boton_instruccion)


        # Crear boton para salir
        boton_salir = tk.Button(canvas_menuS, text="Salir", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=LlamarMenu_Principal)
        canvas_menuS.create_window(screen_width * 0.25, screen_height * 0.7, window=boton_salir)

    def llenar_sopa():
        letras = "AAAAABBCCCDDEEEEFFGGHIIIJKLLMMNNÑOOOOPPPQRRSSSTTUUUVWXYZ"
        sopa = []
        for i in range(10):
            fila = []
            for j in range(10):
                letter = random.choice(letras)
                fila.append(letter)
            sopa.append(fila)
        return sopa

    def separarPalabra(cadena):
        cadena = cadena + " "

        palabra1 = False
        for i in range(len(cadena) - 1):
            if cadena[i] == " ":
                palabra1 = True
        if palabra1 == False:
            cad = cadena[:len(cadena) - 2]
            l = [cadena]
            return l
        count = 0;
        lista = []
        pdiv = ""
        for i in range(len(cadena)):
            if cadena[i] != " ":
                pdiv = pdiv + cadena[i]
            else:
                lista.append(pdiv)
                pdiv = ""
        return lista

    def validar(Lista_pal):
        list = []
        for i in Lista_pal:
            list += separarPalabra(i)
        Lista_pal = list

        for i in range(len(Lista_pal)):
            Lista_pal[i] = Lista_pal[i].upper()

        lis_pal = []
        acentos = ["Á", "É", "Í", "Ó", "Ú"]
        sin_acentos = ["A", "E", "I", "O", "U"]

        for i in range(len(Lista_pal)):
            pal = ""
            for a in range(len(Lista_pal[i])):
                if Lista_pal[i][a].isalpha():
                    letra = Lista_pal[i][a].upper()
                    # Reemplazar letras acentuadas
                    if letra in acentos:
                        letra = sin_acentos[acentos.index(letra)]
                    pal += letra
            lis_pal.append(pal)
        return lis_pal

    def diccionario(palabras):
        diccionario = {"AARON", "ABAJO", "ABANDONADO", "ABANDONAR", "ABBY", "ABIERTA", "ABIERTO", "ABIERTOS", "ABOGADO", "ABOGADOS", "ABRA", "ABRAN", "ABRAZO", "ABRE", "ABRIGO", "ABRIL", "ABRIR", "ABRIO", "ABSOLUTAMENTE", "ABSOLUTO", "ABSURDO", "ABUELA", "ABUELO", "ABURRIDO", "ACA", "ACABA", "ACABADO", "ACABAMOS", "ACABAN", "ACABAR", "ACABARA", "ACABAS", "ACABE", "ACABO", "ACABO", "ACADEMIA", "ACASO", "ACCESO", "ACCIDENTE", "ACCIONES", "ACCION", "ACEITE", "ACEPTA", "ACEPTADO", "ACEPTAR", "ACEPTO", "ACERCA", "ACERO", "ACERQUES", "ACOSTUMBRADO", "ACTITUD", "ACTIVIDAD", "ACTO", "ACTOR", "ACTORES", "ACTRIZ", "ACTUACION", "ACTUAL", "ACTUANDO", "ACTUAR", "ACTUA", "ACUERDA", "ACUERDAS", "ACUERDO", "ACUSADO", "ACA", "ACERCATE", "ADAM", "ADECUADO", "ADELANTE", "ADEMAS", "ADENTRO", "ADIOS", "ADIVINA", "ADIVINAR", "ADIOS", "ADMINISTRACION", "ADMIRO", "ADMITIR", "ADN", "ADONDE", "ADORABLE", "ADORO", "ADULTO", "ADULTOS", "ADVERTENCIA", "ADVIERTO", "ADONDE", "AEROPUERTO", "AFECTA", "AFGANISTAN", "AFORTUNADO", "AFUERA", "AGARRA", "AGARRAR", "AGENCIA", "AGENDA", "AGENTE", "AGENTES", "AGRADA", "AGRADABLE", "AGRADEZCO", "AGUA", "AGUANTA", "AGUANTAR", "AGUAS", "AGUJA", "AGUJERO", "AGARRATE", "AHI", "AHORA", "AHI", "AIGO", "AIRE", "ALA", "ALAN", "ALARMA", "ALAS", "ALBERT", "ALCALDE", "ALCANCE", "ALCANZAR", "ALCOHOL", "ALDEA", "ALEGRA", "ALEGRO", "ALEGRIA", "ALEJANDRO", "ALEMANES", "ALEMANIA", "ALEMAN", "ALERTA", "ALEX", "ALFOMBRA", "ALGO", "ALGUACIL", "ALGUIEN", "ALGUN", "ALGUNA", "ALGUNAS", "ALGUNO", "ALGUNOS", "ALGUN", "ALIANZA", "ALICE", "ALIENTO", "ALLA", "ALLI", "ALLA", "ALLI", "ALMA", "ALMAS", "ALMIRANTE", "ALMORZAR", "ALMUERZO", "ALQUILER", "ALREDEDOR", "ALTA", "ALTERNATIVA", "ALTEZA", "ALTO", "ALTOS", "ALTURA", "ALEJATE", "AMA", "AMABA", "AMABLE", "AMADO", "AMANECER", "AMANTE", "AMANTES", "AMAR", "AMARILLO", "AMAS", "AMBAS", "AMBIENTE", "AMBOS", "AMBULANCIA", "AMENAZA", "AMERICANA", "AMERICANO", "AMERICANOS", "AMIGA", "AMIGAS", "AMIGO", "AMIGOS", "AMISTAD", "AMO", "AMOR", "AMY", "AMEN", "AMERICA", "ANCIANO", "AND", "ANDA", "ANDANDO", "ANDAR", "ANDAS", "ANDERSON", "ANDREW", "ANDY", "ANGELA", "ANGELES", "ANGIE", "ANILLO", "ANIMAL", "ANIMALES", "ANIVERSARIO", "ANNA", "ANNE", "ANNIE", "ANOCHE", "ANTE", "ANTECEDENTES", "ANTERIOR", "ANTES", "ANTIGUA", "ANTIGUO", "ANTIGUOS", "ANUNCIO", "ANALISIS", "APAGA", "APAGAR", "APARATO", "APARECE", "APARECER", "APARECIO", "APARENTEMENTE", "APARTAMENTO", "APARTE", "APELLIDO", "APENAS", "APESTA", "APETECE", "APOLO", "APOSTAR", "APOYO", "APRECIO", "APRENDE", "APRENDER", "APRENDIDO", "APRENDI", "APROPIADO", "APROXIMADAMENTE", "APUESTA", "APUESTAS", "APUESTO", "APUNTA", "APURATE", "APURENSE", "AQUEL", "AQUELLA", "AQUELLO", "AQUELLOS", "AQUI", "AQUILES", "AQUI", "ARAÑA", "ARCHIVO", "ARCHIVOS", "ARCO", "ARENA", "ARMA", "ARMADA", "ARMADO", "ARMADOS", "ARMARIO", "ARMAS", "ARREGLADO", "ARREGLAR", "ARREGLARLO", "ARREGLO", "ARRESTADO", "ARRESTO", "ARRIBA", "ARRUINADO", "ARRUINAR", "ARTE", "ARTHUR", "ARTISTA", "ARTURO", "ARTICULO", "ASALTO", "ASCENSOR", "ASCO", "ASEGURAR", "ASEGURARME", "ASEGURO", "ASEGURATE", "ASESINA", "ASESINADO", "ASESINATO", "ASESINATOS", "ASESINO", "ASESINOS", "ASI", "ASIENTO", "ASIENTOS", "ASISTENTE", "ASOMBROSO", "ASPECTO", "ASQUEROSO", "ASUNTO", "ASUNTOS", "ASUSTA", "ASUSTADA", "ASUSTADO", "ASI", "ATACA", "ATACAR", "ATACO", "ATAQUE", "ATAQUES", "ATENCION", "ATENDER", "ATERRIZAJE", "ATERRIZAR", "ATHENA", "ATRACTIVO", "ATRAPADO", "ATRAPADOS", "ATRAPAR", "ATRAS", "ATRAVESAR", "ATREVES", "ATRAS", "AUDIENCIA", "AUDREY", "AUN", "AUNQUE", "AUTO", "AUTOBUS", "AUTOPISTA", "AUTORIDAD", "AUTORIDADES", "AUTORIZACION", "AUTOS", "AUXILIO", "AVE", "AVENTURA", "AVERIGUAR", "AVERIGUARLO", "AVIONES", "AVISO", "AVION", "AYER", "AYUDA", "AYUDADO", "AYUDANDO", "AYUDANTE", "AYUDAR", "AYUDARLA", "AYUDARLE", "AYUDARLO", "AYUDARLOS", "AYUDARME", "AYUDARNOS", "AYUDARTE", "AYUDARA", "AYUDARE", "AYUDAS", "AYUDE", "AYUDO", "AYUDO", "AYUDAME", "AYUDEME", "AYUDENME", "AZUL", "AZULES", "AZUCAR", "AEREA", "AEREO", "AÑO", "AÑOS", "AUN", "BAILANDO", "BAILAR", "BAILE", "BAJA", "BAJANDO", "BAJAR", "BAJAS", "BAJE", "BAJEN", "BAJO", "BALA", "BALAS", "BALBOA", "BANCO", "BANCOS", "BANDA", "BANDERA", "BAR", "BARATO", "BARBARA", "BARCO", "BARCOS", "BARRA", "BARRIO", "BARRY", "BART", "BASE", "BASTA", "BASTANTE", "BASTARDO", "BASTARDOS", "BASURA", "BATALLA", "BAÑO", "BEBE", "BEBER", "BEBIDA", "BEBIDAS", "BEBIENDO", "BEBE", "BEBES", "BELLA", "BELLEZA", "BELLO", "BEN", "BENDICION", "BENDIGA", "BENNY", "BENTON", "BERLIN", "BESAR", "BESO", "BESTIA", "BETTY", "BIBLIA", "BIBLIOTECA", "BICICLETA", "BIEN", "BIENES", "BIENVENIDA", "BIENVENIDO", "BIENVENIDOS", "BIG", "BILL", "BILLETES", "BILLY", "BIN", "BLACK", "BLANCA", "BLANCO", "BLANCOS", "BOB", "BOBBY", "BOCA", "BODA", "BODAS", "BOLA", "BOLAS", "BOLETO", "BOLETOS", "BOLSA", "BOLSAS", "BOLSILLO", "BOLSO", "BOMBA", "BOMBAS", "BOMBEROS", "BOND", "BONITA", "BONITO", "BORDE", "BORDO", "BORRACHO", "BOSQUE", "BOSTON", "BOTAS", "BOTE", "BOTELLA", "BOTON", "BOURNE", "BRAD", "BRAVO", "BRAZO", "BRAZOS", "BREVE", "BRIAN", "BRIDGET", "BRILLANTE", "BRINDIS", "BRITANICO", "BRITANICOS", "BROMA", "BROMAS", "BROMEANDO", "BROMEAS", "BROWN", "BRUCE", "BRUJA", "BRUJAS", "BUCK", "BUDDY", "BUEN", "BUENA", "BUENAS", "BUENO", "BUENOS", "BURKE", "BURRO", "BUSCA", "BUSCABA", "BUSCADO", "BUSCAMOS", "BUSCAN", "BUSCANDO", "BUSCAR", "BUSCARLO", "BUSCARTE", "BUSCARE", "BUSCAS", "BUSCO", "BUSH", "BUSQUE", "BUSQUEN", "BUZZ", "BASICAMENTE", "BEISBOL", "BUSQUEDA", "CABALLERO", "CABALLEROS", "CABALLO", "CABALLOS", "CABAÑA", "CABELLO", "CABEZA", "CABEZAS", "CABINA", "CABLE", "CABO", "CABRA", "CABRONES", "CABRON", "CADA", "CADENA", "CADAVER", "CADAVERES", "CAE", "CAER", "CAFETERIA", "CAFE", "CAJA", "CAJAS", "CALIDAD", "CALIENTE", "CALIFORNIA", "CALLA", "CALLADO", "CALLATE", "CALLE", "CALLES", "CALMA", "CALOR", "CALVIN", "CAMA", "CAMARADA", "CAMBIA", "CAMBIADO", "CAMBIAN", "CAMBIANDO", "CAMBIAR", "CAMBIE", "CAMBIO", "CAMBIOS", "CAMBIE", "CAMBIO", "CAMINA", "CAMINANDO", "CAMINAR", "CAMINO", "CAMIONES", "CAMIONETA", "CAMISA", "CAMION", "CAMPAMENTO", "CAMPAÑA", "CAMPEONATO", "CAMPEON", "CAMPO", "CAMPOS", "CANAL", "CANCIONES", "CANCION", "CANSADA", "CANSADO", "CANTA", "CANTANDO", "CANTANTE", "CANTAR", "CANTIDAD", "CAOS", "CAPA", "CAPACIDAD", "CAPAZ", "CAPITAL", "CAPITAN", "CAPITAN", "CAPITULO", "CARA", "CARAJO", "CARAMBA", "CARAS", "CARAY", "CARGA", "CARGAR", "CARGO", "CARGOS", "CARIDAD", "CARIÑO", "CARL", "CARLA", "CARLOS", "CARNE", "CARO", "CAROL", "CARRERA", "CARRERAS", "CARRETERA", "CARRO", "CARTA", "CARTAS", "CARTER", "CARTERA", "CARACTER", "CASA", "CASADA", "CASADO", "CASADOS", "CASAR", "CASARME", "CASARSE", "CASARTE", "CASAS", "CASCO", "CASI", "CASINO", "CASO", "CASOS", "CASTIGO", "CASTILLO", "CASTLE", "CASUALIDAD", "CASO", "CATHERINE", "CAUSA", "CAUSADO", "CAUSAR", "CAYENDO", "CAYO", "CAZA", "CAZADOR", "CAZAR", "CAIDA", "CAIDO", "CAÑON", "CELDA", "CELEBRAR", "CELOSO", "CELULAR", "CEMENTERIO", "CENA", "CENAR", "CENTAVO", "CENTAVOS", "CENTRAL", "CENTRO", "CERCA", "CERCANO", "CERDO", "CERDOS", "CEREBRAL", "CEREBRO", "CEREMONIA", "CERO", "CERRADA", "CERRADO", "CERRAR", "CERVEZA", "CHAQUETA", "CHARLA", "CHARLES", "CHARLIE", "CHARLOTTE", "CHEQUE", "CHICA", "CHICAGO", "CHICAS", "CHICO", "CHICOS", "CHINA", "CHINO", "CHINOS", "CHISTE", "CHLOE", "CHOCOLATE", "CHOFER", "CHRIS", "CIA", "CICATRIZ", "CIEGA", "CIEGO", "CIELO", "CIELOS", "CIEN", "CIENCIA", "CIENCIAS", "CIENTO", "CIENTOS", "CIENTIFICO", "CIENTIFICOS", "CIERRA", "CIERRE", "CIERREN", "CIERTA", "CIERTAMENTE", "CIERTAS", "CIERTO", "CIERTOS", "CIGARRILLO", "CIGARRILLOS", "CIMA", "CINCO", "CINCUENTA", "CINDY", "CINE", "CINTA", "CINTURON", "CIRCO", "CIRCUNSTANCIAS", "CIRUGIA", "CIRUJANO", "CITA", "CITAS", "CITY", "CIUDAD", "CIUDADANO", "CIUDADANOS", "CIUDADES", "CIVIL", "CIVILES", "CIVILIZACION", "CLAIRE", "CLARA", "CLARAMENTE", "CLARK", "CLARO", "CLASE", "CLASES", "CLAVE", "CLIENTE", "CLIENTES", "CLIMA", "CLUB", "CLINICA", "COBARDE", "COBRA", "COCA", "COCAINA", "COCHE", "COCHES", "COCINA", "COCINAR", "COGE", "COGER", "COHEN", "COHETE", "COINCIDENCIA", "COLA", "COLE", "COLECCION", "COLEGA", "COLEGAS", "COLEGIO", "COLGAR", "COLINA", "COLLAR", "COLOR", "COLORES", "COLT", "COLUMNA", "COMA", "COMANDANTE", "COMANDO", "COMBATE", "COMBUSTIBLE", "COME", "COMEN", "COMENCE", "COMENZAMOS", "COMENZAR", "COMENZO", "COMER", "COMERCIAL", "COMES", "COMETER", "COMETIDO", "COMIDA", "COMIDO", "COMIENDO", "COMIENZA", "COMIENZO", "COMISARIO", "COMISION", "COMITE", "COMIO", "COMO", "COMPARTIR", "COMPASION", "COMPAÑERA", "COMPAÑERO", "COMPAÑEROS", "COMPAÑIA", "COMPAÑIAS", "COMPETENCIA", "COMPLEJO", "COMPLETA", "COMPLETAMENTE", "COMPLETO", "COMPLICADO", "COMPORTAMIENTO", "COMPRA", "COMPRADO", "COMPRAR", "COMPRAS", "COMPRENDE", "COMPRENDER", "COMPRENDES", "COMPRENDO", "COMPROMISO", "COMPRE", "COMPRO", "COMPUTADORA", "COMPUTADORAS", "COMUNICACION", "COMUNIDAD", "COMUN", "CON", "CONCEPTO", "CONCIENCIA", "CONCIERTO", "CONCURSO", "CONCENTRATE", "CONDADO", "CONDE", "CONDENADO", "CONDICIONES", "CONDICION", "CONDUCE", "CONDUCIR", "CONDUCTA", "CONDUCTOR", "CONEJO", "CONEXION", "CONFERENCIA", "CONFESION", "CONFIANZA", "CONFIAR", "CONFIRMADO", "CONFLICTO", "CONFUNDIDO", "CONFIA", "CONFIO", "CONGRESO", "CONMIGO", "CONOCE", "CONOCEMOS", "CONOCEN", "CONOCER", "CONOCERLA", "CONOCERLO", "CONOCERTE", "CONOCES", "CONOCIDA", "CONOCIDO", "CONOCIMIENTO", "CONOCIMOS", "CONOCISTE", "CONOCIO", "CONOCI", "CONOCIA", "CONOZCA", "CONOZCO", "CONSCIENTE", "CONSECUENCIAS", "CONSEGUIDO", "CONSEGUIMOS", "CONSEGUIR", "CONSEGUIRE", "CONSEGUISTE", "CONSEGUI", "CONSEJO", "CONSEJOS", "CONSIDERA", "CONSIDERADO", "CONSIDERANDO", "CONSIDERAR", "CONSIGO", "CONSIGUE", "CONSIGUIO", "CONSTRUCCION", "CONSTRUIR", "CONSTRUYO", "CONTACTO", "CONTACTOS", "CONTADO", "CONTANDO", "CONTAR", "CONTARE", "CONTENTA", "CONTENTO", "CONTESTA", "CONTESTAR", "CONTIENE", "CONTIGO", "CONTINUAR", "CONTINUA", "CONTINUE", "CONTRA", "CONTRARIO", "CONTRATO", "CONTROL", "CONTROLA", "CONTROLAR", "CONTE", "CONTO", "CONVENCER", "CONVENCIDO", "CONVERSACION", "CONVERSAR", "CONVERTIDO", "CONVERTIRSE", "CONVIERTE", "CONVIRTIO", "COOPER", "COORDENADAS", "COPA", "COPIA", "COPIAS", "CORAJE", "CORAZONES", "CORAZON", "CORBATA", "COREA", "CORONA", "CORONEL", "CORRAN", "CORRE", "CORRECTA", "CORRECTO", "CORREDOR", "CORREO", "CORRER", "CORRIENDO", "CORRIENTE", "CORTA", "CORTADO", "CORTAR", "CORTE", "CORTEN", "CORTO", "CORTO", "COSA", "COSAS", "COSTA", "COSTADO", "COSTUMBRE", "COSTO", "COÑO", "CREA", "CREADO", "CREAR", "CREAS", "CREASY", "CRECER", "CREE", "CREEMOS", "CREEN", "CREER", "CREERLO", "CREES", "CREMA", "CREO", "CRETINO", "CREYO", "CREI", "CREIA", "CREO", "CRIATURA", "CRIATURAS", "CRIMEN", "CRIMINAL", "CRIMINALES", "CRISIS", "CRISTAL", "CRISTO", "CRUEL", "CRUZ", "CRUZAR", "CREDITO", "CREEME", "CRIMENES", "CUADRO", "CUAL", "CUALES", "CUALQUIER", "CUALQUIERA", "CUANDO", "CUANTAS", "CUANTO", "CUANTOS", "CUARTA", "CUARTEL", "CUARTO", "CUATRO", "CUBIERTA", "CUBIERTO", "CUBRIR", "CUCHILLO", "CUELLO", "CUENTA", "CUENTAS", "CUENTE", "CUENTO", "CUENTOS", "CUERDA", "CUERO", "CUERPO", "CUERPOS", "CUESTA", "CUESTION", "CUEVA", "CUIDA", "CUIDADO", "CUIDANDO", "CUIDAR", "CULO", "CULPA", "CULPABLE", "CULTURA", "CUMPLEAÑOS", "CUMPLIDO", "CUMPLIR", "CURA", "CURIOSIDAD", "CURIOSO", "CURSO", "CUSTODIA", "CUYO", "CUAL", "CUALES", "CUAN", "CUANDO", "CUANTA", "CUANTAS", "CUANTO", "CUANTOS", "CUENTAME", "CUIDATE", "CYNTHIA", "CALLATE", "CALMATE", "CALMESE", "CAMARA", "CAMARAS", "CANCER", "CARCEL", "CELULA", "CELULAS", "CESAR", "CIRCULO", "CODIGO", "CODIGOS", "COMO", "COMODO", "DA", "DABA", "DADO", "DALE", "DAMA", "DAMAS", "DAME", "DAMIEN", "DAMOS", "DAN", "DANA", "DANDO", "DANIEL", "DANNY", "DAR", "DAREMOS", "DARLE", "DARLES", "DARME", "DARNOS", "DARSE", "DARTE", "DARA", "DARAN", "DARE", "DARIA", "DAS", "DATA", "DATE", "DATOS", "DAVE", "DAVID", "DAVIS", "DAÑO", "DAÑOS", "DE", "DEAN", "DEBA", "DEBAJO", "DEBAMOS", "DEBE", "DEBEMOS", "DEBEN", "DEBER", "DEBERIA", "DEBERIAS", "DEBERA", "DEBERIA", "DEBERIAMOS", "DEBERIAN", "DEBERIAS", "DEBES", "DEBIDO", "DEBILIDAD", "DEBISTE", "DEBIO", "DEBO", "DEBI", "DEBIA", "DECENTE", "DECIDE", "DECIDIDO", "DECIDIR", "DECIDIO", "DECIDI", "DECIMOS", "DECIR", "DECIRLE", "DECIRLES", "DECIRLO", "DECIRME", "DECIRNOS", "DECIRTE", "DECISIONES", "DECISION", "DECLARACION", "DECIA", "DECIAN", "DECIAS", "DECIRSELO", "DECIRTELO", "DEDO", "DEDOS", "DEFENDER", "DEFENSA", "DEFINITIVAMENTE", "DEI", "DEJA", "DEJADO", "DEJAME", "DEJAMOS", "DEJAN", "DEJANDO", "DEJAR", "DEJARA", "DEJAREMOS", "DEJARLA", "DEJARLO", "DEJARME", "DEJARON", "DEJARTE", "DEJARA", "DEJARAN", "DEJARAS", "DEJARE", "DEJARIA", "DEJAS", "DEJASTE", "DEJE", "DEJEMOS", "DEJEN", "DEJES", "DEJO", "DEJE", "DEJO", "DEL", "DELANTE", "DELICIOSO", "DEMANDA", "DEMASIADA", "DEMASIADAS", "DEMASIADO", "DEMASIADOS", "DEME", "DEMONIO", "DEMONIOS", "DEMOSTRAR", "DEMAS", "DEN", "DENTRO", "DEPARTAMENTO", "DEPENDE", "DEPORTE", "DEPRISA", "DEPOSITO", "DERECHA", "DERECHO", "DERECHOS", "DES", "DESAFORTUNADAMENTE", "DESAGRADABLE", "DESAPARECE", "DESAPARECER", "DESAPARECIDO", "DESAPARECIO", "DESASTRE", "DESAYUNAR", "DESAYUNO", "DESCANSA", "DESCANSAR", "DESCANSO", "DESCONOCIDO", "DESCUBIERTO", "DESCUBRIR", "DESCUBRIO", "DESCUBRI", "DESCUIDA", "DESDE", "DESEA", "DESEAN", "DESEARIA", "DESEAS", "DESEO", "DESEOS", "DESGRACIA", "DESGRACIADO", "DESIERTO", "DESNUDA", "DESNUDO", "DESPACHO", "DESPACIO", "DESPEDIDA", "DESPEDIDO", "DESPEJADO", "DESPERTAR", "DESPERTE", "DESPIERTA", "DESPIERTE", "DESPIERTO", "DESPUES", "DESPUES", "DESTINO", "DESTRUCCION", "DESTRUIDO", "DESTRUIR", "DETALLE", "DETALLES", "DETECTIVE", "DETENER", "DETENERLO", "DETENGA", "DETENGAN", "DETENIDO", "DETENTE", "DETRAS", "DEUDA", "DEVOLVER", "DEX", "DIA", "DIABLO", "DIABLOS", "DIAMANTE", "DIAMANTES", "DIARIO", "DIAS", "DIBUJO", "DIBUJOS", "DICE", "DICEN", "DICES", "DICHO", "DICIENDO", "DICK", "DIENTES", "DIERA", "DIERON", "DIETA", "DIEZ", "DIFERENCIA", "DIFERENTE", "DIFERENTES", "DIFICIL", "DIFICIL", "DIFICILES", "DIGA", "DIGAMOS", "DIGAN", "DIGAS", "DIGNO", "DIGO", "DIJE", "DIJERA", "DIJERON", "DIJIMOS", "DIJISTE", "DIJO", "DILE", "DILES", "DILO", "DIME", "DIMOS", "DINERO", "DINOS", "DIO", "DIOS", "DIOSA", "DIOSES", "DIRECCION", "DIRECTAMENTE", "DIRECTO", "DIRECTOR", "DIRIGE", "DIRA", "DIRAS", "DIRE", "DIRIA", "DIRIAS", "DISCO", "DISCOS", "DISCULPA", "DISCULPARME", "DISCULPAS", "DISCULPE", "DISCULPEN", "DISCURSO", "DISCUSION", "DISCUTIR", "DISCULPAME", "DISCULPEME", "DISEÑO", "DISFRAZ", "DISFRUTA", "DISFRUTAR", "DISPARA", "DISPARADO", "DISPARANDO", "DISPARAR", "DISPARARON", "DISPAREN", "DISPARO", "DISPAROS", "DISPARO", "DISPONIBLE", "DISPUESTO", "DISTANCIA", "DISTE", "DISTINTO", "DISTRITO", "DIVERSION", "DIVERTIDO", "DIVISION", "DIVORCIO", "DIO", "DO", "DOBLE", "DOC", "DOCE", "DOCENA", "DOCTOR", "DOCTORA", "DOCTORES", "DOCUMENTOS", "DOLARES", "DOLOR", "DOLORES", "DOMINGO", "DON", "DONALD", "DONDE", "DONNA", "DORMIDA", "DORMIDO", "DORMIR", "DORMITORIO", "DOS", "DOSIS", "DOUG", "DOY", "DRA", "DRAGON", "DROGA", "DROGAS", "DRACULA", "DUCHA", "DUDA", "DUDAS", "DUDE", "DUDO", "DUELE", "DUERME", "DUEÑO", "DULCE", "DULCES", "DURA", "DURANTE", "DURMIENDO", "DURO", "DAMELO", "DEBIL", "DEJALA", "DEJALO", "DEJAME", "DEJEME", "DEJENME", "DEME", "DIA", "DIAS", "DIGALE", "DIGAME", "DIMELO", "DISELO", "DOLAR", "DOLARES", "DONDE", "EARL", "ECHA", "ECHADO", "ECHAR", "ECHO", "EDAD", "EDDIE", "EDIFICIO", "EDUCACION", "EDWARD", "EEUU", "EFECTIVO", "EFECTO", "EFECTOS", "EGOISTA", "EI", "EJEMPLO", "EJERCICIO", "EJERCITO", "EJERCITO", "ELECCIONES", "ELECCION", "ELECTRICIDAD", "ELEGANTE", "ELEGIDO", "ELEGIR", "ELIMINAR", "ELIZABETH", "ELLA", "ELLAS", "ELLO", "ELLOS", "EMBAJADA", "EMBAJADOR", "EMBARAZADA", "EMBARGO", "EMERGENCIA", "EMILY", "EMOCIONANTE", "EMOCIONES", "EMOCION", "EMPECEMOS", "EMPECE", "EMPERADOR", "EMPEZADO", "EMPEZAMOS", "EMPEZANDO", "EMPEZAR", "EMPEZARON", "EMPEZO", "EMPIECE", "EMPIECES", "EMPIEZA", "EMPIEZO", "EMPLEADO", "EMPLEADOS", "EMPLEO", "EMPRESA", "ENAMORADA", "ENAMORADO", "ENANO", "ENCANTA", "ENCANTADA", "ENCANTADO", "ENCANTADOR", "ENCANTADORA", "ENCANTAN", "ENCANTARIA", "ENCANTO", "ENCARGADO", "ENCARGARE", "ENCARGO", "ENCERRADO", "ENCIENDE", "ENCIMA", "ENCONTRADO", "ENCONTRAMOS", "ENCONTRAR", "ENCONTRAREMOS", "ENCONTRARLA", "ENCONTRARLO", "ENCONTRARME", "ENCONTRARON", "ENCONTRARA", "ENCONTRARAN", "ENCONTRARAS", "ENCONTRARE", "ENCONTRASTE", "ENCONTREMOS", "ENCONTRE", "ENCONTRO", "ENCUENTRA", "ENCUENTRAN", "ENCUENTRAS", "ENCUENTRE", "ENCUENTREN", "ENCUENTRO", "ENEMIGO", "ENEMIGOS", "ENERGIA", "ENFADADO", "ENFERMA", "ENFERMEDAD", "ENFERMERA", "ENFERMO", "ENFRENTAR", "ENFRENTE", "ENGAÑO", "ENOJADA", "ENOJADO", "ENORME", "ENSAYO", "ENSEGUIDA", "ENSEÑA", "ENSEÑAR", "ENSEÑARTE", "ENSEÑARE", "ENSEÑO", "ENTENDER", "ENTENDERLO", "ENTENDIDO", "ENTENDISTE", "ENTENDI", "ENTERA", "ENTERO", "ENTERPRISE", "ENTERRADO", "ENTIENDE", "ENTIENDEN", "ENTIENDES", "ENTIENDO", "ENTONCES", "ENTRA", "ENTRADA", "ENTRADAS", "ENTRADO", "ENTRAMOS", "ENTRANDO", "ENTRAR", "ENTRAS", "ENTRE", "ENTREGA", "ENTREGAR", "ENTREN", "ENTRENADOR", "ENTRENAMIENTO", "ENTREVISTA", "ENTRO", "ENTRE", "ENTRO", "ENVIADO", "ENVIAR", "ENVIARON", "ENVIARE", "ENVIE", "ENVIO", "ENVIA", "EPISODIO", "EQUIPAJE", "EQUIPO", "EQUIPOS", "EQUIVOCADA", "EQUIVOCADO", "EQUIVOCAS", "EQUIVOQUE", "ERA", "ERAN", "ERAS", "ERES", "ERIC", "ERROR", "ERRORES", "ESA", "ESAS", "ESCALA", "ESCALERA", "ESCALERAS", "ESCAPADO", "ESCAPAR", "ESCAPE", "ESCAPO", "ESCENA", "ESCENARIO", "ESCLAVOS", "ESCOGER", "ESCONDE", "ESCONDIDO", "ESCRIBE", "ESCRIBIENDO", "ESCRIBIR", "ESCRIBIO", "ESCRIBI", "ESCRITO", "ESCRITOR", "ESCRITORIO", "ESCUADRON", "ESCUCHA", "ESCUCHADO", "ESCUCHAN", "ESCUCHANDO", "ESCUCHAR", "ESCUCHARME", "ESCUCHAS", "ESCUCHASTE", "ESCUCHE", "ESCUCHEN", "ESCUCHO", "ESCUCHE", "ESCUDO", "ESCUELA", "ESCUCHAME", "ESE", "ESFUERZO", "ESO", "ESOS", "ESPACIAL", "ESPACIO", "ESPADA", "ESPALDA", "ESPALDAS", "ESPAÑOL", "ESPECIAL", "ESPECIALES", "ESPECIALMENTE", "ESPECIE", "ESPECTACULO", "ESPEJO", "ESPERA", "ESPERABA", "ESPERABAS", "ESPERADO", "ESPERAMOS", "ESPERAN", "ESPERANDO", "ESPERANZA", "ESPERANZAS", "ESPERAR", "ESPERAREMOS", "ESPERARE", "ESPERAS", "ESPERE", "ESPEREMOS", "ESPEREN", "ESPERO", "ESPIRITUAL", "ESPOSA", "ESPOSAS", "ESPOSO", "ESPERAME", "ESPIA", "ESPIRITU", "ESPIRITUS", "ESQUINA", "ESTA", "ESTABA", "ESTABAMOS", "ESTABAN", "ESTABAS", "ESTABLE", "ESTACIONAMIENTO", "ESTACION", "ESTADO", "ESTADOS", "ESTADOUNIDENSE", "ESTAMOS", "ESTAN", "ESTANDO", "ESTAR", "ESTAREMOS", "ESTARLO", "ESTARA", "ESTARAN", "ESTARAS", "ESTARE", "ESTARIA", "ESTARIAMOS", "ESTARIAN", "ESTARIAS", "ESTAS", "ESTATUA", "ESTE", "ESTELAR", "ESTEMOS", "ESTILO", "ESTO", "ESTOS", "ESTOY", "ESTRELLA", "ESTRELLAS", "ESTRUCTURA", "ESTUDIANTE", "ESTUDIANTES", "ESTUDIAR", "ESTUDIO", "ESTUDIOS", "ESTUPENDO", "ESTUPIDEZ", "ESTUVE", "ESTUVIERA", "ESTUVIERAS", "ESTUVIERON", "ESTUVIMOS", "ESTUVISTE", "ESTUVO", "ESTA", "ESTABAMOS", "ESTAIS", "ESTAN", "ESTAS", "ESTE", "ESTEN", "ESTES", "ESTOMAGO", "ESTUPIDA", "ESTUPIDO", "ESTUPIDOS", "ETERNA", "ETERNIDAD", "ETHAN", "EUROPA", "EVAN", "EVIDENCIA", "EVITAR", "EVITARLO", "EXACTAMENTE", "EXACTO", "EXAMEN", "EXCELENCIA", "EXCELENTE", "EXCEPTO", "EXCUSA", "EXISTE", "EXISTEN", "EXISTENCIA", "EXPEDIENTE", "EXPEDIENTES", "EXPERIENCIA", "EXPERIMENTO", "EXPERTO", "EXPLICA", "EXPLICACION", "EXPLICAR", "EXPLOSIVOS", "EXPLOSION", "EXPLOTAR", "EXPOSICION", "EXPRESION", "EXTERIOR", "EXTRA", "EXTRANJERO", "EXTRAORDINARIO", "EXTRAÑA", "EXTRAÑAS", "EXTRAÑO", "EXTRAÑOS", "EXTREMADAMENTE", "EXTREMO", "FABULOSO", "FACIL", "FALLA", "FALSA", "FALSO", "FALTA", "FALTAN", "FAMA", "FAMILIA", "FAMILIAR", "FAMILIARES", "FAMILIAS", "FAMOSA", "FAMOSO", "FANTASMA", "FANTASMAS", "FANTASTICA", "FANTASTICO", "FASCINANTE", "FASE", "FATAL", "FAVOR", "FAVORITA", "FAVORITO", "FBI", "FEA", "FECHA", "FEDERAL", "FEDERALES", "FELICES", "FELICIDAD", "FELICIDADES", "FELICITACIONES", "FELIZ", "FENOMENO", "FEO", "FIANZA", "FIEBRE", "FIEL", "FIESTA", "FIESTAS", "FIGURA", "FILA", "FIN", "FINAL", "FINALES", "FINALMENTE", "FIONA", "FIRMA", "FIRMAR", "FIRME", "FISCAL", "FLOR", "FLORES", "FLORIDA", "FLOTA", "FOGG", "FONDO", "FONDOS", "FORMA", "FORMACION", "FORMAR", "FORMAS", "FORTALEZA", "FORTUNA", "FOTO", "FOTOGRAFIA", "FOTOGRAFIAS", "FOTOS", "FOX", "FRACASO", "FRANCAMENTE", "FRANCESA", "FRANCESES", "FRANCIA", "FRANCISCO", "FRANCES", "FRANK", "FRANKIE", "FRASE", "FRECUENCIA", "FRED", "FREDDY", "FRENTE", "FRESCO", "FRODO", "FRONTERA", "FRIA", "FRIO", "FUE", "FUEGO", "FUENTE", "FUENTES", "FUERA", "FUERAN", "FUERAS", "FUERON", "FUERTE", "FUERTES", "FUERZA", "FUERZAS", "FUESE", "FUI", "FUIMOS", "FUISTE", "FUMAR", "FUNCIONA", "FUNCIONAN", "FUNCIONANDO", "FUNCIONAR", "FUNCIONARA", "FUNCIONE", "FUNCIONO", "FUNCION", "FUNERAL", "FURIA", "FURIOSO", "FUSION", "FUTURO", "FUE", "FABRICA", "FACIL", "FACILMENTE", "FIJATE", "FISICA", "FUTBOL", "GABRIELLE", "GAFAS", "GALLETAS", "GALLINA", "GANA", "GANADO", "GANADOR", "GANAMOS", "GANANDO", "GANAR", "GANAS", "GANASTE", "GANDALF", "GANE", "GANO", "GANE", "GANO", "GARAJE", "GARFIELD", "GARGANTA", "GARY", "GAS", "GASOLINA", "GASTOS", "GATILLO", "GATITO", "GATO", "GATOS", "GAY", "GENERACION", "GENERAL", "GENERALMENTE", "GENEROSO", "GENIAL", "GENIO", "GENTE", "GEORGE", "GERENTE", "GIGANTE", "GIMNASIO", "GIRA", "GLOBAL", "GLOBO", "GLORIA", "GOBERNADOR", "GOBIERNO", "GOLF", "GOLPE", "GOLPEAR", "GOLPES", "GOLPEO", "GORDA", "GORDO", "GORDON", "GRACE", "GRACIA", "GRACIAS", "GRACIOSO", "GRADO", "GRADOS", "GRADUACION", "GRAN", "GRANDE", "GRANDES", "GRANDIOSO", "GRANJA", "GRANO", "GRANT", "GRASA", "GRATIS", "GRAVE", "GRAVEDAD", "GRAVES", "GRECIA", "GREEN", "GREENE", "GREG", "GRIAL", "GRIEGOS", "GRIS", "GRITANDO", "GRITAR", "GRITOS", "GRUPO", "GRUPOS", "GUANTES", "GUAPA", "GUAPO", "GUARDA", "GUARDAESPALDAS", "GUARDAR", "GUARDIA", "GUARDIAS", "GUAU", "GUERRA", "GUERRAS", "GUERRERO", "GUERREROS", "GUITARRA", "GUION", "GUSANO", "GUSTA", "GUSTABA", "GUSTADO", "GUSTAN", "GUSTAR", "GUSTARIA", "GUSTARA", "GUSTARIA", "GUSTAS", "GUSTE", "GUSTO", "GUSTO", "GUIA", "HA", "HABER", "HABERLA", "HABERLE", "HABERLO", "HABERME", "HABERSE", "HABERTE", "HABIA", "HABIDO", "HABILIDAD", "HABILIDADES", "HABITACIONES", "HABITACION", "HABLA", "HABLABA", "HABLADO", "HABLAMOS", "HABLAN", "HABLANDO", "HABLAR", "HABLAREMOS", "HABLARLE", "HABLARME", "HABLARTE", "HABLARE", "HABLAS", "HABLASTE", "HABLE", "HABLEMOS", "HABLES", "HABLO", "HABLE", "HABLO", "HABRA", "HABRAN", "HABRIA", "HABRIAN", "HABRIAS", "HABEIS", "HABIA", "HABIAMOS", "HABIAN", "HABIAS", "HACE", "HACEMOS", "HACEN", "HACER", "HACERLA", "HACERLE", "HACERLO", "HACERME", "HACERNOS", "HACERSE", "HACERTE", "HACES", "HACIA", "HACIENDO", "HACIA", "HACIAN", "HACIAS", "HAGA", "HAGAMOS", "HAGAN", "HAGAS", "HAGO", "HAGAMOSLO", "HALL", "HALLAR", "HAMBRE", "HAN", "HANK", "HANNAH", "HARE", "HAREMOS", "HAROLD", "HARRIS", "HARRY", "HARTO", "HARA", "HARAN", "HARAS", "HARE", "HARIA", "HARIAS", "HAS", "HASTA", "HAY", "HAYA", "HAYAMOS", "HAYAN", "HAYAS", "HAZ", "HAZLO", "HAZME", "HEATHER", "HECHA", "HECHIZO", "HECHO", "HECHOS", "HELADO", "HELEN", "HELENA", "HELICOPTERO", "HEMORRAGIA", "HEMOS", "HENRY", "HERIDA", "HERIDAS", "HERIDO", "HERIDOS", "HERMANA", "HERMANAS", "HERMANO", "HERMANOS", "HERMOSA", "HERMOSAS", "HERMOSO", "HEROINA", "HEY", "HICE", "HICIERA", "HICIERAS", "HICIERON", "HICIMOS", "HICISTE", "HIELO", "HIERBA", "HIERRO", "HIJA", "HIJAS", "HIJO", "HIJOS", "HILL", "HISTORIA", "HISTORIAL", "HISTORIAS", "HITLER", "HIZO", "HOGAR", "HOJA", "HOLA", "HOLLY", "HOLLYWOOD", "HOMBRE", "HOMBRES", "HOMBRO", "HOMICIDIO", "HONESTAMENTE", "HONESTO", "HONG", "HONOR", "HORA", "HORARIO", "HORAS", "HORRIBLE", "HOSPITAL", "HOTEL", "HOUSTON", "HOWARD", "HOY", "HOYO", "HUBIERA", "HUBIERAN", "HUBIERAS", "HUBIESE", "HUBO", "HUELE", "HUELLAS", "HUESO", "HUESOS", "HUEVO", "HUEVOS", "HUH", "HUIR", "HUMANA", "HUMANIDAD", "HUMANO", "HUMANOS", "HUMO", "HUMOR", "HABLAME", "HAGALO", "HEROE", "HEROES", "HIGADO", "IA", "IAS", "IBA", "IBAN", "IBAS", "IDEA", "IDEAL", "IDEAS", "IDENTIDAD", "IDENTIFICACION", "IDIOTA", "IDIOTAS", "IDO", "IGLESIA", "IGUAL", "IGUALES", "IGUALMENTE", "ILEGAL", "IMAGEN", "IMAGINA", "IMAGINACION", "IMAGINAR", "IMAGINAS", "IMAGINO", "IMAGINE", "IMBECIL", "IMPACTO", "IMPERIO", "IMPORTA", "IMPORTAN", "IMPORTANCIA", "IMPORTANTE", "IMPORTANTES", "IMPORTAR", "IMPORTARIA", "IMPOSIBLE", "IMPRESIONANTE", "IMPRESION", "IMPUESTOS", "IMAGENES", "INCENDIO", "INCIDENTE", "INCLUSO", "INCLUYENDO", "INCONSCIENTE", "INCREIBLE", "INCREIBLE", "INDIA", "INDICA", "INDIOS", "INDUSTRIA", "INFARTO", "INFECCION", "INFELIZ", "INFIERNO", "INFLUENCIA", "INFORMACION", "INFORMADO", "INFORME", "INFORMES", "INGLATERRA", "INGLESES", "INGLES", "INMEDIATAMENTE", "INMEDIATO", "INOCENTE", "INOCENTES", "INSPECTOR", "INSTANTE", "INSTINTO", "INSTITUTO", "INSTRUCCIONES", "INTELIGENCIA", "INTELIGENTE", "INTENCIONES", "INTENCION", "INTENTA", "INTENTABA", "INTENTADO", "INTENTAMOS", "INTENTANDO", "INTENTAR", "INTENTARLO", "INTENTARE", "INTENTAS", "INTENTE", "INTENTO", "INTENTE", "INTENTO", "INTERESA", "INTERESADO", "INTERESANTE", "INTERESES", "INTERIOR", "INTERNACIONAL", "INTERNET", "INTERRUMPIR", "INTERES", "INVESTIGACION", "INVESTIGANDO", "INVESTIGAR", "INVIERNO", "INVISIBLE", "INVITACION", "INVITADO", "INVITADOS", "INVITO", "INVOLUCRADO", "INUTIL", "IOS", "IRA", "IRAK", "IREMOS", "IRME", "IRNOS", "IRSE", "IRTE", "IRA", "IRAN", "IRAS", "IRE", "IRIA", "ISLA", "ITALIA", "ITALIANO", "IZQUIERDA", "IZQUIERDO", "JACK", "JACKIE", "JACKSON", "JAKE", "JAMES", "JAMAS", "JANE", "JAPONESES", "JAPONES", "JAPON", "JARDIN", "JASON", "JAULA", "JAZZ", "JEAN", "JEDI", "JEFE", "JEFF", "JENNA", "JENNIFER", "JENNY", "JERRY", "JERSEY", "JESSE", "JESSICA", "JESUCRISTO", "JESUS", "JESUS", "JILL", "JIM", "JIMMY", "JODER", "JODIDA", "JODIDO", "JOE", "JOEL", "JOEY", "JOHN", "JOHNNY", "JOHNSON", "JON", "JONATHAN", "JONES", "JORDAN", "JOSEPH", "JOSH", "JOSE", "JOVEN", "JOVENCITA", "JOYAS", "JUAN", "JUDIO", "JUDIOS", "JUEGA", "JUEGAS", "JUEGO", "JUEGOS", "JUEVES", "JUEZ", "JUGADA", "JUGADOR", "JUGADORES", "JUGAMOS", "JUGANDO", "JUGAR", "JUGO", "JUGUETE", "JUGUETES", "JUICIO", "JULIA", "JULIE", "JULIO", "JUNIO", "JUNIOR", "JUNTA", "JUNTAS", "JUNTO", "JUNTOS", "JURADO", "JURO", "JUSTICIA", "JUSTO", "JUVENTUD", "JODETE", "JOVENES", "KANE", "KAREN", "KARL", "KATE", "KATIE", "KELLY", "KEN", "KENT", "KEVIN", "KILOS", "KILOMETROS", "KIM", "KING", "KIRK", "KONG", "KYLE", "LA", "LABIOS", "LABORATORIO", "LADEN", "LADO", "LADOS", "LADRONES", "LADRON", "LADY", "LAGO", "LAMENTO", "LANA", "LANE", "LANNING", "LANZA", "LANZAMIENTO", "LANZAR", "LARGA", "LARGAS", "LARGO", "LARRY", "LAS", "LASTIMAR", "LATA", "LAURA", "LAVAR", "LEALTAD", "LECCION", "LECHE", "LECTURA", "LEE", "LEER", "LEGAL", "LEJOS", "LENGUA", "LENGUAJE", "LENNY", "LENTAMENTE", "LENTO", "LEO", "LES", "LETRA", "LETRAS", "LEVANTA", "LEVANTAR", "LEVANTE", "LEVANTATE", "LEWIS", "LEX", "LEY", "LEYENDA", "LEYENDO", "LEYES", "LEI", "LEIDO", "LEON", "LIBERTAD", "LIBRAS", "LIBRE", "LIBRES", "LIBRO", "LIBROS", "LICENCIA", "LIGA", "LIMPIA", "LIMPIAR", "LIMPIEZA", "LIMPIO", "LINDA", "LINDO", "LINEA", "LIONEL", "LISA", "LISTA", "LISTAS", "LISTO", "LISTOS", "LIZ", "LLAMA", "LLAMABA", "LLAMADA", "LLAMADAS", "LLAMADO", "LLAMAMOS", "LLAMAN", "LLAMANDO", "LLAMAR", "LLAMARLO", "LLAMARME", "LLAMARON", "LLAMARTE", "LLAMARE", "LLAMAS", "LLAMASTE", "LLAME", "LLAMEN", "LLAMES", "LLAMO", "LLAME", "LLAMO", "LLAVE", "LLAVES", "LLEGA", "LLEGADA", "LLEGADO", "LLEGAMOS", "LLEGAN", "LLEGANDO", "LLEGAR", "LLEGARA", "LLEGAREMOS", "LLEGARON", "LLEGARA", "LLEGAS", "LLEGASTE", "LLEGO", "LLEGUE", "LLEGUEMOS", "LLEGUEN", "LLEGUES", "LLEGUE", "LLEGO", "LLENA", "LLENO", "LLEVA", "LLEVABA", "LLEVADO", "LLEVAMOS", "LLEVAN", "LLEVANDO", "LLEVAR", "LLEVAREMOS", "LLEVARLA", "LLEVARLO", "LLEVARME", "LLEVARON", "LLEVARTE", "LLEVARA", "LLEVARE", "LLEVAS", "LLEVE", "LLEVEN", "LLEVO", "LLEVE", "LLEVO", "LLORANDO", "LLORAR", "LLORES", "LLUVIA", "LLAMAME", "LLEVAME", "LLEVATE", "LOBO", "LOBOS", "LOCA", "LOCAL", "LOCO", "LOCOS", "LOCURA", "LOGAN", "LOGRADO", "LOGRAMOS", "LOGRAR", "LOGRARLO", "LOGRASTE", "LOGRO", "LOGRO", "LOIS", "LONDRES", "LORD", "LOS", "LOU", "LOUIS", "LOUISE", "LUCAS", "LUCE", "LUCES", "LUCHA", "LUCHANDO", "LUCHAR", "LUCY", "LUEGO", "LUGAR", "LUGARES", "LUKE", "LUNA", "LUNES", "LUTHER", "LUTHOR", "LUZ", "LAGRIMAS", "LARGATE", "LASTIMA", "LIDER", "LIMITE", "LIMITES", "LINEA", "LINEAS", "LIO", "LOGICA", "MA", "MAC", "MADAME", "MADERA", "MADRE", "MADRES", "MAESTRA", "MAESTRO", "MAGGIE", "MAGIA", "MAGNIFICO", "MAGO", "MAJESTAD", "MAL", "MALA", "MALAS", "MALDAD", "MALDICION", "MALDICION", "MALDITA", "MALDITAS", "MALDITO", "MALDITOS", "MALETA", "MALETAS", "MALETIN", "MALO", "MALOS", "MALVADO", "MAMA", "MAMI", "MAMA", "MANDA", "MANDAR", "MANDO", "MANDO", "MANEJA", "MANEJAR", "MANERA", "MANERAS", "MANO", "MANOS", "MANTENER", "MANTENGA", "MANTENGAN", "MANTENTE", "MANTIENE", "MANTEN", "MANUAL", "MANZANA", "MAPA", "MAQUILLAJE", "MAR", "MARAVILLA", "MARAVILLOSA", "MARAVILLOSO", "MARCA", "MARCAS", "MARCHA", "MARCO", "MARCUS", "MARGARET", "MARICA", "MARICON", "MARIDO", "MARIE", "MARIHUANA", "MARINA", "MARISSA", "MARK", "MARTES", "MARTHA", "MARTIN", "MARTY", "MARY", "MARIA", "MAS", "MASA", "MASAJE", "MATA", "MATADO", "MATAMOS", "MATAN", "MATANDO", "MATAR", "MATARLO", "MATARLOS", "MATARME", "MATARNOS", "MATARON", "MATARTE", "MATARA", "MATARAN", "MATARE", "MATARIA", "MATAS", "MATASTE", "MATE", "MATEN", "MATERIAL", "MATES", "MATO", "MATRIMONIO", "MATT", "MATTHEW", "MATE", "MATO", "MAX", "MAYO", "MAYOR", "MAYORES", "MAYORIA", "MAIZ", "MAÑANA", "MCDONALDS", "MEDALLA", "MEDIA", "MEDIANOCHE", "MEDIAS", "MEDICINA", "MEDICINAS", "MEDIDA", "MEDIDAS", "MEDIO", "MEDIODIA", "MEDIOS", "MEGAN", "MEI", "MEJOR", "MEJORAR", "MEJORES", "MEMORIA", "MENCIONAR", "MENOR", "MENOS", "MENSAJE", "MENSAJES", "MENTAL", "MENTE", "MENTES", "MENTIR", "MENTIRA", "MENTIRAS", "MENTIROSO", "MENUDO", "MERCADO", "MERECE", "MERECES", "MEREZCO", "MES", "MESA", "MESES", "META", "METAL", "METAS", "METE", "METER", "METERTE", "METES", "METIDO", "METIO", "METRO", "METROS", "METI", "MIA", "MIAMI", "MICHAEL", "MICHELLE", "MICKEY", "MIEDO", "MIEL", "MIEMBRO", "MIEMBROS", "MIENTE", "MIENTRAS", "MIERDA", "MIKE", "MIL", "MILAGRO", "MILES", "MILITAR", "MILITARES", "MILLAS", "MILLER", "MILLONES", "MILLON", "MINA", "MINAS", "MINISTRO", "MINTIENDO", "MINUTO", "MINUTOS", "MIO", "MIRA", "MIRABA", "MIRAD", "MIRADA", "MIRANDA", "MIRANDO", "MIRAR", "MIRAS", "MIRE", "MIREN", "MIRES", "MIRO", "MIRE", "MIS", "MISERABLE", "MISILES", "MISION", "MISMA", "MISMAS", "MISMO", "MISMOS", "MISS", "MISTERIO", "MITAD", "MITCH", "MIERCOLES", "MODA", "MODALES", "MODELO", "MODO", "MODOS", "MOLESTA", "MOLESTAR", "MOLESTE", "MOLESTES", "MOLESTIA", "MOLESTO", "MOLLY", "MOMENTO", "MOMENTOS", "MONEDA", "MONEDAS", "MONJE", "MONO", "MONSTRUO", "MONSTRUOS", "MONTAR", "MONTAÑA", "MONTAÑAS", "MONTE", "MONTON", "MORAL", "MORFINA", "MORGAN", "MORIR", "MORIREMOS", "MORIRA", "MORIRAS", "MORRIS", "MORTAL", "MOSCU", "MOSTRAR", "MOSTRARTE", "MOSTRARE", "MOTEL", "MOTIVO", "MOTIVOS", "MOTO", "MOTOR", "MOTORES", "MOVER", "MOVERSE", "MOVIENDO", "MOVIMIENTO", "MOVIMIENTOS", "MUCHA", "MUCHACHA", "MUCHACHO", "MUCHACHOS", "MUCHAS", "MUCHO", "MUCHOS", "MUCHISIMO", "MUELLE", "MUERA", "MUERE", "MUEREN", "MUERES", "MUERO", "MUERTA", "MUERTE", "MUERTES", "MUERTO", "MUERTOS", "MUESTRA", "MUESTRAS", "MUEVA", "MUEVAN", "MUEVAS", "MUEVE", "MUJER", "MUJERES", "MULDER", "MUNDIAL", "MUNDO", "MUNICIONES", "MURIENDO", "MURIERON", "MURIO", "MURO", "MURPHY", "MUSEO", "MUTANTES", "MUY", "MUESTRAME", "MUEVANSE", "MUEVETE", "MUÑECA", "MYERS", "MAQUINA", "MAQUINAS", "MAS", "MASCARA", "MATALO", "MAXIMA", "MAXIMO", "MEDICA", "MEDICO", "MEDICOS", "METETE", "MEXICO", "MIA", "MIAS", "MINIMO", "MIO", "MIOS", "MIRALO", "MIRAME", "MIRATE", "MONICA", "MOVIL", "MUSICA", "NACIDO", "NACIMIENTO", "NACIONAL", "NACIO", "NACION", "NACI", "NADA", "NADAR", "NADIE", "NANCY", "NAPOLEON", "NARANJA", "NARIZ", "NATHAN", "NATURAL", "NATURALEZA", "NATURALMENTE", "NAVE", "NAVES", "NAVIDAD", "NAVORSKI", "NECESARIO", "NECESIDAD", "NECESIDADES", "NECESITA", "NECESITABA", "NECESITAMOS", "NECESITAN", "NECESITAR", "NECESITAREMOS", "NECESITARE", "NECESITAS", "NECESITE", "NECESITO", "NEGATIVO", "NEGOCIAR", "NEGOCIO", "NEGOCIOS", "NEGRA", "NEGRO", "NEGROS", "NEIL", "NENA", "NENE", "NERVIOS", "NERVIOSA", "NERVIOSO", "NEW", "NEWMAN", "NICK", "NICKY", "NIEGA", "NIEVE", "NINGUN", "NINGUNA", "NINGUNO", "NINGUN", "NIVEL", "NIVELES", "NIÑA", "NIÑAS", "NIÑERA", "NIÑO", "NIÑOS", "NOBLE", "NOCHE", "NOCHES", "NOEL", "NOMBRE", "NOMBRES", "NORMAL", "NORMALES", "NORMALMENTE", "NORMAN", "NORTE", "NOS", "NOSOTRAS", "NOSOTROS", "NOTA", "NOTADO", "NOTAS", "NOTICIA", "NOTICIAS", "NOVIA", "NOVIO", "NUBES", "NUCLEAR", "NUESTRA", "NUESTRAS", "NUESTRO", "NUESTROS", "NUEVA", "NUEVAMENTE", "NUEVAS", "NUEVE", "NUEVO", "NUEVOS", "NUMERO", "NUNCA", "NUMERO", "NUMEROS", "OBISPO", "OBJECION", "OBJETIVO", "OBJETO", "OBJETOS", "OBRA", "OBRAS", "OBSERVANDO", "OBTENER", "OBVIAMENTE", "OBVIO", "OCASION", "OCHO", "OCTUBRE", "OCULTAR", "OCUPADA", "OCUPADO", "OCUPADOS", "OCURRA", "OCURRE", "OCURRIDO", "OCURRIENDO", "OCURRIR", "OCURRIO", "OCEANO", "ODIA", "ODIAS", "ODIE", "ODIO", "OESTE", "OFERTA", "OFICIAL", "OFICIALES", "OFICIALMENTE", "OFICINA", "OFRECE", "OIDO", "OIGA", "OIGAN", "OIGO", "OIR", "OJALA", "OJO", "OJOS", "OKAY", "OLIVER", "OLOR", "OLVIDA", "OLVIDADO", "OLVIDAR", "OLVIDARE", "OLVIDASTE", "OLVIDE", "OLVIDES", "OLVIDO", "OLVIDE", "OLVIDO", "OLVIDALO", "OLVIDATE", "ONCE", "ONDA", "OPCIONES", "OPCION", "OPERACIONES", "OPERACION", "OPINAS", "OPINION", "OPORTUNIDAD", "ORDEN", "ORDENES", "ORDENO", "ORDENO", "OREJA", "OREJAS", "ORGANIZACION", "ORGULLO", "ORGULLOSA", "ORGULLOSO", "ORGULLOSOS", "ORIGEN", "ORIGINAL", "ORO", "OSCAR", "OSCURIDAD", "OSCURO", "OSO", "OTRA", "OTRAS", "OTRO", "OTROS", "OTTO", "OXIGENO", "OYE", "OYEN", "OYERON", "OYES", "OYO", "OI", "OIDO", "OIDOS", "OIR", "OIRLO", "OIRME", "OISTE", "PACIENCIA", "PACIENTE", "PACIENTES", "PADRE", "PADRES", "PAGA", "PAGADO", "PAGAN", "PAGAR", "PAGARA", "PAGARE", "PAGO", "PAGUE", "PAGO", "PAIGE", "PALABRA", "PALABRAS", "PALACIO", "PALIZA", "PALO", "PAM", "PAN", "PANDILLA", "PANTALLA", "PANTALONES", "PAPA", "PAPAS", "PAPEL", "PAPELES", "PAPI", "PAPA", "PAQUETE", "PAR", "PARA", "PARADA", "PARADO", "PARAR", "PARAISO", "PARE", "PARECE", "PARECEN", "PARECER", "PARECES", "PARECIDO", "PARECIO", "PARECIA", "PARED", "PAREDES", "PAREJA", "PAREN", "PARES", "PAREZCA", "PAREZCO", "PARIS", "PARK", "PARKER", "PARQUE", "PARTE", "PARTES", "PARTICULAR", "PARTIDA", "PARTIDO", "PARTIR", "PARIS", "PASA", "PASABA", "PASADA", "PASADO", "PASAJE", "PASAJEROS", "PASAMOS", "PASAN", "PASANDO", "PASAPORTE", "PASAR", "PASARA", "PASARON", "PASARA", "PASARIA", "PASAS", "PASASTE", "PASE", "PASEAR", "PASEN", "PASEO", "PASES", "PASILLO", "PASION", "PASO", "PASOS", "PASTA", "PASTEL", "PASTILLAS", "PASTOR", "PASE", "PASO", "PATA", "PATAS", "PATIO", "PATO", "PATRICK", "PATRULLA", "PATRON", "PATETICO", "PAUL", "PAYASO", "PAZ", "PAIS", "PAISES", "PECADO", "PECADOS", "PECES", "PECHO", "PEDAZO", "PEDAZOS", "PEDIDO", "PEDIR", "PEDIRLE", "PEDIRTE", "PEDIRE", "PEDISTE", "PEDRO", "PEDI", "PELEA", "PELEANDO", "PELEAR", "PELEAS", "PELIGRO", "PELIGROSA", "PELIGROSO", "PELO", "PELOTA", "PELOTAS", "PELICULA", "PELICULAS", "PENA", "PENDEJO", "PENE", "PENSABA", "PENSABAS", "PENSADO", "PENSAMIENTO", "PENSAMIENTOS", "PENSAMOS", "PENSANDO", "PENSAR", "PENSARLO", "PENSASTE", "PENSE", "PENSE", "PENSO", "PEOR", "PEORES", "PEQUEÑA", "PEQUEÑAS", "PEQUEÑO", "PEQUEÑOS", "PERDEDOR", "PERDEMOS", "PERDER", "PERDIDA", "PERDIDO", "PERDIDOS", "PERDIENDO", "PERDIERON", "PERDIMOS", "PERDISTE", "PERDIO", "PERDONA", "PERDONE", "PERDI", "PERDON", "PERDONAME", "PERDONEME", "PERFECTA", "PERFECTAMENTE", "PERFECTO", "PERIODISTA", "PERIODICO", "PERIODICOS", "PERMANECER", "PERMISO", "PERMITE", "PERMITIR", "PERMITIRE", "PERMITAME", "PERO", "PERRA", "PERRITO", "PERRO", "PERROS", "PERSONA", "PERSONAJE", "PERSONAL", "PERSONALES", "PERSONALIDAD", "PERSONALMENTE", "PERSONAS", "PERTENECE", "PESADILLA", "PESADILLAS", "PESADO", "PESAR", "PESCADO", "PESO", "PETE", "PETER", "PETROLEO", "PEZ", "PHIL", "PHILIP", "PHOEBE", "PIANO", "PICO", "PIDE", "PIDIENDO", "PIDIO", "PIDO", "PIE", "PIEDAD", "PIEDRA", "PIEDRAS", "PIEL", "PIENSA", "PIENSAN", "PIENSAS", "PIENSE", "PIENSES", "PIENSO", "PIERDAS", "PIERDE", "PIERDES", "PIERDO", "PIERNA", "PIERNAS", "PIES", "PIEZA", "PIEZAS", "PILOTO", "PILOTOS", "PINTA", "PINTURA", "PIPER", "PIRATA", "PIRAMIDE", "PISCINA", "PISO", "PISTA", "PISTAS", "PISTOLA", "PISTOLAS", "PIZZA", "PIENSALO", "PLACA", "PLACER", "PLAN", "PLANEADO", "PLANEANDO", "PLANES", "PLANETA", "PLANO", "PLANOS", "PLANTA", "PLATA", "PLATAFORMA", "PLATO", "PLATOS", "PLAYA", "PLAZA", "PLASTICO", "POBRE", "POBRES", "POCA", "POCAS", "POCION", "POCO", "POCOS", "PODAMOS", "PODEMOS", "PODER", "PODERES", "PODEROSA", "PODEROSO", "PODIDO", "PODREMOS", "PODRIA", "PODRA", "PODRAN", "PODRAS", "PODRE", "PODRIA", "PODRIAMOS", "PODRIAN", "PODRIAS", "PODEIS", "PODIA", "PODIAMOS", "PODIAN", "PODIAS", "POEMA", "POLI", "POLICIA", "POLICIAL", "POLICIA", "POLICIAS", "POLLO", "POLLY", "POLVO", "POLITICA", "POLITICO", "PON", "PONDRA", "PONDRE", "PONE", "PONEMOS", "PONEN", "PONER", "PONERLE", "PONERLO", "PONERME", "PONERSE", "PONERTE", "PONES", "PONGA", "PONGAN", "PONGAS", "PONGO", "PONIENDO", "PONLO", "PONTE", "POPULAR", "POQUITO", "POR", "PORQUE", "PORQUERIA", "PORQUE", "PORTAL", "POSESION", "POSIBILIDAD", "POSIBILIDADES", "POSIBLE", "POSIBLEMENTE", "POSICIONES", "POSICION", "POSITIVO", "POTENCIA", "POTENCIAL", "POTTER", "POZO", "PRACTICAR", "PRECIO", "PRECIOSA", "PRECIOSO", "PRECISAMENTE", "PRECISO", "PREFERIRIA", "PREFIERE", "PREFIERES", "PREFIERO", "PREGUNTA", "PREGUNTABA", "PREGUNTADO", "PREGUNTANDO", "PREGUNTAR", "PREGUNTARLE", "PREGUNTARTE", "PREGUNTAS", "PREGUNTASTE", "PREGUNTE", "PREGUNTES", "PREGUNTO", "PREGUNTE", "PREGUNTO", "PREGUNTALE", "PREMIO", "PRENSA", "PREOCUPA", "PREOCUPACION", "PREOCUPADA", "PREOCUPADO", "PREOCUPARSE", "PREOCUPARTE", "PREOCUPE", "PREOCUPEN", "PREOCUPES", "PREPARA", "PREPARADA", "PREPARADO", "PREPARADOS", "PREPARANDO", "PREPARAR", "PREPAREN", "PREPARATE", "PREPARENSE", "PRESA", "PRESENCIA", "PRESENTA", "PRESENTACION", "PRESENTAR", "PRESENTE", "PRESENTIMIENTO", "PRESENTO", "PRESIDENTE", "PRESION", "PRESO", "PRESTADO", "PRIMA", "PRIMAVERA", "PRIMER", "PRIMERA", "PRIMERAS", "PRIMERO", "PRIMEROS", "PRIMO", "PRINCESA", "PRINCIPAL", "PRINCIPE", "PRINCIPIO", "PRINCIPIOS", "PRIORATO", "PRISA", "PRISIONERO", "PRISIONEROS", "PRISION", "PRIVADA", "PRIVADO", "PROBABLE", "PROBABLEMENTE", "PROBADO", "PROBAR", "PROBLEMA", "PROBLEMAS", "PROCEDIMIENTO", "PROCESO", "PRODUCCION", "PRODUCTO", "PROFESIONAL", "PROFESIONALES", "PROFESOR", "PROFUNDAMENTE", "PROFUNDO", "PROGRAMA", "PROGRAMAS", "PROGRESO", "PROHIBIDO", "PROMESA", "PROMETES", "PROMETIDO", "PROMETISTE", "PROMETIO", "PROMETO", "PROMETI", "PRONTO", "PROPIA", "PROPIAS", "PROPIEDAD", "PROPIO", "PROPIOS", "PROPUESTA", "PROPOSITO", "PROSTITUTA", "PROTECCION", "PROTEGE", "PROTEGER", "PROTEGIDO", "PROYECTO", "PRUEBA", "PRUEBAS", "PRACTICA", "PRACTICAMENTE", "PRINCIPE", "PROXIMA", "PROXIMO", "PROXIMOS", "PSIQUIATRA", "PUBLICIDAD", "PUDE", "PUDIERA", "PUDIERAS", "PUDIERON", "PUDIMOS", "PUDISTE", "PUDO", "PUEBLO", "PUEDA", "PUEDAN", "PUEDAS", "PUEDE", "PUEDEN", "PUEDES", "PUEDO", "PUENTE", "PUERTA", "PUERTAS", "PUERTO", "PUES", "PUESTA", "PUESTO", "PUESTOS", "PULMONES", "PULSO", "PUNTA", "PUNTO", "PUNTOS", "PURA", "PURO", "PUSE", "PUSIERON", "PUSISTE", "PUSO", "PUTA", "PUTAS", "PUTO", "PAGINA", "PAGINAS", "PAJARO", "PAJAROS", "PANICO", "PERDIDA", "PUBLICA", "PUBLICO", "QUE", "QUEDA", "QUEDADO", "QUEDAMOS", "QUEDAN", "QUEDAR", "QUEDARME", "QUEDARNOS", "QUEDARSE", "QUEDARTE", "QUEDARA", "QUEDARE", "QUEDAS", "QUEDATE", "QUEDE", "QUEDES", "QUEDO", "QUEDE", "QUEDO", "QUEJAS", "QUEMA", "QUEMAR", "QUEREMOS", "QUERER", "QUERIA", "QUERIDA", "QUERIDO", "QUERIDOS", "QUERRA", "QUERRAS", "QUERRIA", "QUEREIS", "QUERIA", "QUERIAMOS", "QUERIAN", "QUERIAS", "QUESO", "QUIEN", "QUIENES", "QUIERA", "QUIERAN", "QUIERAS", "QUIERE", "QUIEREN", "QUIERES", "QUIERO", "QUIETO", "QUIETOS", "QUINCE", "QUINTO", "QUIROFANO", "QUISE", "QUISIERA", "QUISIERAS", "QUISO", "QUITA", "QUITAR", "QUIZAS", "QUIZA", "QUIZAS", "QUIEN", "QUIENES", "QUE", "QUEDATE", "QUEDENSE", "QUEDESE", "QUIMICA", "QUITATE", "RACHEL", "RADAR", "RADIO", "RALPH", "RANGO", "RAPIDO", "RARA", "RARAS", "RARO", "RASTRO", "RATA", "RATAS", "RATO", "RAY", "RAYMOND", "RAYO", "RAYOS", "RAZA", "RAZON", "RAZONABLE", "RAZONES", "RAZON", "REACCION", "REAL", "REALES", "REALIDAD", "REALIZAR", "REALMENTE", "REBELDES", "RECEPCION", "RECIBE", "RECIBIDO", "RECIBIMOS", "RECIBIR", "RECIBIO", "RECIBO", "RECIBI", "RECIENTEMENTE", "RECIEN", "RECOGER", "RECOMPENSA", "RECONOCIMIENTO", "RECONOZCO", "RECORDAR", "RECUERDA", "RECUERDAS", "RECUERDE", "RECUERDEN", "RECUERDO", "RECUERDOS", "RECUPERAR", "RECURSOS", "RED", "REFERIA", "REFIERE", "REFIERES", "REFIERO", "REFUERZOS", "REFUGIO", "REGALO", "REGALOS", "REGINA", "REGISTRO", "REGISTROS", "REGLA", "REGLAS", "REGRESA", "REGRESADO", "REGRESAR", "REGRESARA", "REGRESARE", "REGRESE", "REGRESEN", "REGRESES", "REGRESO", "REGRESE", "REGRESO", "REHENES", "REINA", "REINO", "RELACIONES", "RELACION", "RELIGION", "RELOJ", "RELAJATE", "REMEDIO", "RENTA", "RENUNCIAR", "REPENTE", "REPITO", "REPORTE", "REPRESENTA", "REPRESENTANTE", "REPUTACION", "REPUBLICA", "REQUIERE", "RESCATE", "RESERVA", "RESIDENCIA", "RESISTENCIA", "RESOLVER", "RESPECTO", "RESPETO", "RESPIRA", "RESPIRACION", "RESPIRAR", "RESPONDA", "RESPONDE", "RESPONDER", "RESPONSABILIDAD", "RESPONSABLE", "RESPUESTA", "RESPUESTAS", "RESTAURANTE", "RESTO", "RESTOS", "RESULTA", "RESULTADO", "RESULTADOS", "RESULTO", "RETIRO", "RETO", "RETROCEDAN", "REUNION", "REVERENDO", "REVISA", "REVISAR", "REVISTA", "REVOLUCION", "REVES", "REY", "REYES", "REZAR", "REIR", "RICA", "RICHARD", "RICK", "RICKY", "RICO", "RICOS", "RIDDICK", "RIDICULO", "RIESGO", "RIESGOS", "RIFLE", "RISA", "RITMO", "ROB", "ROBADO", "ROBANDO", "ROBAR", "ROBARON", "ROBASTE", "ROBERT", "ROBIN", "ROBO", "ROBOT", "ROBOTS", "ROBO", "ROCA", "ROCAS", "ROCK", "ROCKY", "RODILLA", "RODILLAS", "ROGER", "ROJA", "ROJO", "ROLLO", "ROMA", "ROMANO", "ROMANOS", "ROMPE", "ROMPER", "ROMPIO", "ROMANTICO", "RON", "RONDA", "ROPA", "ROSA", "ROSAS", "ROSE", "ROSIE", "ROSS", "ROSTRO", "ROTA", "ROTO", "ROY", "RUBIA", "RUBY", "RUEDA", "RUEDAS", "RUEGO", "RUIDO", "RUMBO", "RUMOR", "RUMORES", "RUSIA", "RUSO", "RUSOS", "RUTA", "RUTINA", "RYAN", "RAPIDA", "RAPIDAMENTE", "RAPIDO", "RIO", "SABE", "SABEMOS", "SABEN", "SABER", "SABERLO", "SABES", "SABIA", "SABIDO", "SABIENDO", "SABOR", "SABREMOS", "SABRA", "SABRAN", "SABRAS", "SABRIA", "SABEIS", "SABIA", "SABIAMOS", "SABIAN", "SABIAS", "SACA", "SACADO", "SACAR", "SACARLO", "SACARON", "SACARTE", "SACARE", "SACASTE", "SACERDOTE", "SACO", "SACRIFICIO", "SACO", "SAGRADO", "SAINT", "SAL", "SALA", "SALDREMOS", "SALDRA", "SALDRE", "SALE", "SALEN", "SALES", "SALGA", "SALGAMOS", "SALGAN", "SALGAS", "SALGO", "SALIDA", "SALIDO", "SALIENDO", "SALIERON", "SALIMOS", "SALIR", "SALISTE", "SALIO", "SALLY", "SALSA", "SALTA", "SALTAR", "SALTO", "SALUD", "SALUDA", "SALUDABLE", "SALUDOS", "SALVA", "SALVADO", "SALVAJE", "SALVAJES", "SALVAR", "SALVASTE", "SALVE", "SALVO", "SALVO", "SALI", "SALIA", "SALON", "SAM", "SAMANTHA", "SAMMY", "SAMURAI", "SAN", "SANDY", "SANGRANDO", "SANGRE", "SANO", "SANTA", "SANTO", "SANTOS", "SAQUE", "SAQUEN", "SAQUE", "SARA", "SARAH", "SARGENTO", "SATISFECHO", "SATELITE", "SCOTT", "SCULLY", "SEA", "SEAMOS", "SEAN", "SEAS", "SECCION", "SECO", "SECRETA", "SECRETARIA", "SECRETARIO", "SECRETO", "SECRETOS", "SECTOR", "SECUENCIA", "SECUESTRO", "SECUNDARIA", "SED", "SEGUIDO", "SEGUIMOS", "SEGUIR", "SEGUIREMOS", "SEGUIRA", "SEGUIRE", "SEGUNDA", "SEGUNDO", "SEGUNDOS", "SEGURA", "SEGURAMENTE", "SEGURIDAD", "SEGURO", "SEGUROS", "SEGUI", "SEGUIA", "SEGUN", "SEIS", "SEIYA", "SELVA", "SEMANA", "SEMANAS", "SEMEJANTE", "SENADO", "SENADOR", "SENCILLO", "SENSACION", "SENSIBLE", "SENTADA", "SENTADO", "SENTADOS", "SENTARME", "SENTARSE", "SENTARTE", "SENTIDO", "SENTIMIENTO", "SENTIMIENTOS", "SENTIMOS", "SENTIR", "SENTIRME", "SENTIRSE", "SENTI", "SENTIA", "SEPA", "SEPAN", "SEPAS", "SEPTIEMBRE", "SER", "SERA", "SEREMOS", "SERES", "SERIA", "SERIE", "SERIO", "SERLO", "SERPIENTE", "SERPIENTES", "SERVICIO", "SERVICIOS", "SERVIR", "SERVIRA", "SERA", "SERAN", "SERAS", "SERE", "SERIA", "SERIAN", "SERIAS", "SESION", "SETH", "SEXO", "SEXUAL", "SEXY", "SEÑAL", "SEÑALES", "SEÑOR", "SEÑORA", "SEÑORAS", "SEÑORES", "SEÑORITA", "SEÑORITAS", "SEÑORIA", "SHARON", "SHAUN", "SHAW", "SHERIFF", "SHOCK", "SHOW", "SHREK", "SIDO", "SIEMPRE", "SIENDO", "SIENTA", "SIENTAS", "SIENTE", "SIENTEN", "SIENTES", "SIENTO", "SIETE", "SIGA", "SIGAMOS", "SIGAN", "SIGAS", "SIGLO", "SIGLOS", "SIGNIFICA", "SIGNIFICADO", "SIGO", "SIGUE", "SIGUEN", "SIGUES", "SIGUIENDO", "SIGUIENTE", "SIGUIO", "SILENCIO", "SILLA", "SIMON", "SIMPLE", "SIMPLEMENTE", "SIN", "SINCERO", "SINCRONIZADO", "SINO", "SIQUIERA", "SIR", "SIRVE", "SIRVEN", "SISTEMA", "SISTEMAS", "SITIO", "SITIOS", "SITUACION", "SIENTATE", "SIENTENSE", "SIENTESE", "SMALLVILLE", "SMITH", "SOBRA", "SOBRE", "SOBREVIVIR", "SOBRINO", "SOCIAL", "SOCIEDAD", "SOCIO", "SOCIOS", "SOCORRO", "SOFA", "SOIS", "SOL", "SOLA", "SOLAMENTE", "SOLAS", "SOLDADO", "SOLDADOS", "SOLITARIO", "SOLO", "SOLOS", "SOLUCION", "SOLIA", "SOMBRA", "SOMBRAS", "SOMBRERO", "SOMOS", "SON", "SONAR", "SONIDO", "SONNY", "SONRISA", "SOPA", "SOPHIE", "SOPORTAR", "SOPORTO", "SORPRENDE", "SORPRENDENTE", "SORPRENDIDO", "SORPRESA", "SOS", "SOSPECHOSO", "SOSPECHOSOS", "SOSTEN", "SOY", "SOÑANDO", "SRA", "SRTA", "STAN", "STANLEY", "STEVE", "STEVEN", "SUAVE", "SUBA", "SUBAN", "SUBE", "SUBIENDO", "SUBIR", "SUBTITULOS", "SUCEDA", "SUCEDE", "SUCEDER", "SUCEDERA", "SUCEDIDO", "SUCEDIENDO", "SUCEDIO", "SUCIA", "SUCIO", "SUELDO", "SUELO", "SUELTA", "SUELTE", "SUELTO", "SUENA", "SUERTE", "SUEÑO", "SUEÑOS", "SUFICIENTE", "SUFICIENTEMENTE", "SUFICIENTES", "SUFRIDO", "SUFRIMIENTO", "SUFRIR", "SUGIERO", "SUICIDIO", "SUJETO", "SUMMER", "SUPE", "SUPER", "SUPERFICIE", "SUPERIOR", "SUPERMAN", "SUPIERA", "SUPIERAS", "SUPISTE", "SUPO", "SUPONE", "SUPONGO", "SUPONIA", "SUPUESTO", "SUR", "SUS", "SUSAN", "SUYA", "SUYO", "SUYOS", "SUELTAME", "SYDNEY", "SABADO", "SI", "SIGANME", "SIGUEME", "SIMBOLO", "SOIO", "SOLO", "SOTANO", "SUBETE", "SUPER", "TABACO", "TAL", "TALENTO", "TALVEZ", "TAMAÑO", "TAMBIEN", "TAMBIEN", "TAMPOCO", "TAN", "TANQUE", "TANQUES", "TANTA", "TANTAS", "TANTO", "TANTOS", "TARDE", "TARDES", "TAREA", "TARJETA", "TARJETAS", "TAXI", "TAYLOR", "TAZA", "TEATRO", "TECHO", "TECNOLOGIA", "TED", "TEDDY", "TELE", "TELEFONO", "TELEVISION", "TELLY", "TELEFONO", "TELEFONOS", "TEMA", "TEMAS", "TEME", "TEMER", "TEMO", "TEMOR", "TEMPERATURA", "TEMPLO", "TEMPORADA", "TEMPORAL", "TEMPRANO", "TEN", "TENDREMOS", "TENDRA", "TENDRAN", "TENDRAS", "TENDRE", "TENDRIA", "TENDRIAMOS", "TENDRIAS", "TENEMOS", "TENER", "TENERLO", "TENERTE", "TENGA", "TENGAMOS", "TENGAN", "TENGAS", "TENGO", "TENIA", "TENIAS", "TENIDO", "TENIENDO", "TENIENTE", "TENIS", "TENSION", "TENEIS", "TENIA", "TENIAMOS", "TENIAN", "TENIAS", "TEORIA", "TERAPIA", "TERCER", "TERCERA", "TERCERO", "TERMINA", "TERMINADO", "TERMINAMOS", "TERMINAR", "TERMINE", "TERMINO", "TERMINE", "TERMINO", "TERRENO", "TERRIBLE", "TERRITORIO", "TERROR", "TERRORISTA", "TERRORISTAS", "TERRY", "TESORO", "TESTIGO", "TESTIGOS", "TETAS", "TEXAS", "THE", "THOMAS", "THUNDERBIRD", "TIBURONES", "TIBURON", "TIEMPO", "TIEMPOS", "TIENDA", "TIENE", "TIENEN", "TIENES", "TIERRA", "TIERRAS", "TIGRE", "TIM", "TINA", "TIO", "TIPO", "TIPOS", "TIRA", "TIRADO", "TIRAR", "TIRO", "TIRO", "TOALLA", "TOCA", "TOCADO", "TOCANDO", "TOCAR", "TOCO", "TODA", "TODAS", "TODAVIA", "TODAVIA", "TODO", "TODOS", "TOM", "TOMA", "TOMADO", "TOMAMOS", "TOMAN", "TOMANDO", "TOMAR", "TOMAREMOS", "TOMARON", "TOMARA", "TOMARE", "TOMAS", "TOMASTE", "TOME", "TOMEN", "TOMES", "TOMMY", "TOMO", "TOME", "TOMO", "TONO", "TONTA", "TONTERIA", "TONTERIAS", "TONTO", "TONTOS", "TONY", "TOQUE", "TOQUES", "TORMENTA", "TORNEO", "TORRE", "TOTAL", "TOTALMENTE", "TRABAJA", "TRABAJABA", "TRABAJADO", "TRABAJADORES", "TRABAJAMOS", "TRABAJAN", "TRABAJANDO", "TRABAJAR", "TRABAJAS", "TRABAJO", "TRABAJOS", "TRABAJE", "TRACY", "TRADICION", "TRADUCCION", "TRAE", "TRAEN", "TRAER", "TRAERE", "TRAES", "TRAGEDIA", "TRAGO", "TRAGOS", "TRAICION", "TRAIDOR", "TRAIGA", "TRAIGAN", "TRAIGO", "TRAJE", "TRAJERON", "TRAJISTE", "TRAJO", "TRAMPA", "TRANQUILA", "TRANQUILO", "TRANQUILOS", "TRANQUILIZATE", "TRANSMISION", "TRANSPORTE", "TRAS", "TRASERA", "TRASERO", "TRATA", "TRATABA", "TRATADO", "TRATAMIENTO", "TRATAMOS", "TRATAN", "TRATANDO", "TRATAR", "TRATARE", "TRATAS", "TRATE", "TRATO", "TRATE", "TRATO", "TRAUMA", "TRAVIS", "TRAVES", "TRAIDO", "TREINTA", "TREN", "TRENES", "TRES", "TRIBUNAL", "TRIPULACION", "TRISTE", "TRONO", "TROPAS", "TROYA", "TROZO", "TRUCO", "TRUCOS", "TRAEME", "TRAFICO", "TUBO", "TUMBA", "TURNER", "TURNO", "TUS", "TUVE", "TUVIERA", "TUVIERAS", "TUVIERON", "TUVIMOS", "TUVISTE", "TUVO", "TUYA", "TUYO", "TUYOS", "TYLER", "TECNICA", "TIA", "TIO", "TIOS", "TIPICO", "TITULO", "TOMALO", "TOMATE", "TUNEL", "UBICACION", "UDS", "ULTIMA", "ULTIMO", "UN", "UNA", "UNAS", "UNICO", "UNIDAD", "UNIDADES", "UNIDOS", "UNIFORME", "UNIVERSIDAD", "UNIVERSO", "UNION", "UNO", "UNOS", "URGENCIAS", "URGENTE", "USA", "USADO", "USAMOS", "USAN", "USANDO", "USAR", "USARLO", "USAS", "USE", "USO", "USR", "USTED", "USTEDES", "USO", "UTILIZAR", "V", "VACA", "VACACIONES", "VACAS", "VACIA", "VACIO", "VAIS", "VALE", "VALIENTE", "VALLE", "VALOR", "VAMONOS", "VAMOS", "VAMPIRO", "VAMPIROS", "VAN", "VAQUERO", "VARIAS", "VARIOS", "VAS", "VASO", "VAYA", "VAYAMOS", "VAYAN", "VAYAS", "VE", "VEA", "VEAMOS", "VEAN", "VEAS", "VECES", "VECINDARIO", "VECINO", "VECINOS", "VEGAS", "VEHICULO", "VEINTE", "VELA", "VELAS", "VELOCIDAD", "VEMOS", "VEN", "VENCIDO", "VENDE", "VENDEDOR", "VENDER", "VENDIENDO", "VENDRA", "VENDRAN", "VENDRAS", "VENDRIA", "VENENO", "VENGA", "VENGAN", "VENGANZA", "VENGAS", "VENGO", "VENIDO", "VENIMOS", "VENIR", "VENTA", "VENTAJA", "VENTANA", "VENTANAS", "VENIA", "VEO", "VER", "VERANO", "VERAS", "VERDAD", "VERDADERA", "VERDADERAMENTE", "VERDADERO", "VERDADEROS", "VERDE", "VEREMOS", "VERGÜENZA", "VERLA", "VERLE", "VERLO", "VERLOS", "VERME", "VERNOS", "VERSION", "VERTE", "VERA", "VERAN", "VERAS", "VERE", "VES", "VESTIDO", "VETE", "VEZ", "VEIA", "VIAJAR", "VIAJE", "VIAJES", "VICTORIA", "VIDA", "VIDAS", "VIDEO", "VIDRIO", "VIEJA", "VIEJAS", "VIEJO", "VIEJOS", "VIENDO", "VIENE", "VIENEN", "VIENES", "VIENTO", "VIERA", "VIERNES", "VIERON", "VIETNAM", "VIGILA", "VIGILANCIA", "VIGILANDO", "VIKTOR", "VILLA", "VIMOS", "VINCENT", "VINE", "VINIENDO", "VINIERA", "VINIERON", "VINIMOS", "VINISTE", "VINO", "VIO", "VIOLACION", "VIOLENCIA", "VIRGEN", "VIRGINIA", "VIRUS", "VISITA", "VISITAR", "VISITAS", "VISION", "VISTA", "VISTAZO", "VISTE", "VISTO", "VIVA", "VIVE", "VIVEN", "VIVES", "VIVIDO", "VIVIENDO", "VIVIMOS", "VIVIR", "VIVO", "VIVOS", "VIVIA", "VOCES", "VOLANDO", "VOLANTE", "VOLAR", "VOLUNTAD", "VOLVAMOS", "VOLVEMOS", "VOLVER", "VOLVEREMOS", "VOLVERA", "VOLVERAN", "VOLVERAS", "VOLVERE", "VOLVERIA", "VOLVIENDO", "VOLVIERON", "VOLVISTE", "VOLVIO", "VOLVI", "VOMITAR", "VOS", "VOSOTROS", "VOTO", "VOY", "VOZ", "VUELA", "VUELO", "VUELTA", "VUELTAS", "VUELTO", "VUELVA", "VUELVAN", "VUELVAS", "VUELVE", "VUELVEN", "VUELVES", "VUELVO", "VUESTRA", "VUESTRO", "VUESTROS", "VAMONOS", "VAYANSE", "VAYASE", "VIA", "VICTIMA", "VICTIMAS", "VICTOR", "WALLACE", "WALTER", "WARREN", "WASHINGTON", "WATSON", "WAYNE", "WEST", "WHISKY", "WHITE", "WILL", "WILLIAM", "WILLIAMS", "WILLIE", "WILSON", "WONG", "WOODY", "WOW", "WYATT", "XENA", "YA", "YEAH", "YENDO", "YORK", "YOU", "ZAPATO", "ZAPATOS", "ZONA", "ZORRA", "AFRICA", "ANGEL", "ANGELES", "ANIMO", "ARBOL", "ARBOLES", "AREA", "EL", "EPOCA", "ERAMOS", "ESA", "ESE", "ESTA", "ESTAS", "ESTE", "ESTO", "ESTOS", "EXITO", "IBAMOS", "ORDENES", "ORGANOS", "ULTIMA", "ULTIMAMENTE", "ULTIMAS", "ULTIMO", "ULTIMOS", "UNICA", "UNICO", "UNICOS", "UTIL"}

        palabrasCorrectas = []
        palabrasIncorrectas = []
        i = 0
        while i < len(palabras):
            if palabras[i] in diccionario and len(palabras[i])>=3:
                if palabras[i] not in palabrasCorrectas:
                    palabrasCorrectas.append(palabras[i])
                    i += 1
                else:
                    palabras.pop(i)
            else:
                palabrasIncorrectas.append(palabras.pop(i))

        return palabrasCorrectas, palabrasIncorrectas

    def finalizar_juego():
        messagebox.showinfo("Tiempo agotado", "¡El tiempo se ha agotado!")
        canvas.destroy()
        mostrar_resultados(root)

    def finalizar_entrada():
        messagebox.showinfo("Fin del juego", "¡Fin del juego!")
        canvas.destroy()
        mostrar_resultados(root)
    
    def pintar_matriz(palabra):
        palabrasValidadas = validar([palabra])
        palabrasValidadas, palabrasNoEncDicc = diccionario(palabrasValidadas)
        palabrasEncontradas, palabrasNoEncontradas, posicionesEncontradas = busquedaPalabras(sopaDeLetras, palabrasValidadas)

        for i, j in posicionesEncontradas:
            labels[(i, j)].config(bg="yellow")
        
        mensaje = ""
        for i in palabrasNoEncDicc:
            mensaje += f"{i} no está en el diccionario.\n"
        
        for i in palabrasNoEncontradas:
            mensaje += f"{i} No está en la sopa.\n"
        
        if mensaje != "":
            # Crear un label para mensaje de error (usando el canvas)
            label_mensaje = tk.Label(canvas, text=mensaje , font=("Helvetica", 12) )
            canvas.create_window(screen_width * 0.55 , screen_height * 0.85 , window=label_mensaje, anchor="center")
            

            # Programar la destrucción del label después de 2000 milisegundos (2 segundos)
            canvas.after(2000, label_mensaje.destroy)

    def agregar_palabra(event=None):
        global longitud_actual
        palabra = entry.get()
        palabras.append(palabra)
        entry.delete(0, tk.END)

        longitud_actual += len(palabra)
            
        # Concatenar todas las palabras con un espacio
        texto_concatenado = text_widget.get("1.0", tk.END).strip()
        if texto_concatenado:
            texto_concatenado += "; " + palabra
        else:
            texto_concatenado = palabra
            
        if longitud_actual >= 15:
            # Agregar nueva línea si la longitud acumulada es 15 o más
            texto_concatenado += "\n"
            longitud_actual = 0
            
        # Limpiar y actualizar el widget Text
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, texto_concatenado)

        pintar_matriz(palabra)

    def mostrar_matriz(matriz, tiempoSegundo, root):
        def update_timer():
            nonlocal tiempo_restante
            if tiempo_restante > 0:
                tiempo_restante -= 1
                minutos = tiempo_restante // 60
                segundos = tiempo_restante % 60
                timer_label.config(text=f"{minutos:02}:{segundos:02}")
                canvas.after(1000, update_timer)
            else:
                finalizar_juego()

        # Configuración del canvas
        global canvas, entry, timer_label, text_widget, longitud_actual, palabras, boton_agregar, boton_finalizar, labels

        # Configurar el canvas para que sea del mismo tamaño que la pantalla completa
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Configuración del canvas
        canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)

        palabras = []
        longitud_actual = 0

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"sopaFoto.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height-55), Image.Resampling.LANCZOS)
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
        canvas.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)

        # Crear un marco para la matriz (usando el canvas)
        frame_matriz = tk.Frame(canvas, bg='blue')
        canvas.create_window(screen_width // 2 + 300, screen_height // 2 - 30, window=frame_matriz, anchor="center")

        labels = {}
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                label = tk.Label(frame_matriz, text=matriz[i][j], borderwidth=0, relief="solid", width=7, bg="skyblue", height=3, font=("Arial Black",10) ,foreground="white")
                label.grid(row=i, column=j, padx=1, pady=1)
                labels[(i, j)] = label  
                # Guardar la referencia del label en el diccionario

        # Crear una entrada para agregar palabras
        entry = tk.Entry(canvas, width=30, font=("Cooper Black", 14), borderwidth=10)
        canvas.create_window(screen_width * 0.25, screen_height * 0.38, window=entry)
        entry.bind("<Return>", agregar_palabra)



        # Botón para agregar palabras
        boton_agregar = tk.Button(canvas, text="Ingresar", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=agregar_palabra)
        canvas.create_window(screen_width * 0.25, screen_height * 0.3, window=boton_agregar)

        # Botón para finalizar la entrada de palabras
        boton_finalizar = tk.Button(canvas, text="Finalizar", font=("Lilita One", 23), bg="white", foreground="#31CFFF", relief="flat", command=finalizar_entrada)
        canvas.create_window(screen_width * 0.383, screen_height * 0.830, window=boton_finalizar)

        # Crear un text widget para mostrar las palabras ingresadas
        text_widget = tk.Text(canvas, wrap='word', height=9, width=28, font=("Helvetica", 14), borderwidth=0)
        canvas.create_window(screen_width * 0.165, screen_height * 0.7, window=text_widget)

        # Etiqueta para mostrar el tiempo restante
        timer_label = tk.Label(canvas, text="01:00", font=("Cooper Black", 30), bg="white")
        canvas.create_window(screen_width * 0.385, screen_height * 0.61, window=timer_label)

        # Iniciar el temporizador
        tiempo_restante = tiempoSegundo
        update_timer()

        # Mantener una referencia a la imagen para evitar que sea recolectada por el GC
        canvas.image = imagen_fondo_tk

    def busquedaPalabras(sopaDeLetras, palabras):
        def busqueda(sopaletra, palabra, f, c):
            ady = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            if len(palabra) == 1:
                for b in (ady):
                    x = f + b[0]
                    y = c + b[1]
                    if 0 <= x < 10 and 0 <= y < 10:
                        if palabra == sopaletra[x][y]:
                            posicionesEncontradas.append([x,y])
                            return True
            else:
                for b in (ady):
                    x = f + b[0]
                    y = c + b[1]
                    if 0 <= x < 10 and 0 <= y < 10:
                        if palabra[0] == sopaletra[x][y]:
                            sopaletra[x][y] = 1
                            esta_palabra = busqueda(sopaletra, palabra[1:], x, y)
                            if esta_palabra:
                                posicionesEncontradas.append([x,y])
                            return esta_palabra
        
        global posicionesEncontradas
        posicionesEncontradas = []
        palabrasEncontradas = []
        palabrasNoEncontradas = []

        for i in (palabras):
            esta_palabra = False
            f = 0
            while f < 10 and not esta_palabra:
                c = 0
                while c < 10 and not esta_palabra:
                    if i[0] == sopaDeLetras[f][c]:
                        copia = copy.deepcopy(sopaDeLetras)
                        copia[f][c] = 1
                        esta_palabra = busqueda(copia, i[1:], f, c)
                        if esta_palabra:
                            posicionesEncontradas.append([f,c])
                    c += 1
                f += 1
            if esta_palabra:
                palabrasEncontradas.append(i)
            else:
                palabrasNoEncontradas.append(i)
                
        return palabrasEncontradas, palabrasNoEncontradas, posicionesEncontradas

    def puntosCorrectos(palabras):
        puntos = 0
        for i in palabras:
            puntos += len(i)*10
        return puntos

    def mostrar_resultados(root):
        def LLamar_Menu_Sopa_desde_result():
            canvas2.destroy()
            menuSopa(root)
        palabrasValidadas = validar(palabras)
        palabrasValidadas, palabrasNoEncDicc = diccionario(palabrasValidadas)
        palabrasEncontradas, palabrasNoEncontradas, posicionesEncontradas = busquedaPalabras(sopaDeLetras, palabrasValidadas)
        puntosLogrados = puntosCorrectos(palabrasEncontradas)

        #Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        #Configuración del canvas
        canvas2 = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas2.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"menu_fin_sopa_de_letra.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

        # Guardar una referencia de la imagen
        canvas2.image = imagen_fondo_tk

        # Mostrar la imagen de fondo en el canvas
        canvas2.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)

        canvas2.update()

        #####################################################################
        text_widget = tk.Text(canvas2, wrap='word', height=9, width=28, font=("Helvetica", 14), borderwidth=0)
        canvas2.create_window(screen_width * 0.165, screen_height * 0.7, window=text_widget)

        # Etiqueta para mostrar Las palabras ingresadas por el usuario
        palabrasIngresadas = "Ingresadas: "
        for i in palabras:
            palabrasIngresadas +=  i + "; "
        text_widget.insert(tk.END, palabrasIngresadas)


        # Etiqueta para mostrar Las palabras correctas ingresadas por el usuario
        palabrasIncorrectasIngresadas = "\n\nNo en diccionario: "
        for i in range(len(palabrasNoEncDicc)):
            palabrasIncorrectasIngresadas += f" {palabrasNoEncDicc[i]};"
        text_widget.insert(tk.END, palabrasIncorrectasIngresadas)

        # Etiqueta para mostrar Las palabras correctas ingresadas por el usuario
        palabrasCorrectasIngresadas = "\n\nCorrectas: "
        for i in range(len(palabrasEncontradas)):
            palabrasCorrectasIngresadas += f" {palabrasEncontradas[i]};"
        text_widget.insert(tk.END, palabrasCorrectasIngresadas)

        # Etiqueta para mostrar Las palabras correctas ingresadas por el usuario
        palabrasCorrectasNoSopa = "\n\nNo en sopa: "
        for i in range(len(palabrasNoEncontradas)):
            palabrasCorrectasNoSopa += f" {palabrasNoEncontradas[i]};"
        text_widget.insert(tk.END, palabrasCorrectasNoSopa)

        # Etiqueta para mostrar Las palabras correctas ingresadas por el usuario
        text_widget.insert(tk.END, f"\n\nPuntos Logrados: {puntosLogrados}")
        text_widget.config(state=tk.DISABLED) 


        # Crear un marco para la matriz (usando el canvas)
        frame_matriz = tk.Frame(canvas2, bg='blue')
        canvas2.create_window(screen_width // 2 + 300, screen_height // 2 - 30, window=frame_matriz, anchor="center")

        #####################################################################


        for i in range(len(sopaDeLetras)):
            for j in range(len(sopaDeLetras[i])):
                if [i,j] in posicionesEncontradas:
                    color = "yellow"
                else:
                    color = "skyblue"
                label = tk.Label(frame_matriz, text=sopaDeLetras[i][j], borderwidth=0, relief="solid", width=7, bg=color, height=3, font=("Arial Black",10) ,foreground="white")
                label.grid(row=i, column=j, padx=1, pady=1)
    
        # Crear boton para salir
        boton_salir = tk.Button(canvas2, text="Salir", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command = LLamar_Menu_Sopa_desde_result )
        canvas2.create_window(screen_width * 0.25, screen_height * 0.7, window=boton_salir)

    menuSopa(root)

  


def BatallaNaval(root):
    class Barco():
        def __init__(self, tipo, posicion, x, y):
            self.tipo = tipo
            self.posicion = posicion
            self.centro_x = x
            self.centro_y = y

            if tipo == 1:
                if posicion == 1:
                    self.matriz = [[0, - 1], [- 1, 0], [1, 0], [1, 1], [-1, 1], [0, 1], [0, 0]]
                    self.adyacentes = [[-2, -1], [-2, 0], [-2, 1], [-2, 2], [-1, -2], [-1, -1], [-1, 2], [0, -2], [0, 2],
                                        [1, -2], [1, -1], [1, 2],[2, -1], [2, 0], [2, 1], [2, 2]]

                if posicion == 2:
                    self.matriz = [[0, -1], [-1, -1], [0, 1], [-1, 1], [-1, 0], [1, 0], [0, 0]]
                    self.adyacentes = [[-2, -2], [-2, -1], [-2, 0], [-2, 2], [-2, 1], [-1, -2], [-1, 2], [0, -2], [0, 2],
                                    [1, -2], [1, -1], [1, 2], [1, 1], [2, -1], [2, 0], [2, 1]]

                if posicion == 3:
                    self.matriz = [[0, -1], [-1, 0], [0, 1], [-1, -1], [1, 0], [1, -1], [0, 0]]
                    self.adyacentes = [[-2, -1], [-2, 0], [-2, 1], [-2, -2], [-1, -2], [-1, 1], [-1, 2], [0, -2], [0, 2],
                                    [1, -2], [1, 1], [1, 2],[2, -1], [2, 0], [2, 1], [2, -2]]
                if posicion == 4:
                    self.matriz = [[0, -1], [1, 1], [0, 1], [-1, 0], [1, 0], [1, -1], [0, 0]]
                    self.adyacentes = [[-1, -1], [-2, -1], [-2, 0], [-1, 1], [-2, 1], [-1, -2], [-1, 2], [0, -2], [0, 2],
                                    [1, -2], [2, -2], [1, 2], [2, 2],[2, -1], [2, 0], [2, 1]]
            
            elif tipo == 2:
                if posicion == 1:
                    self.matriz = [[-1, 0], [-1, 1], [-1, -1], [1, 0], [1, -1], [1, 1],[0,0]]
                    self.adyacentes = [[-1, -2], [-2, -1], [-2, 0], [-2, 1], [-1, 2], [0, -1], [0, 1], [1, -2], [2, -1],
                                    [2, 0],[2, 1], [1, 2], [-2, -2], [0, -2], [-2, 2], [2, 2], [2, -2], [0, 2]]
                if posicion == 2:
                    self.matriz = [[-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1], [0, 0]]
                    self.adyacentes = [[-2, -1], [-1, 2], [0, 2], [1, 2], [2, 1], [-2, 1], [-1, -2], [0, -2], [1, -2],
                                    [2, -1], [1, 0],[-1, 0], [-2, -2], [-2, 0], [-2, 2], [2, 2], [2, -2], [2, 0]]
            
            elif tipo == 3:
                if posicion == 1:
                    self.matriz = [[- 1, - 1], [- 1, 0], [1, 0], [1, 1], [0, 0]]
                    self.adyacentes = [[-2, -1], [-2, 0], [-1, 1], [0, 1], [1, 2], [2, 1], [2, 0], [1, -1],
                                        [0, -1], [-1, -2], [-2, -2], [-2, 1], [0, 2], [2, 2], [2, -1], [0, -2]]

                if posicion == 2:
                    self.matriz = [[0, - 1], [0, 0], [1, - 1], [0, 1], [- 1, 1]]
                    self.adyacentes = [[-1, -1], [-1, 0], [-1, 2], [-1, -2], [1, 0], [1, -2], [1, 2], [1, 1],
                                        [-2, 0], [-2, 1], [-2, 2], [0, -2], [0, 2], [2, -2], [2, -1], [2, 0]]

            elif tipo == 4:
                if posicion == 1:
                    self.matriz = [[1, 0], [- 1, 0], [0, 0]]
                    self.adyacentes = [[-2, -1], [-2, 0], [-2, 1], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1],
                                        [1, 1], [2, -1], [2, 0], [2, 1]]

                if posicion == 2:
                    self.matriz = [[0, -1], [0, 1], [0, 0]]
                    self.adyacentes = [[-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2], [0, -2], [0, 2], [1, -2],
                                        [1, -1], [1, 1], [1, 0], [1, 2]]


        def validar_rango(self):
            for puntos in self.matriz:
                i, j = puntos
                if not(0 <= (i + self.centro_x) <= 9) or not(0 <= (j + self.centro_y) <= 9):
                    return False
            return True

        def posiciones_libres(self, M):
            if self.validar_rango():
                for x, y in self.adyacentes:
                    if (0 <= (x + self.centro_x) <= 9) and (0 <= (y + self.centro_y) <= 9):
                        if M[self.centro_x + x][self.centro_y + y] != 0:
                            return False
                return True
            return False

        def colocar_figuraA(self, M):
            if self.posiciones_libres(M):
                for x, y in self.matriz:
                    M[x + self.centro_x][y + self.centro_y] = 1
                return True
            return False

        def formar_barco(self):
            if self.tipo != 4:
                matriz = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]
                for i, j in self.matriz:
                    matriz[i + 1][j + 1] = 1
            else:
                matriz = [1,1,1]
            return matriz

    def Iniciar_Batalla_Naval(root):
        # Llamar a la función para crear el tablero del usuario
        crear_tableroUsuario()

    def Instruccion_Batalla_Naval(root):
        def Llamar_Sopa_desde_Ins():
            canvas_Intruccion.destroy()
            menuBatalla_Naval(root)

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Configuración del canvas
        canvas_Intruccion = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas_Intruccion.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"intruccion_Sopa.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

        # Guardar una referencia de la imagen
        canvas_Intruccion.image = imagen_fondo_tk

        # Mostrar la imagen de fondo en el canvas
        canvas_Intruccion.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)
        

        # Crear boton para salir
        boton_salir = tk.Button(canvas_Intruccion, text="Salir", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command = Llamar_Sopa_desde_Ins)
        canvas_Intruccion.create_window(screen_width * 0.25, screen_height * 0.7, window=boton_salir)

    def menuBatalla_Naval(root):
        def LlamarMenu_Principal():
            canvas_menuB.destroy()
            menu_principal(root)

        def Llamar_iniciar_juegoBatalla():
            canvas_menuB.destroy()
            Iniciar_Batalla_Naval(root)
        
        def Llamar_Instrucciones():
            canvas_menuB.destroy()
            Instruccion_Batalla_Naval(root)

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Configuración del canvas
        global canvas_menuB
        canvas_menuB = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas_menuB.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"menu_Sopa_.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

        # Guardar una referencia de la imagen
        canvas_menuB.image = imagen_fondo_tk

        # Mostrar la imagen de fondo en el canvas
        canvas_menuB.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)
        
        # Crear boton iniciar Sopa
        boton_iniciar_Batalla = tk.Button(canvas_menuB, text="Iniciar", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=Llamar_iniciar_juegoBatalla)
        canvas_menuB.create_window(screen_width * 0.25, screen_height * 0.3, window=boton_iniciar_Batalla)

        # Crear boton Instruccion
        boton_instruccion = tk.Button(canvas_menuB, text="Intrucciones ", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=Llamar_Instrucciones)
        canvas_menuB.create_window(screen_width * 0.25, screen_height * 0.5, window=boton_instruccion)

        # Crear boton para salir
        boton_salir = tk.Button(canvas_menuB, text="Salir", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command=LlamarMenu_Principal)
        canvas_menuB.create_window(screen_width * 0.25, screen_height * 0.7, window=boton_salir)

    def crearTablero():
        M = []
        for x in range(10):
            M.append([0] * 10)
            cont = 0
        for tipo in range(1, 5):
            if tipo == 4:
                cantBarcos = 3
            else:
                cantBarcos = 1
            for k in range(cantBarcos):
                colocacion_correcta = False
                while colocacion_correcta == False:
                    i = randint(0, 9)
                    j = randint(0, 9)

                    if tipo == 1:
                        posicion = randint(1, 4)
                    else:
                        posicion = randint(1, 2)

                    figura = Barco(tipo, posicion, i, j)
                    colocacion_correcta = figura.colocar_figuraA(M)
        return M

    def verificarTablero(matriz):
        def marcar_barcoEncontrado(matriz, barco):
            for i, j in (barco.matriz):
                x = barco.centro_x + i
                y = barco.centro_y + j
                matriz[x][y] = 0
            
        def verificarBarco(matriz, centro_x, centro_y):
            matrizAuxiliar = [matriz[centro_x-1][centro_y-1:centro_y+2],
                            matriz[ centro_x ][centro_y-1:centro_y+2],
                            matriz[centro_x+1][centro_y-1:centro_y+2]]
            
            #Verificación con el barco tipo 1
            for j in range(1,5):
                barcoAuxiliar = Barco(1,j,centro_x,centro_y)

                if matrizAuxiliar == barcoAuxiliar.formar_barco():
                    if barcoAuxiliar.posiciones_libres(matriz):    
                        marcar_barcoEncontrado(matriz, barcoAuxiliar)
                        return barcoAuxiliar.tipo

            #Verificar barcos 2 y 3
            for i in range(2, 4):
                for j in range(1,3):
                    barcoAuxiliar = Barco(i,j,centro_x,centro_y)

                    if matrizAuxiliar == barcoAuxiliar.formar_barco():
                        if barcoAuxiliar.posiciones_libres(matriz):    
                            marcar_barcoEncontrado(matriz, barcoAuxiliar)
                            return barcoAuxiliar.tipo

            #Verificar barco tipo 4 posicion 1
            for j in range(2):
                barcoAuxiliar = Barco(4, 1, centro_x, centro_y-1+j)
                matrizAuxiliar2 = []
                for i in range(3):
                    matrizAuxiliar2.append(matrizAuxiliar[i][j])
                
                if matrizAuxiliar2 == barcoAuxiliar.formar_barco():
                    if barcoAuxiliar.posiciones_libres(matriz):    
                        marcar_barcoEncontrado(matriz, barcoAuxiliar)
                        return barcoAuxiliar.tipo
                
            #Verificar barco tipo 4 posicion 2
            for i in range(2):
                barcoAuxiliar = Barco(4,2,centro_x-1+i,centro_y)
                if matrizAuxiliar[i] == barcoAuxiliar.formar_barco():
                    if barcoAuxiliar.posiciones_libres(matriz):    
                        marcar_barcoEncontrado(matriz, barcoAuxiliar)
                        return barcoAuxiliar.tipo
            return 0
        
        #Inicio verificación
        cantBarcos = [0]*4
        for i in range(0, 8):
            for j in range(0, 8):
                tipoBarco = 0
                if matriz[i][j] == 1 or matriz[i][j+1] == 1 or matriz[i+1][j] == 1:
                    tipoBarco = verificarBarco(matriz, i+1, j+1)
                    
                if j == 7 and tipoBarco == 0:
                    #Verificar barco tipo 4 posicion 1 en la última columna
                    if matriz[i][9] == 1:
                        barcoAuxiliar = Barco(4,1,i+1,9)
                        matrizAuxiliar = []
                        for fila in range(i, i+3):
                            matrizAuxiliar.append(matriz[fila][9])
                        
                        if matrizAuxiliar == barcoAuxiliar.formar_barco():
                            if barcoAuxiliar.posiciones_libres(matriz):
                                marcar_barcoEncontrado(matriz, barcoAuxiliar)
                                tipoBarco = barcoAuxiliar.tipo

                if i == 7 and tipoBarco == 0:
                    #Verificar barco tipo 4 posicion 2 en la última fila
                    barcoAuxiliar = Barco(4,2,9,j+1)
                    matrizAuxiliar = matriz[9][j:j+3]
                    if matrizAuxiliar == barcoAuxiliar.formar_barco():
                        if barcoAuxiliar.posiciones_libres(matriz):    
                            marcar_barcoEncontrado(matriz, barcoAuxiliar)
                            tipoBarco = barcoAuxiliar.tipo
                
                if tipoBarco != 0:
                    cantBarcos[tipoBarco-1] += 1

        mensaje = "ERRORES: \n"
        barcoscorrectos = [1,1,1,3]
        if cantBarcos == barcoscorrectos:
            es_correcto = True
        else:
            cont = 1
            for i, j in zip(barcoscorrectos, cantBarcos):
                if j < i:
                    # colocar sistema para asignar un nombre a cada num de barco
                    mensaje += f"Falta(n) {i-j} barco(s) tipo: {cont}.\n"
                elif j > i:
                    mensaje += f"Sobra(n) {j-i} barco(s) tipo: {cont}.\n"
                cont+=1
            es_correcto = False
        return mensaje, es_correcto
    
    # global tableroUsuario
    def crear_tableroUsuario():
        def finalizar_entrada():
            mensaje, es_correcto = verificarTablero(copy.deepcopy(tableroUsuario))
            if es_correcto:
                canvas.destroy()
                mostrar_ambosTableros()
            else:
                messagebox.showinfo("Tablero Inválido", mensaje)

        # Configurar la ventana para que sea del mismo tamaño que la pantalla completa
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Crear un canvas para la imagen de fondo
        canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"batalla_naval_selec_tab.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

        # Redimensionar la imagen para ajustarse a la ventana
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
        canvas.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)

        # Asegurarse de que la imagen de fondo persista
        root.imagen_fondo_tk = imagen_fondo_tk

        # Definir el tablero del usuario
        global tableroUsuario
        tableroUsuario = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Crear un marco para la matriz (usando el canvas)
        frame_matriz = tk.Frame(canvas, bg='blue')
        canvas.create_window(screen_width // 2 + 350 , screen_height // 2 + 1 , window=frame_matriz, anchor="center")

        # Crear la matriz con botones
        for i in range(len(tableroUsuario)):
            for j in range(len(tableroUsuario[i])):
                frame_cell = tk.Frame(frame_matriz, borderwidth=1, relief="solid", width=50, height=50)
                frame_cell.grid(row=i, column=j, padx=10, pady=10) # cambie de 5 a 10.
                button = tk.Button(frame_cell, text="", bg="blue", width=5, height=2)
                button.config(command=lambda b=button, i=i, j=j: cambiarValor(tableroUsuario, i, j, b))
                button.grid(row=0, column=0, sticky="nsew")  # Añadir un padding para expandir los botones
                frame_cell.rowconfigure(0, weight=1)  # Hacer que la fila se expanda
                frame_cell.columnconfigure(0, weight=1)  # Hacer que la columna se expanda

        # Botón para FINALIZAR ENTRADA de palabras
        boton_finalizar = tk.Button(canvas,width=15, height=2, text="Verificar Matriz", command=finalizar_entrada , bg="lightblue" , fg="#0000FA",font=("Lilita One", 16),borderwidth=3)
        boton_finalizar.place(relx=0.428 , rely=0.850, anchor="center")

    def cambiarValor(matriz, i, j, button):
        if matriz[i][j] == 0:
            matriz[i][j] = 1
            button.config(bg="yellow",text="*")  # Cambiar color a amarillo si es 1
        else:
            matriz[i][j] = 0
            button.config(bg="blue",text="")  # Cambiar color a azul si es 0

    def mostrar_ambosTableros():
        #Inicialzación de puntos para el usuario y la maquina
        global puntosUsuario, puntosMaquina
        puntosUsuario = 0
        puntosMaquina = 0 

        # Configurar la ventana para que sea del mismo tamaño que la pantalla completa
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Crear un canvas para la imagen de fondo
        global canvas
        canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"batalla_naval_fondoBasic.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

        # Redimensionar la imagen para ajustarse a la ventana
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
        canvas.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)

        # Asegurarse de que la imagen de fondo persista
        root.imagen_fondo_tk = imagen_fondo_tk

        # Definir el tablero de la maquina
        global tableroMaquina
        tableroMaquina = crearTablero()

        # Crear un marco para la matriz (usando el canvas)
        frame_matrizMaquina = tk.Frame(canvas, bg='blue')
        canvas.create_window(screen_width // 2 - 300, screen_height // 2 + 30, window=frame_matrizMaquina, anchor="center")

        # Crear la matriz con botones del tablero Maquina
        global buttons_maquina
        buttons_maquina = []
        for i in range(len(tableroUsuario)):
            row_buttons = []
            for j in range(len(tableroUsuario[i])):
                frame_cell = tk.Frame(frame_matrizMaquina, borderwidth=1, relief="solid", width=50, height=50)
                frame_cell.grid(row=i, column=j, padx=5, pady=5)
                button = tk.Button(frame_cell, text="", bg="white", width=4, height=2, cursor="pirate")
                button.config(command=lambda b=button, i=i, j=j: atacarTableroMaquina(tableroMaquina, i, j, b))
                button.grid(row=0, column=0, sticky="nsew")  # Añadir un padding para expandir los botones
                frame_cell.rowconfigure(0, weight=1)  # Hacer que la fila se expanda
                frame_cell.columnconfigure(0, weight=1)  # Hacer que la columna se expanda
                row_buttons.append(button)
            buttons_maquina.append(row_buttons)

        # Crear un marco para la matriz del Usuario (usando el canvas)
        frame_matrizUsuario = tk.Frame(canvas, bg='blue')
        canvas.create_window(screen_width // 2 + 300, screen_height // 2 + 30, window=frame_matrizUsuario, anchor="center")

        # Crear la matriz con botones del tablero del usuario
        global botones_usuario
        botones_usuario=[]
        for i in range(len(tableroUsuario)):
            row_buttons = []
            for j in range(len(tableroUsuario[i])):
                frame_cell = tk.Frame(frame_matrizUsuario, borderwidth=1, relief="solid", width=50, height=50)
                frame_cell.grid(row=i, column=j, padx=5, pady=5)
                if tableroUsuario[i][j] == 1:
                    punto = "*"
                    color = "yellow"
                else:
                    punto = ""
                    color = "blue"
                button = tk.Button(frame_cell, text=punto, bg=color, width=4, height=2, state=tk.DISABLED)
                button.grid(row=0, column=0, sticky="nsew")  # Añadir un padding para expandir los botones
                frame_cell.rowconfigure(0, weight=1)  # Hacer que la fila se expanda
                frame_cell.columnconfigure(0, weight=1)  # Hacer que la columna se expanda
                row_buttons.append(button)
            botones_usuario.append(row_buttons)
                

    # Función para deshabilitar todos los botones del tablero del usuario
    def deshabilitar_botones_maquina():
        for i in range(10):
            for j in range(10):
                buttons_maquina[i][j].config(state=tk.DISABLED)

    # Función para habilitar todos los botones del tablero del usuario
    def habilitar_botones_maquina():
        for i in range(10):
            for j in range(10):
                if buttons_maquina[i][j]["bg"] not in ["yellow", "blue"]:  # No habilitar botones ya atacados
                    buttons_maquina[i][j].config(state=tk.NORMAL)

    # Función para atacar el tablero de la máquina
    def atacarTableroMaquina(matriz, i, j, button):
        global puntosUsuario
        if matriz[i][j] == 1:
            button.config(bg="yellow", text="*")  # Cambiar color a amarillo si es 1
            puntosUsuario += 1
            if puntosUsuario == 28:
                root.after(4000, lambda: canvas.destroy())  # Destruir el canvas después de 1 segundo
                mostrar_resultados(True)
        else:
            button.config(bg="blue", text="X")  # Cambiar color a azul si es 0
        button.config(state=tk.DISABLED)  # Deshabilitar el botón atacado
        deshabilitar_botones_maquina()  # Deshabilitar los botones del tablero del usuario
        # Usar after para esperar 0,5 segundo antes de llamar a atacarTableroUsuario
        root.after(1000, atacarTableroUsuario())

    # Función para atacar el tablero del usuario
    def atacarTableroUsuario():
        # buttons_maquina[i][j].config(state=tk.DISABLED)
        global puntosMaquina
        a = randint(0, 9)
        b = randint(0, 9)

        # Verifica que la posición no haya sido atacada antes
        while tableroUsuario[a][b] == -1:  
            a = randint(0, 9)
            b = randint(0, 9)

        # Marcar como atacado si es igual a 1
        if tableroUsuario[a][b] == 1:
            tableroUsuario[a][b] = -1  
            button = botones_usuario[a][b]

            # Cambiar color a rojo si es 1
            button.config(bg="#E30613", text="*")  
            puntosMaquina += 1

        else:
            tableroUsuario[a][b] = -1  # Marcar como atacado
            button = botones_usuario[a][b]
            button.config(bg="black", text="X")  # Cambiar color a negro si es 0

        if puntosMaquina == 28:
            root.after(4000, lambda: canvas.destroy())  # Destruir el canvas después de 1 segundo
            mostrar_resultados(False)
        
        habilitar_botones_maquina()
        
    def mostrar_resultados(es_ganadorUsuario):
        def Llamar_menu_Batalla_desde_Result():
            canvas.destroy()
            menuBatalla_Naval(root)
        
        # Configurar la ventana para que sea del mismo tamaño que la pantalla completa
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Crear un canvas para la imagen de fondo
        canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas.pack(fill="both", expand=True)

        # Cargar la imagen de fondo usando Pillow
        ruta_imagen = r"reusltado_1_batalla_naval.png"
        imagen_fondo = Image.open(ruta_imagen)
        imagen_fondo = imagen_fondo.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

        # Redimensionar la imagen para ajustarse a la ventana
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
        canvas.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)

        # Asegurarse de que la imagen de fondo persista
        root.imagen_fondo_tk = imagen_fondo_tk

        if es_ganadorUsuario:
            print("Ganaste")
            ruta_imagen_resultado = r"ganaste_batalla_naval.png"
        else:
            print("Perdiste")
            ruta_imagen_resultado = r"perdiste_batalla_naval.png"

        # Cargar la imagen de fondo del resultado usando Pillow
        imagen_fondo_resultado = Image.open(ruta_imagen_resultado)

        # Mantener la proporción de la imagen
        aspect_ratio = imagen_fondo_resultado.width / imagen_fondo_resultado.height
        new_width = int(screen_width * 0.5)
        new_height = int(new_width / aspect_ratio)

        imagen_fondo_resultado = imagen_fondo_resultado.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Redimensionar la imagen para ajustarse a la ventana
        imagen_fondo_resultado_tk = ImageTk.PhotoImage(imagen_fondo_resultado)
        canvas.create_image(screen_width // 2, screen_height // 2, anchor="center", image=imagen_fondo_resultado_tk)

        # Asegurarse de que la imagen de resultado persista
        root.imagen_fondo_resultado_tk = imagen_fondo_resultado_tk

        # Crear boton para salir
        boton_salir = tk.Button(canvas, text="Salir", font=("Lilita One", 28), bg="white", foreground="#31CFFF", relief="flat", command = Llamar_menu_Batalla_desde_Result)
        canvas.create_window(screen_width * 0.25, screen_height * 0.7, window=boton_salir)
   
    menuBatalla_Naval(root)




root = tk.Tk()
root.title("Juegos Divertidos")

# Configurar la root para que sea un poco más pequeña que la pantalla completa
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")


menu_principal(root)

# Iniciar el loop principal
root.mainloop() 


