from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import pandas as pd

url = input('Masukkan URL Tokopedia: ')

if url:
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(3)  # Beri waktu halaman untuk load

    data = []
    
    for i in range(3):  # Loop untuk scraping 3 halaman
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        containers = soup.findAll('article', attrs={'class': 'css-ccpe8t'})
        
        for container in containers:
            try:
                review = container.find('span', attrs={'data-testid': 'lblItemUlasan'}).text.strip()
                data.append(review)  # Koreksi cara menyimpan data
            except Exception as e:  # Tangkap semua error
                print(f"Error: {e}")
                continue
        
        time.sleep(3)  # Tunggu sebelum pindah halaman

        try:
            # Menunggu tombol "Laman berikutnya" muncul sebelum klik
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label^="Laman berikutnya"]'))
            )
            next_button.click()
            time.sleep(3)  # Tunggu halaman berikutnya load
        except Exception as e:
            print("Tidak bisa menemukan tombol berikutnya atau halaman habis.")
            break  # Hentikan loop jika tidak ada tombol berikutnya

    driver.quit()  # Tutup browser setelah selesai

    print(data)
    df = pd.DataFrame(data, columns=['Ulasan'])
    df.to_csv('tokopedia.csv', index=False)
    print("Data berhasil disimpan ke tokopedia.csv")
