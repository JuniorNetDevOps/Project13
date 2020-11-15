from netmiko import ConnectHandler


# Define the router's details
rtr2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.16.34',
    'port': '22',
    'username': 'kenshin',
    'password': 's3cur3@2020',
}


# Connect to router using SSH
net_connect = ConnectHandler(**rtr2)
output = net_connect.send_command('show running-config')


print(f"\n\n--------- {rtr2['host']} ---------")
print(output)
print("--------- END ---------")
