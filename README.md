# InstaCrawler

InstaCrawler is an automated tool for scraping Instagram user data using Selenium and BeautifulSoup. It can log in to Instagram, retrieve lists of followers and following, and identify users who do not follow you back. The automation is designed to mimic human browser behavior to avoid detection.

## Features

- Automated login to Instagram (manual login supported)
- Scrape followers and following lists
- Identify users not following you back
- Uses Microsoft Edge WebDriver for browser automation
- Configurable scraping cadence and browser profile

## Requirements

- Python 3.8+
- Microsoft Edge browser
- Microsoft Edge WebDriver (`msedgedriver.exe`)
- Instagram account

## Installation

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd InstaCrawler
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables**  
   Edit the `.env` file to set the paths for your Edge user data directory and WebDriver, and adjust scraping parameters if needed.

   Example:
   ```
   NAVIGATOR_DATA_DIR_OF_USER=C:\Users\<YourUser>\AppData\Local\Microsoft\Edge\User Data\Default
   NAVIGATOR_WEBDRIVER_PATH=D:\path\to\msedgedriver.exe
   TIMES_TO_SCROLL_DOWN_USER_CONTAINER=25
   SECONDS_TO_WAIT_AFTER_SCROLL=0.1
   SECONDS_TO_WAIT_FOR_USERS_CONTAINER_TO_LOAD=1.5
   ```

## Usage

Run the main script with one of the available commands:

```sh
python main.py <order>
```

### Available Orders

- `help` — Show usage information
- `manual_login` — Open Instagram and allow you to log in manually
- `not_following_back` — Retrieve and print users you follow who do not follow you back

### Example

```sh
python main.py manual_login
# Log in to Instagram in the opened browser window, then close it.

python main.py not_following_back
# The script will print the list of users not following you back.
```

## Project Structure

- `main.py` — Entry point for the CLI
- `app/` — Application logic and command definitions
- `entities/` — Data models and selectors
- `marionette/` — Browser automation classes
- `.env` — Environment configuration
- `requirements.txt` — Python dependencies

## Notes

- The script uses your existing Edge browser profile for authentication.
- Instagram UI changes may require updates to selectors in [`entities/InstagramSelectors.py`](entities/InstagramSelectors.py).
- Use responsibly and respect Instagram's terms of service.

## License

MIT