import feedparser
from datetime import datetime, timedelta


def fetch_all_rss(url):
    # Fetch and return all RSS feed entries
    feed = feedparser.parse(url)
    return feed.feed.title, feed.feed.description, feed.entries


def get_latest_rss(url, since=24):
    """
    Returns RSS entries published in the last 'since' hours.

    :param url: URL of the RSS feed.
    :param since: Time range in hours to filter entries. Defaults to 24 hours.
    :return: List of recent RSS entries.
    """
    # Fetch all RSS entries
    title, description, entries = fetch_all_rss(url)

    # Get the current time and calculate the threshold time (since the specified hours)
    current_time = datetime.now()
    threshold_time = current_time - timedelta(hours=since)

    # List to store entries from the last 'since' hours
    recent_entries = []

    # Iterate through all entries and check if they are within the last 'since' hours
    for entry in entries:
        # Ensure the entry has a 'published' field and handle it
        if 'published' in entry:
            # Convert 'published' field to datetime
            pub_date = datetime(*entry.published_parsed[:6])  # Convert time tuple to datetime object

            # Check if the published date is within the last 'since' hours
            if pub_date > threshold_time:
                recent_entries.append(entry)

    return title, description, recent_entries
