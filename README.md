# 🕸️ Web Scraper CLI

A simple interactive command-line tool to scrape website content using Python. You can fetch raw HTML or extract specific HTML elements like `<li>` and `<div>`.

## ✨ Features

- Fetch and display full HTML from any URL
- Extract tag options
- Interactive shell interface for ease of use
- Command-line argument parsing

## 📦 Requirements

- Python 3.1+
- `requests`
- `beautifulsoup4` (for HTML parsing)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Start the interactive shell:

```bash
python scraper_shell.py
```

### Inside the shell:

| Command Example                           | Description                     |
| ----------------------------------------- | ------------------------------- |
| `scrape https://example.com`              | Fetch full HTML from URL        |
| `scrape -url https://example.com -li`     | Extract all `<li>` elements     |
| `scrape -url https://example.com -script` | Extract all `<script>` elements |
| `clear`                                   | Clear the screen                |
| `exit`                                    | Exit the CLI shell              |
| `help`                                    | Show available commands         |

## 📁 Project Structure

```
web_scraper/
├── scraper_shell.py      # Main CLI interface
├── scraper_core.py       # Core scraping functions
├── requirements.txt      # Dependencies
├── .gitignore            # Git ignore file
└── README.md             # You're here!
```

## 🔧 Example Output

```bash
scraper > scrape -url https://example.com -li
<li>First item</li>
<li>Second item</li>
...
```

## 🛡️ License

This project is licensed under the MIT License.
