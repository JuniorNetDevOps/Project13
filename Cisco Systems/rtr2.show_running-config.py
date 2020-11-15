from netmiko import ConnectHandler


# DEFINE THE ROUTER's DETAILS
rtr1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.16.33',
    'port': '22',
    'username': 'kenshin',
    'password': 's3cur3@2020',
}


net_connect = ConnectHandler(**rtr1)
output = net_connect.send_command('\nshow running-config interface ethernet 0/0')
output += net_connect.send_command('\nshow ip interface brief')
output += net_connect.send_command('\nshow ip route 0.0.0.0 0.0.0.0')


print(f"\n\n--------- {rtr1['host']} ---------")
print(output)
print("--------- END ---------")
