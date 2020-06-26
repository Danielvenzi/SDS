import os
import mysql.connector
import schedule
import time

def zabbix_clean():

    try:
        print("Zabbix cleaner - Inicializando a conexão...")
        connection = mysql.connector.connect(host='127.0.0.1',
                                            database='zabbix',
                                            user='root',
                                            password='Zabbix!22')

        if connection.is_connected():
            print("Zabbix - cleaner - Conexão bem sucedida")
            cursor = connection.cursor()
            sql_Delete_queries = ["DELETE FROM history_uint;",
                                    "DELETE FROM history;",
                                    "DELETE FROM trends_uint;",
                                    "DELETE FROM trends;",
                                    "DELETE FROM events;",
                                    "DELETE FROM alerts;"]

            for query  in sql_Delete_queries:
                print("Zabbix cleaner - Executando comando: {}".format(query))
                cursor.execute(query)

            connection.commit()
            cursor.close()
            connection.close()
            print("Zabbix cleaner - Registros antigos retirados do banco de dados.")
        
        else:
            print("Zabbix - cleaner - Conexão mal sucedida")
            

    except mysql.connector.Error as e:
        print("Zabbix cleaner - Um erro aconteceu {}".format(e))

if __name__ == "__main__":

    schedule.every().monday.at("23:00").do(zabbix_clean)
    schedule.every().tuesday.at("23:00").do(zabbix_clean)
    schedule.every().wednesday.at("23:00").do(zabbix_clean)
    schedule.every().thursday.at("23:00").do(zabbix_clean)
    schedule.every().friday.at("23:00").do(zabbix_clean)

    while True:
        schedule.run_pending()
        time.sleep(1)