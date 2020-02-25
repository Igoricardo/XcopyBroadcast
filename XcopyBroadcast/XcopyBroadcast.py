U = 'UltraVNC'                                         # <- Variaveis criadas para evitar erros de unicode
u = 'uvnc bvba'

ip1 = input('Informe o IP 1: ')
ip2 = input('Informe o IP 2: ')
ip3 = input('Informe o IP 3: ')

arquivo = open('XcopyBroadcast.bat', 'w')
arquivo.write('@echo off \n')

while True:
    opcao = int(input('1 = Acrescentar / 2 = Encerrar Aplicação: '))
    if opcao == 1:

        ip4 = int(input('IP 4: '))

        with open('XcopyBroadcast.bat', 'a') as arquivo:
            arquivo.write(f'''
ping -n 2 {ip1}.{ip2}.{ip3}.{ip4} >> 'C:\\applications\XcopyBroadcast_Ping.log' ''')

            arquivo.write(f'''
xcopy "C:\\applications\SecureVNC" "\\\\{ip1}.{ip2}.{ip3}.{ip4}\c$\SecureVNC" /F /C /E
xcopy "\\\\{ip1}.{ip2}.{ip3}.{ip4}\c$\SecureVNC\Chaves" "\\\\{ip1}.{ip2}.{ip3}.{ip4}\c$\Program Files (x86)\{u}\{U}" /F /C /E \n''')

    elif opcao == 2:
        print('Aplicação Encerrada!')
        break

arquivo = open('XcopyBroadcast.bat', 'a')
arquivo.write('\npause')
