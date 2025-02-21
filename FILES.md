# Files Description

## data/companies/
Directory containing verified company information from various sources.

### tokyo_truck_association_members.csv
A CSV file containing verified Tokyo Truck Association member companies.

Fields:
- 支部名: Branch name within the Tokyo Truck Association
- 事業者名: Company name
- verified: Website verification status (True/False)
- website: Company website URL if found

Total companies: 3,317
Source: 東京都トラック協会 会員名簿 (令和元年7月現在)
Verification: Automated website existence check with 15-second timeout per company

## tiktok_research/
Directory containing data about TikTok live streams with under 50 viewers.

### live_streams.csv
A CSV file containing information about TikTok live streamers with fewer than 50 viewers.

Fields:
- username: TikTok account username
- stream_url: Direct link to the stream
- content_genre: Type of content being streamed
- viewer_count: Number of current viewers (<50)
- timestamp: When the stream was checked
- stream_title: Title of the live stream
- language: Primary language of the stream

Total streams documented: 3

Notable observations:
- Common content types: Gaming, Entertainment, Religious content
- Peak viewer count: 42 viewers
- Time periods checked: February 13, 2025 08:40-08:55 UTC
- All observed streams were in English

## instagram_search/
Directory containing files related to Instagram account search and data collection.

### accounts_list.csv
A CSV file containing information about foreign (Western) Instagram users living in Japan.

Fields:
- username: Instagram account username
- profile_url: Direct link to the Instagram profile
- content_type: Type/genre of content posted
- followers_count: Number of followers
- location: Location in Japan
- bio_summary: Brief summary of account bio/description
- post_frequency: Posting frequency (High/Regular/Low)
- engagement_rate: Level of engagement with followers (High/Medium/Low)
- verified: Account verification status (Yes/No)

Total accounts collected: 12
Notable accounts:
- gaijinpot (2300+ followers): Information platform for foreigners in Japan
- anton.injapan (1800+ followers): Sharing Japanese festival experiences and daily life
- theblackexjp (400+ followers): 13 years of living experience in Japan
