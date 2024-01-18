#

file { '/var/www/html/wp-settings.php':
  ensure => file,
}

exec { 'find-class':
  command => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin:/usr/bin',
  require => File['/var/www/html/wp-settings.php'],
}