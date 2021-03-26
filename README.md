Raspberry Pi OS Downloader / Seeder
===================================

A script for ensuring that you always have the latest Raspberry Pi OS image
handy, while at the same time helping to seed the latest version for others.
This script is written specifically for Deluge users, but other torrent
clients may work too.

Run check.py regularly from cron to check the Raspberry Pi website for new
OS images, and automatically add them to your Deluge download queue.

* You need to have Deluge configured with a 'watch' directory. Any
  .torrent files that get dropped in here get automatically added
  to the download queue.
* Please seed for as long as possible. If you don't plan on seeding, just
  use the website to download your OS images, it's easier.

To configure, modify the variables in check.py accordingly:

* `watch_path`: The path that Deluge watches for new .torrent files.
* `download_path`: This is a path where torrent files are initially
  downloaded before being copied to `watch_path`. The reason is
  that Deluge deletes files in `watch_path` once it's added them
  to the download queue, and we don't want to keep downloading and
  re-adding the same file over and over again for no reason. The
  script only downloads files that do not exist in `download_path`.
* `user_agent`: This is the user agent that will be used by the script
  to call the Raspberry Pi website. Spoofing this is not essential, but
  raspberrypi.org is behind Cloudflare so it may become necessary.
