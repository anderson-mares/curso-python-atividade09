import platform
import subprocess

# Identifica o sistema operacional
os_name = platform.system()
print(f"Sistema Operacional: {os_name}")

if os_name == 'Windows':
    try:
        # Verificando tanto a chave 32-bit quanto 64-bit para programas instalados
        output = subprocess.check_output('reg query "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall" /s', shell=True, text=True)
        output += subprocess.check_output('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall" /s', shell=True, text=True)
        
        # Filtrando a saída para pegar apenas os nomes dos programas
        programs = [line for line in output.splitlines() if 'DisplayName' in line]
        print("\nProgramas instalados:")
        for program in programs:
            print(program.split("    ")[-1])
    except Exception as e:
        print(f"Erro ao listar programas no Windows: {e}")

elif os_name == 'Darwin':  # macOS
    try:
        # Usando 'system_profiler SPApplicationsDataType' no macOS
        output = subprocess.check_output(['system_profiler', 'SPApplicationsDataType'], text=True)
        programs = output.split('\n')
        print("\nProgramas instalados:")
        for program in programs:
            print(program)
    except Exception as e:
        print(f"Erro ao listar programas no macOS: {e}")

else:
    print("Sistema Operacional não suportado.")
