# Project Structure

## Directories
- `data/` - Contains all data files
  - `companies/` - Company information files
    - `company_list.csv` - Main company information database

## File Descriptions
### company_list.csv
CSV file containing company information with the following columns:
- 会社名: Company name
- 所在地: Location
- 売上規模: Sales scale (10-300億 range)
- 担当部署: Department (if known)
- メールアドレス: Email address (highest priority)
- 電話番号: Phone number (optional)
- 問い合わせフォームURL: Contact form URL (optional)
- 備考: Notes

File encoding: UTF-8
