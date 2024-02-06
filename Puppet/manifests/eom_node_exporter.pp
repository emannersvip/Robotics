#

$node_exporter = 'node_exporter-1.7.0.linux-amd64.tar.gz'
$url = "https://github.com/prometheus/node_exporter/releases/download/v1.7.0/${node_exporter}"

#package { 'htop':  ensure => installed, }
#package { 'vim':  ensure => installed, }

file { 'node_exporter_service':
  ensure        => present,
  path		=> '/etc/systemd/system/node_exporter.service',
  owner         => root,
  group         => root,
  source        => 'file:///profile/node_exporter/node_exporter.service',
  require	=> Exec['node_exporter_binary'],
}
exec { 'node_exporter_binary':
  path		=> '/usr/bin',
  command       => "wget -c ${url} -O - | tar zx",
  creates	=> '/home/emanners/Code/Robotics/Puppet/manifests/node_exporter-1.7.0.linux-amd64',
}
service { 'node_exporter':
  ensure	=> running,
  enable	=> true,
  hasrestart	=> true,
  hasstatus	=> true,
  require	=> [Exec['node_exporter_binary'], File['node_exporter_service']],
}


