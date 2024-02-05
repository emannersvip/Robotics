# Build New Ubuntu host 2021
# Change: Update for 2024
#
$user    = 'emanners'
$homedir = "/home/$user"
$codedir = "$homedir/Code"

file { "$homedir/Code":         ensure => directory, owner => $user, group => $user }

#--
package { 'htop':  ensure => installed, }
package { 'iotop':  ensure => installed, }
package { 'mlocate':  ensure => installed, }
package { 'screen':  ensure => installed, }
# https://forum.level1techs.com/t/how-to-reformat-520-byte-drives-to-512-bytes-usually/133021
# package { 'sg3-utils': ensure => installed, }
package { 'smartmontools':  ensure => installed, }

#--Miscellaneous files
#
#--Vim
package { 'vim':  ensure => installed, }
file { "$homedir/.vimrc":
  ensure        => present,
  owner         => $user,
  group         => $user,
  content       => "colorscheme darkblue\nsyntax on",
}
