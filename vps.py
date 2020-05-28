# 
# This is a application where you can automatically
# create virtual host without any hesitation.
# 

import os
print("""
                             _                    
__   ___ __  ___  __ _ _   _| |_ ___  _ __  _   _ 
\ \ / / '_ \/ __|/ _` | | | | __/ _ \| '_ \| | | |
 \ V /| |_) \__ \ (_| | |_| | || (_) | |_) | |_| |
  \_/ | .__/|___/\__,_|\__,_|\__\___/| .__/ \__, |
      |_|                            |_|    |___/ 

""")
domain = input("Domain name(For which you are gonna create virtual host): ")
os.system(f"sudo mkdir -p /var/www/{domain}/public_html")
os.system(f"sudo chown -R $USER:$USER /var/www/{domain}/public_html")
os.system("sudo chmod -R 755 /var/www")
os.system(f"sudo touch /etc/apache2/sites-available/{domain}.conf")
config = f"""
    <VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	ServerName {domain}
    ServerAlias www.{domain} 
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/{domain}/public_html
	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${{APACHE_LOG_DIR}}/error.log
	CustomLog ${{APACHE_LOG_DIR}}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

"""
with open(f'/etc/apache2/sites-available/{domain}.conf', 'w') as f:
    f.write(config)

os.system(f"sudo a2ensite {domain}.conf")
os.system("sudo a2dissite 000-default.conf")
os.system("sudo systemctl restart apache2")

print("Your Virtual host is been enabled. Now check")