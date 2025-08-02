# 📸 InstaCrawler

**InstaCrawler** is your automated sidekick for scraping Instagram user data using Selenium 4.34.2 and BeautifulSoup 4.12.2!  
It logs in, grabs your followers/following lists, and spots who’s not following you back — all while mimicking real human browsing to stay under the radar. 🕵️‍♂️

---

## ✨ Features

- 🤖 Automated (or manual) Instagram login
- 📋 Scrape followers & following lists
- 🚦 Find out who’s not following you back
- 🖥️ Uses Microsoft Edge WebDriver for browser automation
- ⚙️ Customizable scraping speed & browser profile

---

## 🛠️ Requirements

- Python 3.8+
- Microsoft Edge browser
- Microsoft Edge WebDriver (`msedgedriver.exe`)
- Instagram account

---

## 🚀 Installation

1. **Clone the repo**
   ```sh
   git clone <your-repo-url>
   cd InstaCrawler
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables**  
   Edit the `.env` file to set your Edge user data directory, WebDriver path, and scraping parameters.

   Example:
   ```
   NAVIGATOR_DATA_DIR_OF_USER=C:\Users\<YourUser>\AppData\Local\Microsoft\Edge\User Data\Default
   NAVIGATOR_WEBDRIVER_PATH=D:\path\to\msedgedriver.exe
   TIMES_TO_SCROLL_DOWN_USER_CONTAINER=25
   SECONDS_TO_WAIT_AFTER_SCROLL=0.1
   SECONDS_TO_WAIT_FOR_USERS_CONTAINER_TO_LOAD=1.5
   ```

---

## 🏁 Usage

Run the main script with a command:

```sh
python main.py <order>
```

### 📚 Available Orders

- `help` — Show usage info
- `manual_login` — Open Instagram for manual login
- `not_following_back` — List users you follow who don’t follow you back

### 💡 Example

```sh
python main.py manual_login
# Log in to Instagram in the opened browser window, then close it.

python main.py not_following_back
# See who’s not following you back!
```

---

## 🗂️ Project Structure

- `main.py` — CLI entry point
- `app/` — App logic & commands
- `entities/` — Data models & selectors
- `marionette/` — Browser automation
- `.env` — Config file
- `requirements.txt` — Python dependencies

---

## ⚠️ Notes

- Uses your existing Edge browser profile for authentication.
- Instagram UI changes may require updates to selectors in [`entities/InstagramSelectors.py`](entities/InstagramSelectors.py).
- Use responsibly and respect Instagram’s terms of service! 🙏

---

## 📄 License

MIT
