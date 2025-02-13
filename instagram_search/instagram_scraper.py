import requests
import pandas as pd
import json
import time
from urllib.parse import quote
import re
from bs4 import BeautifulSoup

class InstagramScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.accounts_data = []
        
    def search_hashtag(self, hashtag):
        url = f'https://www.instagram.com/explore/tags/{quote(hashtag)}/'
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                scripts = soup.find_all('script', type='text/javascript')
                for script in scripts:
                    if 'window._sharedData' in script.text:
                        json_data = script.text.split('window._sharedData = ')[1].split(';</script>')[0]
                        return json.loads(json_data)
            return None
        except Exception as e:
            print(f"Error searching hashtag {hashtag}: {str(e)}")
            return None
        
    def search_accounts(self, hashtags):
        for hashtag in hashtags:
            data = self.search_hashtag(hashtag)
            if data and 'data' in data:
                for post in data['data']['hashtag']['edge_hashtag_to_media']['edges']:
                    owner = post['node']['owner']
                    account_info = self.get_account_info(owner['username'])
                    if account_info:
                        self.accounts_data.append(account_info)
            time.sleep(2)  # Rate limiting
        return self.accounts_data
        
    def get_account_info(self, username):
        url = f'https://www.instagram.com/{username}/?__a=1'
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                data = response.json()
                user = data['graphql']['user']
                return {
                    'username': username,
                    'profile_url': f'https://www.instagram.com/{username}/',
                    'followers': user['edge_followed_by']['count'],
                    'bio': user['biography'],
                    'posts_count': user['edge_owner_to_timeline_media']['count']
                }
            return None
        except:
            return None
            
    def save_to_csv(self, accounts, filename='instagram_accounts.csv'):
        df = pd.DataFrame(accounts)
        df.to_csv(filename, index=False, encoding='utf-8')
        
    def close(self):
        self.driver.quit()
        self.display.stop()

def main():
    hashtags = ['expatjapan', 'foreignerinjapan', '日本生活', 'gaijininjapan']
    
    scraper = InstagramScraper()
    accounts = scraper.search_accounts(hashtags)
    
    if accounts:
        scraper.save_to_csv(accounts, 'instagram_accounts.csv')
        print(f"Found {len(accounts)} accounts")

if __name__ == "__main__":
    main()
