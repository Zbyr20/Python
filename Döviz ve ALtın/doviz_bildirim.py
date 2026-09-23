import xml.etree.ElementTree as ET
import requests
from plyer import notification


def doviz_kurlarini_al():
    # TCMB Günlük Döviz Kurları XML Servisi
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # XML verisini ayrıştır
        root = ET.fromstring(response.content)

        # USD verisini çek
        usd = root.find("./Currency[@Kod='USD']")
        usd_alis = usd.find("ForexBuying").text if usd is not None else "N/A"

        # EUR verisini çek
        eur = root.find("./Currency[@Kod='EUR']")
        eur_alis = eur.find("ForexBuying").text if eur is not None else "N/A"

        return f"USD Alış: {usd_alis} TL\nEUR Alış: {eur_alis} TL"

    except Exception as e:                                                    
        return f"Veri alınamadı: {e}"


def bildirim_gonder():
    mesaj = doviz_kurlarini_al()

    notification.notify(
        title="💱 Anlık Döviz Kurları (TCMB)",
        message=mesaj,
        app_name="PythonHocam Döviz",
        timeout=8,  # Bildirimin ekranda kalma süresi (saniye)
    )


if __name__ == "__main__":
    bildirim_gonder()