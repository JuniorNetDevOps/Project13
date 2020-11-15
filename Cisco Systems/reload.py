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

routers = [rtr1, rtr2]

cofig_commands['no username jailani']

for router in routers:
    net_connect = ConnectHandler(**router)
    task1 = net_connect.send_config_set(config_commands='c', expect_string='[confirm]')
    task1 += net_connect.send_command('\n')
    print(task1)