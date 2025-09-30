import json
import pandas as pd

# Gantilah ini dengan JSON kamu, atau simpan di file dan baca dari file jika terlalu panjang
data_json = {
"warna": [
    {
      "nama": "Brave Pink",
      "kode_warna": {
        "hex": "#FF69B4",
        "rgb": "255,105,180"
      },
      "simbolisasi": "keberanian",
      "media_representasi": ["poster", "banner", "kaos", "feed media sosial"],
      "respon_publik": "positif"
    },
    {
      "nama": "Hero Green",
      "kode_warna": {
        "hex": "#008000",
        "rgb": "0,128,0"
      },
      "simbolisasi": "kepahlawanan",
      "media_representasi": ["mural", "hashtag", "feed media sosial"],
      "respon_publik": "netral"
    },
    {
      "nama": "Calm Blue",
      "kode_warna": {
        "hex": "#0000FF",
        "rgb": "0,0,255"
      },
      "simbolisasi": "ketenangan",
      "media_representasi": ["banner", "poster", "feed media sosial"],
      "respon_publik": "positif"
    },
    {
      "nama": "Sunshine Yellow",
      "kode_warna": {
        "hex": "#FFD700",
        "rgb": "255,215,0"
      },
      "simbolisasi": "keceriaan",
      "media_representasi": ["kaos", "poster", "banner"],
      "respon_publik": "positif"
    },
    {
      "nama": "Passion Red",
      "kode_warna": {
        "hex": "#FF0000",
        "rgb": "255,0,0"
      },
      "simbolisasi": "semangat",
      "media_representasi": ["mural", "feed media sosial", "kaos"],
      "respon_publik": "positif"
    },
    {
      "nama": "Peace White",
      "kode_warna": {
        "hex": "#FFFFFF",
        "rgb": "255,255,255"
      },
      "simbolisasi": "kedamaian",
      "media_representasi": ["poster", "banner", "kaos"],
      "respon_publik": "positif"
    },
    {
      "nama": "Mystery Black",
      "kode_warna": {
        "hex": "#000000",
        "rgb": "0,0,0"
      },
      "simbolisasi": "misteri",
      "media_representasi": ["mural", "feed media sosial"],
      "respon_publik": "netral"
    },
    {
      "nama": "Hope Orange",
      "kode_warna": {
        "hex": "#FFA500",
        "rgb": "255,165,0"
      },
      "simbolisasi": "harapan",
      "media_representasi": ["banner", "kaos", "poster"],
      "respon_publik": "positif"
    },
    {
      "nama": "Trust Blue",
      "kode_warna": {
        "hex": "#1E90FF",
        "rgb": "30,144,255"
      },
      "simbolisasi": "kepercayaan",
      "media_representasi": ["feed media sosial", "poster", "banner"],
      "respon_publik": "positif"
    },
    {
      "nama": "Energy Red",
      "kode_warna": {
        "hex": "#DC143C",
        "rgb": "220,20,60"
      },
      "simbolisasi": "energi",
      "media_representasi": ["kaos", "mural", "feed media sosial"],
      "respon_publik": "positif"
    },
    {
      "nama": "Nature Green",
      "kode_warna": {
        "hex": "#228B22",
        "rgb": "34,139,34"
      },
      "simbolisasi": "alam",
      "media_representasi": ["mural", "poster", "banner"],
      "respon_publik": "positif"
    },
    {
      "nama": "Royal Purple",
      "kode_warna": {
        "hex": "#800080",
        "rgb": "128,0,128"
      },
      "simbolisasi": "kebangsawanan",
      "media_representasi": ["kaos", "feed media sosial"],
      "respon_publik": "netral"
    },
    {
      "nama": "Fresh Cyan",
      "kode_warna": {
        "hex": "#00FFFF",
        "rgb": "0,255,255"
      },
      "simbolisasi": "kesegaran",
      "media_representasi": ["banner", "poster", "feed media sosial"],
      "respon_publik": "positif"
    },
    {
      "nama": "Warm Brown",
      "kode_warna": {
        "hex": "#A52A2A",
        "rgb": "165,42,42"
      },
      "simbolisasi": "kehangatan",
      "media_representasi": ["kaos", "mural"],
      "respon_publik": "netral"
    },
    {
      "nama": "Bright Lime",
      "kode_warna": {
        "hex": "#32CD32",
        "rgb": "50,205,50"
      },
      "simbolisasi": "semangat muda",
      "media_representasi": ["poster", "feed media sosial"],
      "respon_publik": "positif"
    },
    {
      "nama": "Soft Lavender",
      "kode_warna": {
        "hex": "#E6E6FA",
        "rgb": "230,230,250"
      },
      "simbolisasi": "ketenangan",
      "media_representasi": ["banner", "kaos"],
      "respon_publik": "positif"
    },
    {
      "nama": "Bold Maroon",
      "kode_warna": {
        "hex": "#800000",
        "rgb": "128,0,0"
      },
      "simbolisasi": "kekuatan",
      "media_representasi": ["mural", "poster"],
      "respon_publik": "netral"
    },
    {
      "nama": "Clear Sky Blue",
      "kode_warna": {
        "hex": "#87CEEB",
        "rgb": "135,206,235"
      },
      "simbolisasi": "kebebasan",
      "media_representasi": ["feed media sosial", "banner"],
      "respon_publik": "positif"
    },
    {
      "nama": "Gentle Pink",
      "kode_warna": {
        "hex": "#FFC0CB",
        "rgb": "255,192,203"
      },
      "simbolisasi": "kelembutan",
      "media_representasi": ["kaos", "poster"],
      "respon_publik": "positif"
    },
    {
      "nama": "Electric Blue",
      "kode_warna": {
        "hex": "#7DF9FF",
        "rgb": "125,249,255"
      },
      "simbolisasi": "inovasi",
      "media_representasi": ["feed media sosial", "banner"],
      "respon_publik": "positif"
    },
    {
      "nama": "Deep Sea Blue",
      "kode_warna": {
        "hex": "#003366",
        "rgb": "0,51,102"
      },
      "simbolisasi": "kedalaman",
      "media_representasi": ["mural", "poster"],
      "respon_publik": "netral"
    },
    {
      "nama": "Bright Coral",
      "kode_warna": {
        "hex": "#FF7F50",
        "rgb": "255,127,80"
      },
      "simbolisasi": "keceriaan",
      "media_representasi": ["kaos", "banner"],
      "respon_publik": "positif"
    },
    {
      "nama": "Soft Mint",
      "kode_warna": {
        "hex": "#98FF98",
        "rgb": "152,255,152"
      },
      "simbolisasi": "kesegaran",
      "media_representasi": ["poster", "feed media sosial"],
      "respon_publik": "positif"
    },
    {
      "nama": "Dark Slate Gray",
      "kode_warna": {
        "hex": "#2F4F4F",
        "rgb": "47,79,79"
      },
      "simbolisasi": "ketegasan",
      "media_representasi": ["mural", "kaos"],
      "respon_publik": "netral"
    },
    {
      "nama": "Goldenrod",
      "kode_warna": {
        "hex": "#DAA520",
        "rgb": "218,165,32"
      },
      "simbolisasi": "kemakmuran",
      "media_representasi": ["banner", "poster"],
      "respon_publik": "positif"
    },
    {
      "nama": "Bright Turquoise",
      "kode_warna": {
        "hex": "#40E0D0",
        "rgb": "64,224,208"
      },
      "simbolisasi": "kreativitas",
      "media_representasi": ["feed media sosial", "kaos"],
      "respon_publik": "positif"
    }
  ]
}


# Ekstraksi data menjadi list of dict (format datar)
rows = []
for item in data_json["warna"]:
    row = {
        "Nama": item["nama"],
        "Hex": item["kode_warna"]["hex"],
        "RGB": item["kode_warna"]["rgb"],
        "Simbolisasi": item["simbolisasi"],
        "Media Representasi": ", ".join(item["media_representasi"]),
        "Respon Publik": item["respon_publik"]
    }
    rows.append(row)

# Konversi ke DataFrame
df = pd.DataFrame(rows)

# Simpan ke file Excel
df.to_excel("warna_output.xlsx", index=False)

print("Data berhasil diekspor ke warna_output.xlsx")
