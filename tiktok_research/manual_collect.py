from datetime import datetime
import csv
import os

def add_stream_entry(username: str, viewer_count: int, title: str, genre: str = "Unknown", language: str = "Unknown"):
    """Add a single stream entry to the CSV file"""
    stream_data = {
        'username': username,
        'stream_url': f'https://www.tiktok.com/@{username}/live',
        'content_genre': genre,
        'viewer_count': viewer_count,
        'timestamp': datetime.utcnow().isoformat(),
        'stream_title': title,
        'language': language
    }
    
    filename = 'live_streams.csv'
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(stream_data.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(stream_data)
    print(f"Added stream: {username} - {viewer_count} viewers")

if __name__ == "__main__":
    print("TikTok Live Stream Data Collection Tool")
    print("Enter stream information (Ctrl+C to exit):")
    
    try:
        while True:
            username = input("\nUsername: ").strip()
            if not username:
                continue
                
            try:
                viewer_count = int(input("Viewer count: "))
                if viewer_count >= 50:
                    print("Skipping: Viewer count >= 50")
                    continue
            except ValueError:
                print("Invalid viewer count. Please enter a number.")
                continue
                
            title = input("Stream title: ").strip()
            genre = input("Content genre (or press Enter for Unknown): ").strip() or "Unknown"
            language = input("Language (or press Enter for Unknown): ").strip() or "Unknown"
            
            add_stream_entry(username, viewer_count, title, genre, language)
            
    except KeyboardInterrupt:
        print("\nData collection completed.")
