import requests
import os
import urllib.parse
from bs4 import BeautifulSoup
import time
import sys
import random
from colorama import init, Fore, Back, Style

init()  # Initialize colorama

class BlueSecAnimation:
    @staticmethod
    def show_intro():
        print(Fore.BLUE + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣴⣶⣾⣿⣿⣾⣷⣦⣤⣿⣶⣶⣤⣄⣀⢤⡀⠀⠀⠀⠀⢰⣴⣶⣷⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣀⣀⣤⣤⣶⣶⣶⣦⣤⠤    
⠠⠔⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠂⠀⠀
⠀⠀⠀⠘⠋⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⢻⣿⣿⣿⣿⡏⠀⠀⠀⢀⣤⣾⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠀⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠛⠟⠋⣿⣿⡿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠋⠙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⠀⠸⠋⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⠋⠛⠇⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⢀⣿⣿⠁⠀⠈⢻⣿⣿⣿⣿⣿⡿⠋⠈⣿⣿⡏⠃⠀⠘⣿⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡏⠀⠀⠀⠈⣿⣿⣿⣿⣿⠀⠀⠀⠸⣿⣇⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⣼⣿⣿⣿⣿⣿⡄⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀By ph3lixxx⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠋⠉⠉⠛⠉⠋⠻⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣷⣄⠀⠀⠀ Bye Bye <3⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⡇⠙⠀⠀⠀⢸⠋⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⢿⣷⡢⡀⠀⠀⢀⣰⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⠀⠁⠁⠀⠀⠀⠀⠉⢠⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⢸⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⠀⠀⠀⠀⠘⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀
        """ + Style.RESET_ALL)
        
        print(Fore.CYAN + "=== THE POWER IS INVISIBLE ===")
        print("=== BlueSec Security ===" + Style.RESET_ALL)
        time.sleep(1)
        
    @staticmethod
    def show_loading():
        animations = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        for i in range(15):
            time.sleep(0.1)
            sys.stdout.write("\r" + Fore.BLUE + "Penyesalan itu datang terakhir!! " + animations[i % len(animations)] + " " + Style.RESET_ALL)
            sys.stdout.flush()
        print("\n")

    @staticmethod
    def show_success():
        print(Fore.GREEN + """
  ____  _   _  ____  _____   _____ ___ _   _ ___ 
 / ___|| | | |/ ___|| ____| |  ___|_ _| \ | |_ _|
 \___ \| | | | |    |  _|   | |_   | ||  \| || | 
  ___) | |_| | |___ | |___  |  _|  | || |\  || | 
 |____/ \___/ \____||_____| |_|   |___|_| \_|___|
        """ + Style.RESET_ALL)

class WaybackDownloader:
    def __init__(self):
        self.file_types = {
            '1': {'ext': ['pdf'], 'desc': 'PDF Documents'},
            '2': {'ext': ['doc', 'docx'], 'desc': 'Word Documents'},
            '3': {'ext': ['xls', 'xlsx'], 'desc': 'Excel Files'},
            '4': {'ext': ['ppt', 'pptx'], 'desc': 'PowerPoint Files'},
            '5': {'ext': ['html', 'htm'], 'desc': 'Web Pages'},
            '6': {'ext': ['txt', 'csv'], 'desc': 'Text Files'},
            '7': {'ext': ['jpg', 'jpeg', 'png', 'gif'], 'desc': 'Images'},
            '8': {'ext': ['zip', 'rar', 'tar', 'gz'], 'desc': 'Archive Files'},
            '9': {'ext': ['js', 'css', 'json', 'xml'], 'desc': 'Code Files'},
            '10': {'ext': ['env', 'conf', 'config', 'bak'], 'desc': 'Configuration Files'}
        }
        self.social_links = {
            'github': 'https://github.com/ph3lixxx',
            'youtube': 'https://www.youtube.com/@ph3lixxx',
            'telegram': 'https://t.me/ph3lixxx'
        }

    def show_social_links(self):
        print(Fore.YELLOW + "\n=== Follow Kami ===")
        print(f"GitHub: {self.social_links['github']}")
        print(f"YouTube: {self.social_links['youtube']}")
        print(f"Telegram: {self.social_links['telegram']}")
        print("="*30 + Style.RESET_ALL)

    def show_menu(self):
        print(Fore.CYAN + "\nPilih jenis dokumen yang ingin diunduh:" + Style.RESET_ALL)
        for key, value in self.file_types.items():
            print(Fore.BLUE + f"{key}. {value['desc']} ({', '.join(value['ext'])})" + Style.RESET_ALL)
        print(Fore.GREEN + "11. Unduh SEMUA jenis dokumen" + Style.RESET_ALL)
        print(Fore.RED + "0. Keluar" + Style.RESET_ALL)

    def get_selected_extensions(self, choices):
        extensions = []
        if '11' in choices:
            # Select all extensions
            for item in self.file_types.values():
                extensions.extend(item['ext'])
            return extensions
        
        for choice in choices:
            if choice in self.file_types:
                extensions.extend(self.file_types[choice]['ext'])
        return extensions

    def get_wayback_urls(self, domain, extensions):
        cdx_url = "https://web.archive.org/cdx/search/cdx"
        params = {
            'url': f"{domain}/*",
            'matchType': 'domain',
            'output': 'json',
            'fl': 'original,timestamp',
            'filter': 'statuscode:200',
            'collapse': 'digest'
        }
        
        try:
            response = requests.get(cdx_url, params=params)
            response.raise_for_status()
            results = response.json()
            
            filtered_urls = []
            for entry in results[1:]:  # Skip header
                url = entry[0].lower()
                if any(url.endswith(f".{ext}") for ext in extensions):
                    timestamp = entry[1]
                    wayback_url = f"https://web.archive.org/web/{timestamp}/{entry[0]}"
                    filtered_urls.append((entry[0], wayback_url))
            
            return filtered_urls
        
        except Exception as e:
            print(Fore.RED + f"Error fetching URLs: {e}" + Style.RESET_ALL)
            return []

    def download_file(self, url, wayback_url, output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            filename = os.path.basename(urllib.parse.urlparse(url).path)
            if not filename:
                filename = f"file_{int(time.time())}"
            
            # Sanitize filename
            filename = "".join(c for c in filename if c.isalnum() or c in ('.', '-', '_'))
            
            filepath = os.path.join(output_dir, filename)
            
            if os.path.exists(filepath):
                print(Fore.YELLOW + f"File exists, skipping: {filename}" + Style.RESET_ALL)
                return
            
            print(Fore.BLUE + f"Downloading: {filename}" + Style.RESET_ALL)
            
            response = requests.get(wayback_url, stream=True)
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            
            # For HTML files, download assets
            if any(filename.endswith(f".{ext}") for ext in ['html', 'htm']):
                self.download_html_assets(url, wayback_url, os.path.dirname(filepath))
            
            time.sleep(0.5)  # Be polite to the server
        
        except Exception as e:
            print(Fore.RED + f"Failed to download {url}: {e}" + Style.RESET_ALL)

    def download_html_assets(self, original_url, wayback_url, output_dir):
        try:
            response = requests.get(wayback_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            assets_dir = os.path.join(output_dir, "assets")
            os.makedirs(assets_dir, exist_ok=True)
            
            for tag in soup.find_all(['link', 'script', 'img']):
                asset_url = None
                if tag.name == 'link' and tag.get('rel') == ['stylesheet']:
                    asset_url = tag.get('href')
                elif tag.name == 'script':
                    asset_url = tag.get('src')
                elif tag.name == 'img':
                    asset_url = tag.get('src')
                
                if asset_url and not asset_url.startswith(('http', '//')):
                    parsed = urllib.parse.urlparse(original_url)
                    base_url = f"{parsed.scheme}://{parsed.netloc}"
                    asset_url = urllib.parse.urljoin(base_url, asset_url)
                    
                    timestamp = wayback_url.split('/web/')[1].split('/')[0]
                    asset_wayback_url = f"https://web.archive.org/web/{timestamp}/{asset_url}"
                    
                    self.download_file(asset_url, asset_wayback_url, assets_dir)
        
        except Exception as e:
            print(Fore.RED + f"Error downloading assets: {e}" + Style.RESET_ALL)

    def run(self):
        BlueSecAnimation.show_intro()
        self.show_social_links()
        
        print(Fore.GREEN + "Inisialisasi sistem downloader..." + Style.RESET_ALL)
        BlueSecAnimation.show_loading()
        
        domain = input(Fore.CYAN + "\nMasukkan domain target (contoh: example.com): " + Style.RESET_ALL).strip()
        output_dir = input(Fore.CYAN + "Masukkan direktori output (default: wayback_downloads): " + Style.RESET_ALL).strip()
        output_dir = output_dir if output_dir else "wayback_downloads"
        
        while True:
            self.show_menu()
            choices = input(Fore.CYAN + "\nMasukkan pilihan (pisahkan dengan koma untuk memilih banyak): " + Style.RESET_ALL).strip().split(',')
            
            if '0' in choices:
                print(Fore.RED + "\nKeluar dari program." + Style.RESET_ALL)
                self.show_social_links()
                return
            
            selected_extensions = self.get_selected_extensions([c.strip() for c in choices])
            
            if not selected_extensions:
                print(Fore.RED + "\nPilihan tidak valid. Silakan coba lagi." + Style.RESET_ALL)
                continue
            
            print(Fore.BLUE + f"\nMemulai pencarian untuk: {', '.join(selected_extensions)}" + Style.RESET_ALL)
            
            # Animasi loading
            print(Fore.BLUE + "Memindai Wayback Machine..." + Style.RESET_ALL)
            BlueSecAnimation.show_loading()
            
            urls = self.get_wayback_urls(domain, selected_extensions)
            
            if not urls:
                print(Fore.RED + "\nTidak ditemukan file yang cocok." + Style.RESET_ALL)
                continue
            
            print(Fore.GREEN + f"\nMenemukan {len(urls)} file. Mulai mengunduh..." + Style.RESET_ALL)
            
            for original_url, wayback_url in urls:
                self.download_file(original_url, wayback_url, output_dir)
            
            BlueSecAnimation.show_success()
            print(Fore.GREEN + "\nProses selesai. File disimpan di:", os.path.abspath(output_dir) + Style.RESET_ALL)
            self.show_social_links()
            
            another = input(Fore.CYAN + "\nApakah Anda ingin mengunduh jenis dokumen lain dari domain yang sama? (y/n): " + Style.RESET_ALL).lower()
            if another != 'y':
                break

if __name__ == "__main__":
    try:
        downloader = WaybackDownloader()
        downloader.run()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nProgram dihentikan oleh pengguna." + Style.RESET_ALL)
        downloader.show_social_links()
    except Exception as e:
        print(Fore.RED + f"\nError: {e}" + Style.RESET_ALL)
        downloader.show_social_links()
