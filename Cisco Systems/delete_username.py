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

config_commands = ['no username humaira']

for device in devices:
    net_connect = ConnectHandler(**device)
    print(f"----- BEGIN -----")
    print(f"******************* DELETE username *******************")
    output = net_connect.send_command_timing(
        command_string=config_commands, strip_prompt=False, strip_command=False
    )
    if "Delete filename" in output:
        output += net_connect.send_command_timing(
            command_string="y", strip_prompt=False, strip_command=False
        )
    if "confirm" in output:
        output += net_connect.send_command_timing(
            command_string="\n", strip_prompt=False, strip_command=False
        )
    print(output)
    print(f"----- END -----")
