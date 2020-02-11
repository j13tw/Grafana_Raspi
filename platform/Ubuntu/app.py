import os, sys
import requests

os.system("apt-get update -y")
os.system('echo "deb https://packages.grafana.com/oss/deb stable main" > /etc/apt/sources.list.d/grafana.list')
os.system("apt-get install -y apt-transport-https curl")
os.system("curl https://packages.grafana.com/gpg.key | apt-key add -")
os.system("apt-get update -y")
os.system("apt-get install -y grafana")
os.system("service grafana-server start")
os.system("update-rc.d grafana-server defaults")
os.system("apt-get install -y mysql-server mysql-client")
os.system("apt-get install -y python3-dev python3-pip libmysqlclient-dev")
os.system("apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev")
os.system("pip3 install mysqlclient")
os.system("pip3 install paho-mqtt")
os.system("service mysql start")
os.system('mysql -u root -proot -e "create database factory"')
os.system('mysql -u root -proot -e "CREATE USER \'imac\'@\'localhost\' IDENTIFIED BY \'imacuser\';"')
os.system('mysql -u root -proot -e "GRANT ALL PRIVILEGES ON factory.* TO \'imac\'@\'localhost\';"')
os.system('mysql -u root -proot -e "FLUSH PRIVILEGES;"')
os.system("python3 ../../database/MySQL/Create_Tables.py")
os.system("apt-get install supervisor -y")
os.system("cp ./dataTransport.conf /etc/supervisor/conf.d")
os.system("service supervisor restart")

datasources = open("../../database/MySQL/datasource/mysql.json", "r")
datasources_info = datasources.read()
datasources.close()

dashboard_dl303 = open("../../database/MySQL/dashboard/dl303.json", "r")
dashboard_dl303_info = dashboard_dl303.read()
dashboard_dl303.close()

dashboard_et7044 = open("../../database/MySQL/dashboard/et7044.json", "r")
dashboard_et7044_info = dashboard_et7044.read()
dashboard_et7044.close()

dashboard_ups_a = open("../../database/MySQL/dashboard/ups-a.json", "r")
dashboard_ups_a_info = dashboard_ups_a.read()
dashboard_ups_a.close()

dashboard_ups_b = open("../../database/MySQL/dashboard/ups-b.json", "r")
dashboard_ups_b_info = dashboard_ups_b.read()
dashboard_ups_b.close()

dashboard_ups_route = open("../../database/MySQL/dashboard/ups-route.json", "r")
dashboard_ups_route_info = dashboard_ups_route.read()
dashboard_ups_route.close()

dashboard_air_condiction = open("../../database/MySQL/dashboard/air-condiction.json", "r")
dashboard_air_condiction_info = dashboard_air_condiction.read()
dashboard_air_condiction.close()

try: 
    if (requests.get("http://127.0.0.1:3000/login").status_code == 200):
        try:
            requests.post("http://admin:admin@127.0.0.1:3000/api/datasources", data=datasources_info.encode('utf-8'), headers={"Content-Type": "application/json"})
            print("create datasource")
        except:
            print("add datasource error")
        try:
            requests.post("http://admin:admin@127.0.0.1:3000/api/dashboards/db", data=dashboard_dl303_info.encode('utf-8'), headers={"Content-Type": "application/json"})
            print("create dl303 dashboard")
        except:
            print("add dl303 dashboard error")
        try:
            requests.post("http://admin:admin@127.0.0.1:3000/api/dashboards/db", data=dashboard_et7044_info.encode('utf-8'), headers={"Content-Type": "application/json"})
            print("create et7044 dashboard")
        except:
            print("add et7044 dashboard error")
        try:
            requests.post("http://admin:admin@127.0.0.1:3000/api/dashboards/db", data=dashboard_ups_a_info.encode('utf-8'), headers={"Content-Type": "application/json"})
            print("create ups-a dashboard")
        except:
            print("add ups-a dashboard error")
        try:
            requests.post("http://admin:admin@127.0.0.1:3000/api/dashboards/db", data=dashboard_ups_b_info.encode('utf-8'), headers={"Content-Type": "application/json"})
            print("create ups-b dashboard")
        except:
            print("add ups-b dashboard error")
        try:
            requests.post("http://admin:admin@127.0.0.1:3000/api/dashboards/db", data=dashboard_ups_route_info.encode('utf-8'), headers={"Content-Type": "application/json"})
            print("create ups-route dashboard")
        except:
            print("add ups-route dashboard error")
        try:
            requests.post("http://admin:admin@127.0.0.1:3000/api/dashboards/db", data=dashboard_air_condiction_info.encode('utf-8'), headers={"Content-Type": "application/json"})
            print("create air_condiction dashboard")
        except:
            print("add air_condiction dashboard error")
    else:
        try:
            os.system("service grafana-server start")
        except:
            print("grafana_service error")
except:
    print("grafana_service error")