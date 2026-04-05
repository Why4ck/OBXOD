import subprocess
from colorama import Fore, Style, init
import os
import time
from pathlib import Path
import rich.console
import sys

init()



# base
warp_work = False
zapret_work = False
console = rich.console.Console()



class Launcher:
    
    
    def __init__(self, zapret_path: Path):
        self.zp = zapret_path
        self.z_file = "general (ALT3).bat"
        self.wapr_check_cmd = "warp-cli -V"
        
        from rich.console import Console
        self.console = Console()
       
       
       
    def check_zapret(self):
        folder_path = self.zp
        
        if not os.path.isdir(folder_path) or not os.path.isdir(Path(self.zp).parent):
            print(Fore.RED, f"Error: Dir not found: {folder_path}", Style.RESET_ALL, sep='')
            return False

        full_file_path = os.path.join(folder_path, self.z_file)

        if os.path.isfile(full_file_path):
            print(Fore.GREEN, "Successfully | Zapret found", Style.RESET_ALL, sep="")
            return True
        else:
            try:
                files_in_dir = os.listdir(folder_path)
                bat_files = [f for f in files_in_dir if f.endswith('.bat')]
                print(Fore.YELLOW, f"Available .bat files in '{folder_path}': {bat_files}", Style.RESET_ALL, sep='')
            except Exception:
                pass
                
            print(Fore.RED, f"Error\nZapret file not found: {self.z_file}", Style.RESET_ALL, sep="", end='\n\n')
            return False
        
        
        
    def check_warp(self):
        try:
            cmd_list = self.wapr_check_cmd.split(" ")
            
            warp_check = subprocess.check_output(
                [cmd_list[0], cmd_list[1]],
                stderr=subprocess.STDOUT,
                text=True,
                timeout=5
            )
            
            if "warp-cli" in warp_check:
                print(Fore.GREEN, "Successfully | Warp found", Style.RESET_ALL, sep="")
                return True
            
        except FileNotFoundError:
            print(Fore.RED, f"\nERROR\nCloudflare WARP not found", Style.RESET_ALL, sep="", end="\n\n")
            print(Fore.GREEN, "Download warp here -> https://1.1.1.1", Style.RESET_ALL, sep="", end="\n\n")
            return False
        
        except Exception as e:
            print(Fore.RED, f"Unknown error\n\nError: {e}\n\n", Style.RESET_ALL, sep="")
            return False



    def __warp_reg(self):
        try:
            show = subprocess.check_output(
                ['warp-cli', 'registration', 'show'], 
                stderr=subprocess.STDOUT,
                text=True
            )
        except subprocess.CalledProcessError as e:
            show = e.output
        
        if "Error" in show:
            text = f"{Fore.GREEN} Warp account creating\n{Style.RESET_ALL}"
            
            with self.console.status(text, spinner='bouncingBar'):
                new_reg = subprocess.run(
                    ['warp-cli', 'registration', 'new'],
                    capture_output=True,
                    text=True
                )
            
            reg_output = new_reg.stdout + new_reg.stderr
            
            if "Success" in reg_output:
                print(Fore.GREEN, "Warp account created", Style.RESET_ALL, sep='')
                return True
            
            elif "The IPC call hit a timeout and could not be processed" in reg_output:
                print(Fore.RED, "Error Warp account creating", Style.RESET_ALL, sep="")
                print(Fore.RED, "Killing Warp task", Style.RESET_ALL, sep="")
                
                subprocess.run(['taskkill', '/f', '/im', 'Cloudflare WARP.exe'], 
                            capture_output=True)
                
                print(Fore.RED, "Delete old Warp account", Style.RESET_ALL, sep="")
                subprocess.run(['warp-cli', 'registration', 'delete'],
                            capture_output=True)
                
                print(Fore.RED, "Creating new Warp account", Style.RESET_ALL, sep="")
                
                retry = subprocess.run(
                    ['warp-cli', 'registration', 'new'],
                    capture_output=True,
                    text=True
                )
                
                if "Success" in retry.stdout + retry.stderr:
                    print(Fore.GREEN, "Warp account created", Style.RESET_ALL, sep='')
                    return True
                else:
                    print(Fore.RED, "Failed to create account", Style.RESET_ALL, sep="")
                    return False
            
            else:
                print(Fore.RED, "Error Warp account creating", Style.RESET_ALL, sep="")
                print(Fore.RED, "Try restarting WARP service manually", Style.RESET_ALL, sep="")
                return False
                
        else:
            print(Fore.GREEN, "Warp account was created earlier", Style.RESET_ALL, sep='')
            return True
        
        
        
    def check_warp_account(self):
        show = subprocess.run(
            ['warp-cli', 'registration', 'show'],
            capture_output=True, 
            text=True
        )
        
        output = show.stdout + show.stderr
        
        if "Account type" in output:
            print(Fore.GREEN, "Warp account was created earlier", Style.RESET_ALL, sep='')
            return True
        
        else:
            return self.__warp_reg()
    
    
    
    def run_zapret(self):
        try:
            os.chdir(self.zp)
            subprocess.run(
                [self.z_file],
                check=True,
                )
            
            os.chdir('..')
            
            print(Fore.GREEN, "\nZapret was started", Style.RESET_ALL, sep="")
            return True
        except Exception as e:
            print(Fore.RED, f'Error {e}', Style.RESET_ALL, sep="")
            return False
        
        
    def run_warp(self):
        run = subprocess.run(
            ['warp-cli', 'connect'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if run.returncode == 0:
            print(Fore.GREEN, "Warp was connected", Style.RESET_ALL, sep='')
            return True
        else:
            print(Fore.RED, "Error warp connect", Style.RESET_ALL, sep="")
            return False
    
    
    
    def kill(self, kill_yn: bool):
        while True:
            
            if kill_yn == True:
                try:
                    subprocess.run(['warp-cli',  'disconnect'], 
                                capture_output=True)
                    subprocess.run(['taskkill', '/f', '/im', 'winws.exe'], 
                                capture_output=True)
                    
                    print(Fore.GREEN, "OBXOD process has been killed", Style.RESET_ALL, sep="")
                    break
                except Exception:
                    print(Fore.RED, "Error to kill all process", Style.RESET_ALL, sep="")
            else:
                break

