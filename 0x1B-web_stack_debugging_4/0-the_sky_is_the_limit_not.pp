# Increase the amountnn of traffic an Nginx server can handle.

# Increase the ULINIT of the default file
exec {	'fix--for-nginx':
  # Modify the ULINIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specify the path for the sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  # Restart Nginx services
  command => '/etc/init.d/nginx restart',
  # Specify the path for the innit.
  path    => '/etc/init.d/',
}
