file {'motion_service':
  ensure  => present,
  path    => '/lib/systemd/system/motion.service',
  #content => template('motion.service.erb'),
  source  => 'puppet:///motion.service',
}

file {'motion_binary':
  ensure => present,
  path   => '/usr/local/bin/motion',
  source => 'puppet:///PiSurveillanceCamera.py',
}

service {'motion':
  ensure     => running,
  hasrestart => true,
  hasstatus  => true,
  require    => File['motion_service'],
}