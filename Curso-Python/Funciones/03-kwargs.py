def get_product(**datos): #en este caso tenemos que indicar el nombre del parametro al pasarlo 
    print(datos) #imprime todos los datos
    print("id: " + datos["id"]) #imprime solo id     
    print("id:" + datos["id"] + " Name:" + datos["name"]) #imprime id y name     

get_product(id="7168549",
            name="Iphone",
            des="Modelo 2020, 15 pro max")