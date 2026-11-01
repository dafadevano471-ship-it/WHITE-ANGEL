# === WHITE ANGEL MERAUKE v1 - AKTIF ===
# Defender Toolkit - Dari Merauke Untuk Indonesia
# Fungsi: Cek link penipuan biar teman gak kena hack

print("=== WHITE ANGEL MERAUKE v1 - AKTIF ===")

link = input("Tempel link mencurigakan di sini: ")

jahat = ["free-robux", "rblx", "gift", "login", "verify", ".xyz", ".tk"]

ketemu = False
for j in jahat:
    if j in link.lower():
        ketemu = True

if ketemu:
    print("\n[BAHAYA!] Link ini 99% JEBAKAN PENJAHAT!")
    print("Jangan diklik! Laporkan!")
else:
    print("\n[AMAN] Link ini keliatannya bersih.")
    print("Tapi tetap hati-hati ya White Angel!")

print("\nS0 - Defender Aktif")
