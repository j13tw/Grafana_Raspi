import os, sys

os.system("apt-get update -y")
os.system('echo "deb https://packages.grafana.com/oss/deb stable main" > /etc/apt/sources.list.d/grafana.list')
os.system("apt-get install -y curl")
os.system("apt-get install -y apt-transport-https")
os.system("curl https://packages.grafana.com/gpg.key | apt-key add -")
os.system("apt-get update -y")
os.system("apt-get install grafana")
os.system("service grafana-server start")
os.system("update-rc.d grafana-server defaults")
