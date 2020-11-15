from netmiko import ConnectHandler


# Define the devices' details
rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.16.32',
    'port': '22',
    'username': 'kenshin',
    'password': 's3cur3@2020',
}

rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.16.33',
    'port': '22',
    'username': 'kenshin',
    'password': 's3cur3@2020',
}

cor1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.16.34',
    'port': '22',
    'username': 'kenshin',
    'password': 's3cur3@2020',
}

cor2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.16.35',
    'port': '22',
    'username': 'kenshin',
    'password': 's3cur3@2020',
}


# Create the dictionary
devices = [rtr1, rtr2, cor1, cor2]


# Connect to the devices using SSH
for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show running-config')
    print(f"--------- ('ip') ---------")
    print(f"\n\n--------- BEGIN ---------")
    print(output)
    print("--------- END ---------")
