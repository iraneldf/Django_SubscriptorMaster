import json
import os

import filelock
from django.core.mail import send_mail

from src import settings
from web.models import Config, Suscriptor

# crear un bloqueo para el archivo "datos.json"
lock = filelock.FileLock("news.json.lock")
lock2 = filelock.FileLock("sms.json.lock")


def ppp():
    try:
        # Abrir el archivo JSON en modo de lectura
        with lock.acquire(timeout=7):
            with open('news.json', 'r') as archivo:
                # Leer cada diccionario del archivo

                recipient_list = [
                    suscriptor.email for suscriptor in Suscriptor.objects.all()]

                config = Config.objects.first()
                for linea in archivo:
                    diccionario = json.loads(linea)
                    subject = diccionario['titulo']
                    nombre_negocio = f'Desde {config.business_name}' if config.business_name is not None else " "
                    noticia = diccionario["noticia"]
                    message = f'{nombre_negocio}:\n{noticia}'
                    email_from = settings.EMAIL_HOST_USER
                    count = 0
                    for r in range(0, len(recipient_list), 100):

                        try:
                            send_mail(subject, '', email_from, recipient_list=recipient_list[count:count + 100],
                                      html_message=message)
                            print(recipient_list[count:count + 100])
                        except:
                            print('no se envio')

                        else:
                            print(f'Correo electrónico enviado a destinatarios {count + 1} a {count + 100}')

                        count += 100

        # Cierra el archivo JSON
        print('se elimina el json')
        os.remove('news.json')

    except FileNotFoundError as e:
        # Si el archivo no existe, imprimir un mensaje de error
        print("El archivo 'news.json' no se pudo encontrar.", e)

    except filelock.Timeout as e:
        print("El archivo 'news.json' aun esta en uso.", e)



    finally:
        lock.release()

    try:
        # Abrir el archivo JSON en modo de lectura
        with lock2.acquire(timeout=7):
            with open('sms.json', 'r') as archivo2:
                # Leer cada diccionario del archivo
                numbers = Suscriptor.objects.exclude(phone__isnull=True)
                sms_dir = settings.SMS_DIR
                queryset = []
                for linea in archivo2:
                    diccionario = json.loads(linea)
                    queryset.append(diccionario)

                for number in numbers:
                    for sms in queryset:
                        nombre_archivo = f'{number.phone}__{sms["pk"]}.txt.tmp'
                        ruta_completa = os.path.join(sms_dir, nombre_archivo)

                        archivo3 = open(ruta_completa, "w")

                        # para que respete la cantidad de espacios en blanco
                        [archivo3.write(linea) for linea in sms['sms'].split('\n')]

                        archivo3.close()
                        try:
                            print(ruta_completa)
                            os.rename(ruta_completa, ruta_completa.replace('.tmp', ''))
                            print(ruta_completa)
                        except Exception as e:
                            print('ya esxiste', e)

            # Cierra el archivo JSON
            print('se elimina el json')
            os.remove('sms.json')


    except FileNotFoundError as e:
        # Si el archivo no existe, imprimir un mensaje de error
        print("El archivo 'sms.json' no se pudo encontrar.", e)

    except filelock.Timeout as e:
        print("El archivo 'sms.json' aun esta en uso.", e)


    finally:
        lock2.release()
