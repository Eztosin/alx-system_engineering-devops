# Increase the ULIMIT of the default file
file { '/etc/default/nginx':
  ensure  => file,
  content => "#This file is managed by puppet\n\nULIMIT=\"-n 4096\"\n",
  notify  => Exec['restart_nginx'],
}

# Restart Nginx
exec { 'restart_nginx':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
}
