import cv2
import pandas as pd


url1 = "Gorilla1.jpg"
url2 = "perro.PNG"
url3 = "Mamut2.pnp"
img1 = cv2.imread("Gorilla1.jpg", 0)

#orb = cv2.ORB_create()

listaImagenes = [url2,url3]

resultadoClasificacion = []

def clasificarImagenes(imagenReferencia,url): 
    imagenAClasificar = cv2.imread(url, 0)



    orb = cv2.ORB_create()   
    kp1, des1 = orb.detectAndCompute(imagenReferencia, None)
    kp2, des2 = orb.detectAndCompute(imagenAClasificar, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    resultado = cv2.drawMatches(img1, kp1, imagenAClasificar, kp2, matches[:20], None)

    good_matches = [m for m in matches if m.distance < 50]

    porcentaje = (len(good_matches) / len(kp1)) * 100

    print("Coincidencia: ",porcentaje)
    clasificacion = ""
    cv2.imshow("Coincidencias", resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if porcentaje < 0.8:
        print("Es un Gorilla")
        clasificacion = "Es un Gorilla"
    else:
        print("No es un Gorilla")
        clasificacion = "No es un Gorilla"
    
    datosClasificacion ={
        "ImagenClasificada": url,
        "Clasificacion": clasificacion
    } 
    resultadoClasificacion.append(datosClasificacion)

for imagen in listaImagenes:
    clasificarImagenes(img1,imagen)

print(resultadoClasificacion)
resultadoFinal = pd.DataFrame(resultadoClasificacion)

resultadoFinal.to_json("backup_clasificacion.json")