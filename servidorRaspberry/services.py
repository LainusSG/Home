import requests
  
if __name__ == '__main__':
    url = 'https://io.adafruit.com/api/v2/LainusG/feeds/mi-primer-envio'
   
    response = requests.get(url)

if response.status_code == 200:
    contenido= response.content
    print (contenido)
    
  


  





