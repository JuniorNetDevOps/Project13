from netmiko import ConnectHandler


# DEFINE THE ROUTER's DETAILS
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

devices = [rtr1, rtr2, cor1, cor2]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(f"----- BEGIN -----")
    print(f"******************* Before create username *******************")
    task1 = net_connect.send_command('show running-config | include username')
    print(task1)
    print(f"******************* DELETE username *******************")
    config_commands = ['no username azrul']

    task2 = net_connect.send_config_set(config_commands)
    task2 +=
    print(task2)
    print(f"******************* After create username *******************")
    task3 = net_connect.send_command('show running-config | include username')
    print(task3)
    print(f"----- END -----")