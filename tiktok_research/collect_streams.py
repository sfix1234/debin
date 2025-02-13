import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import csv
import os

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    return webdriver.Chrome(options=options)

def get_stream_data(driver):
    streams = []
    driver.get('https://www.tiktok.com/live')
    time.sleep(5)  # Allow page to load
    
    # Find live stream elements
    live_streams = driver.find_elements(By.CSS_SELECTOR, '[data-e2e="live-room-item"]')
    
    for stream in live_streams:
        try:
            viewer_count = int(stream.find_element(By.CSS_SELECTOR, '[data-e2e="live-room-viewer-count"]').text)
            if viewer_count >= 50:
                continue
                
            username = stream.find_element(By.CSS_SELECTOR, '[data-e2e="live-room-user-name"]').text
            stream_url = stream.find_element(By.TAG_NAME, 'a').get_attribute('href')
            title = stream.find_element(By.CSS_SELECTOR, '[data-e2e="live-room-title"]').text
            
            streams.append({
                'username': username,
                'stream_url': stream_url,
                'content_genre': 'To be classified',  # Will need manual classification
                'viewer_count': viewer_count,
                'timestamp': datetime.utcnow().isoformat(),
                'stream_title': title,
                'language': 'To be detected'  # Will need detection logic
            })
        except Exception as e:
            print(f"Error processing stream: {e}")
            continue
            
    return streams

def save_to_csv(streams, filename):
    fieldnames = ['username', 'stream_url', 'content_genre', 'viewer_count', 
                 'timestamp', 'stream_title', 'language']
    
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(streams)

def main():
    driver = setup_driver()
    try:
        while True:
            streams = get_stream_data(driver)
            if streams:
                save_to_csv(streams, 'live_streams.csv')
                print(f"Saved {len(streams)} streams")
            time.sleep(300)  # Wait 5 minutes before next check
    except KeyboardInterrupt:
        print("Data collection stopped")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
