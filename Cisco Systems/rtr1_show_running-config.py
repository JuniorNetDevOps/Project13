from netmiko import ConnectHandler


# Define the router's details
rtr1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.16.33',
    'port': '22',
    'username': 'kenshin',
    'password': 's3cur3@2020',
}

# Connect to router using SSH
net_connect = ConnectHandler(**rtr1)
output = net_connect.send_command('show running-config interface ethernet 0/0')


print(f"\n\n--------- {rtr1['host']} ---------")
print(output)
print("--------- END ---------")
