Autogenerated Cloudflare IP rules for Nginx
=============================================================

See [https://www.cloudflare.com/ips/](https://www.cloudflare.com/ips/)

Installation
------------------

This script requires Python 3 installed.

1. Clone repo on your server. For exaple to /usr/local/nginx-cloudflare.

	git clone https://bitbucket.org/lafayette/nginx-cloudflare.git /usr/local/nginx-cloudflare

2. Check if everything is ok and create initial cloudflare.conf file:

	./nginx-cloudflare.py --config config.ini

3. Link crontab script:

	ln -s /usr/local/nginx-cloudflare/nginx-cloudflare.cron /etc/cron.d/nginx-cloudflare

4. Include cloudflare.conf from nginx scripts (server block):

	include /usr/local/nginx-cloudflare/cloudflare.conf;

You could change the output path and Cloudflare URLs in config.ini.
