#Using Puppet to install flask from pip3

$package = 'flask'

package { $package:
    ensure   => '2.1.0',
    provider => 'pip3',
}