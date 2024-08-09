

# YouTube Comments and Replies Scraper

This project is a Python-based tool that fetches comments and replies from YouTube videos using the YouTube Data API v3 and stores them in a SQLite database. The scraper allows you to analyze and store data for further analysis or use in other applications.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Fetches top-level comments and their replies from any YouTube video.
- Stores comments and replies in separate SQLite databases.
- Handles pagination and retrieves all available comments and replies.
- Provides a modular and extensible code structure.

## Requirements

- Python 3.6+
- `google-api-python-client`
- `pandas`
- `SQLAlchemy`

## Installation


    ```

1. Obtain a YouTube Data API key by following the instructions [here](https://developers.google.com/youtube/v3/getting-started).

2. Save your API key in a `key.json` file:

    ```json
    {
        "api": "YOUR_YOUTUBE_API_KEY"
    }
    ```

## Usage

1. Run the script and enter the YouTube video ID when prompted:

    ```bash
    python youtube_scraper.py
    ```

2. The script will fetch the comments and replies and store them in SQLite databases named `comments.db` and `replies.db`.

3. You can query the databases using any SQLite-compatible tools or libraries.

## Project Structure

- `youtube_scraper.py`: Main script that runs the data pipeline.
- `key.json`: File containing your YouTube API key.
- `requirements.txt`: List of Python dependencies.

## Configuration

- The database name and other configurations can be modified directly in the `youtube_scraper.py` script.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to fork this repository, create a feature branch, and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Google API Python Client](https://github.com/googleapis/google-api-python-client) - For the YouTube Data API integration.
- [Pandas](https://pandas.pydata.org/) - For data manipulation and analysis.
- [SQLAlchemy](https://www.sqlalchemy.org/) - For database management.

---

Feel free to modify the README to better fit your project specifics, and replace placeholders like `"yourusername"` with your actual GitHub username.
