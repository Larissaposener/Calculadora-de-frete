def calculadoraFrete(altura,largura,peso):
    entrega1 =entregaNinja(altura[0],largura[0],peso[0])
    entrega2 = entregaKabum(altura[0],largura[0],peso[0])

    return [entrega1,entrega2]

def entregaNinja(altura,largura,peso):
    constanteNinja = 0.3
    valorFrete = calculaConstante(peso,constanteNinja)
    if(altura < 10 or altura > 200 or largura < 6 or largura > 140):
        return []
    else:
        return {
          "nome":"Entrega Ninja",
    	  "valor_frete": valorFrete,
    	  "prazo_dias": 6
	    }
    

def entregaKabum(altura,largura,peso):
    constanteKabum = 0.2
    valorFreteK = calculaConstante(peso,constanteKabum)
    if(altura < 5 or altura > 140 or largura < 13 or largura > 125):
        return []
    else:
       return {
          "nome":"Entrega KaBuM",
    	  "valor_frete": valorFreteK,
    	  "prazo_dias": 4
	    }

def calculaConstante(peso,constante):
    return (peso*constante)/10   

