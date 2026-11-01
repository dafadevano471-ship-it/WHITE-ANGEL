import os, time

W="\033[97m"; B="\033[94m"; G="\033[92m"; Y="\033[93m"; R="\033[91m"; C="\033[96m"; RESET="\033[0m"

def banner():
    os.system("clear")
    print(f"{W}")
    print("  ██╗    ██╗██╗  ██╗██╗████████╗███████╗     █████╗ ███╗  ██╗ ██████╗ ███████╗██╗     ")
    print("  ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝    ██╔══██╗████╗ ██║██╔════╝ ██╔════╝██║     ")
    print("  ██║ █╗ ██║███████║██║   ██║   █████╗      ███████║██╔██╗██║██║  ███╗█████╗  ██║     ")
    print("  ██║███╗██║██╔══██║██║   ██║   ██╔══╝      ██╔══██║██║╚████║██║   ██║██╔══╝  ██║     ")
    print("  ╚███╔███╔╝██║  ██║██║   ██║   ███████╗    ██║  ██║██║ ╚███║╚██████╔╝███████╗███████╗")
    print("   ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚══╝ ╚═════╝ ╚══════╝╚══════╝")
    print(f"{RESET}")
    print(f"{C}   [+] CODE BY WHITE ANGEL - Defender dari Merauke, Papua [+]")
    print(f"{B}   +++[ Specially For Orang Baik, Lawan Penipu ]+++")
    print(f"{Y}   <<----------[ WHITE ANGEL MENU - v3.0 - 8 DEFENDER ]---------->>{RESET}")
    print(f"{W}   ----------------------------------------------------------------{RESET}")

def pause():
    input(f"\n{W}Tekan Enter untuk kembali...{RESET}")

def cek_link():
    print(f"\n{Y}=== [01] CEK LINK PHISING ==={RESET}")
    url=input(f"{W}Tempel link: {RESET}").lower()
    bahaya=["free-robux","robux-generator","bit.ly","tinyurl","rblx","freefire-free","diamond-gratis","login-roblox","robux88"]
    skor=sum(1 for k in bahaya if k in url)
    print(f"{C}[*] Analisa: {url}{RESET}"); time.sleep(1)
    if skor>0 or len(url)>60 or url.count("-")>3:
        print(f"{R}[!] BAHAYA! PHISING! JANGAN DIKLIK!{RESET}")
    else:
        print(f"{G}[+] AMAN - Terlihat normal, tetap hati-hati!{RESET}")
    pause()

def edukasi():
    print(f"\n{Y}=== [02] CIRI LINK PALSU ==={RESET}")
    print(f"{W}1. Gratis robux/diamond berlebihan\n2. Alamat bukan roblox.com asli\n3. Disuruh login ulang di web aneh\n4. Pakai bit.ly / tinyurl\n5. Banyak tanda - dan angka random\n{G}Asli cuma roblox.com!{RESET}")
    pause()

def tips_roblox():
    print(f"\n{C}=== [03] TIPS AMAN ROBLOX ==={RESET}")
    print(f"{W}[1] Jangan kasih password\n[2] Aktifin 2-Step Verification\n[3] Gratis robux = 99% nipu\n[4] Cek web harus roblox.com\n[5] Kalo ragu, tanya WHITE ANGEL!{RESET}")
    pause()

def lapor():
    print(f"\n{Y}=== [04] CARA LAPOR PENIPU ==={RESET}")
    print(f"{W}1. Screenshot link & chat\n2. Report Abuse di Roblox\n3. Lapor ke roblox.com/support\n4. Kasih tau teman biar gak kena{G}\nKamu pahlawan kalo lapor!{RESET}")
    pause()

def izin_cctv():
    print(f"\n{R}=== [05] CEK IZIN CCTV / KAMERA ==={RESET}")
    print(f"{W}Waspada jika website minta:{RESET}")
    print(f"{R}[!] Minta akses Kamera / Microphone tiba-tiba\n[!] Minta izin Lokasi padahal gak perlu\n[!] Pop-up 'Allow' terus menerus{RESET}")
    print(f"\n{G}=== CARA AMAN: ==={RESET}")
    print(f"{W}[1] Di Chrome HP: Titik 3 > Settings > Site Settings > Camera > Block\n[2] Jangan pernah klik 'Allow' di web mencurigakan\n[3] Cek ikon kamera di address bar, kalo nyala berarti aktif!\n[4] Penipu bisa rekam wajah kamu buat nipu!{RESET}")
    print(f"\n{Y}Tips Merauke: Kalo web robux gratis minta kamera, 100% PENIPU!{RESET}")
    pause()

def perlindungan_website():
    print(f"\n{B}=== [07] PERLINDUNGAN WEBSITE ==={RESET}")
    print(f"{W}Cara cek website aman atau tidak:{RESET}")
    print(f"{C}[*] Cek 1: Harus ada gembok (https)\n[*] Cek 2: Nama domain harus benar\n[*] Cek 3: Tidak banyak iklan pop-up\n[*] Cek 4: Umur domain baru = curiga{RESET}")
    url=input(f"\n{W}Tempel link website mau dicek: {RESET}").lower()
    print(f"{C}[*] Scan {url}...{RESET}"); time.sleep(1)
    aman=True
    if "http://" in url: print(f"{R}[!] Tidak ada HTTPS, tidak aman!{RESET}"); aman=False
    if url.count(".")>3: print(f"{R}[!] Subdomain banyak, curiga phising!{RESET}"); aman=False
    if aman: print(f"{G}[+] Website terlihat punya perlindungan dasar (HTTPS ok){RESET}")
    else: print(f"{R}[!] Website berisiko!{RESET}")
    pause()

def perlindungan_hp():
    print(f"\n{G}=== [08] PERLINDUNGAN HP DARI HACKER ==={RESET}")
    print(f"{W}8 JURUS DEFENDER MERAUKE:{RESET}")
    print(f"{C}[1] Kunci Layar: PIN 6 angka, bukan 123456\n[2] Update HP: Selalu update sistem\n[3] Aplikasi: Jangan install APK dari luar Play Store\n[4] WiFi: Jangan pakai WiFi gratis untuk login bank/game\n[5] Link: Jangan klik link sembarang (pakai menu [01])\n[6] Izin Aplikasi: Settings > Apps > Permission, matikan yang aneh\n[7] Antivirus: Play Protect aktif\n[8] Backup: Akun Roblox kaitkan email asli{RESET}")
    print(f"\n{Y}Bonus Merauke: Aktifin 'Find My Device' biar kalo hilang bisa dikunci!{RESET}")
    pause()

def scan_bocor():
    print(f"\n{C}=== [06] CEK KEBOCORAN DATA ==={RESET}")
    print(f"{W}Edukasi: Kalo pernah login di web phising, password bisa bocor!{RESET}")
    print(f"{Y}Yang harus dilakukan:{RESET}")
    print(f"{W}[1] Ganti password Roblox segera\n[2] Ganti password email yang sama\n[3] Aktifin 2 langkah verifikasi\n[4] Cek di haveibeenpwned.com{RESET}")
    pause()

while True:
    banner()
    print(f"""
 {C}[{W}01{C}] {W}Cek Link Phising
 {C}[{W}02{C}] {W}Edukasi Ciri Link Palsu
 {C}[{W}03{C}] {W}Tips Aman Roblox
 {C}[{W}04{C}] {W}Cara Lapor Penipu
 {C}[{W}05{C}] {W}Cek Izin CCTV / Kamera
 {C}[{W}06{C}] {W}Cek Kebocoran Data
 {C}[{W}07{C}] {W}Perlindungan Website
 {C}[{W}08{C}] {W}Perlindungan HP dari Hacker
 {C}[{W}00{C}] {W}Keluar
 {W}   ----------------------------------------------------------------{RESET}
""")
    pilih=input(f"{C}Select@[{W} WhiteAngel {C}]#----> {RESET}")
    if pilih in ["1","01"]: cek_link()
    elif pilih in ["2","02"]: edukasi()
    elif pilih in ["3","03"]: tips_roblox()
    elif pilih in ["4","04"]: lapor()
    elif pilih in ["5","05"]: izin_cctv()
    elif pilih in ["6","06"]: scan_bocor()
    elif pilih in ["7","07"]: perlindungan_website()
    elif pilih in ["8","08"]: perlindungan_hp()
    elif pilih in ["0","00"]: print(f"{W}Terima kasih Defender Merauke!{RESET}"); break
    else: print(f"{R}Salah pilih!{RESET}"); time.sleep(1)
