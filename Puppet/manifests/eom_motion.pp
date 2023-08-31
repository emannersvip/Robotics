file {'motion_service':
  ensure => present,
  path   => '/lib/systemd/system/motion.service',
}

file {'motion_binary':
  ensure => present,
  path   => '/usr/local/bin/motion', 
}

service {'motion':
  ensure => running,
}