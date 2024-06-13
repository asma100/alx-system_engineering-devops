#ULIMIT
exec { 'set-ulimit-nginx':
  command => 'echo "ULIMIT=\\"-n 1048576\\"" > /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
  unless  => 'grep -q "ULIMIT=\\"-n 1048576\\"" /etc/default/nginx',
}

exec { 'reload-nginx':
  command     => '/usr/sbin/service nginx reload',
  path        => ['/sbin', '/usr/sbin', '/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Exec['set-ulimit-nginx'],
}
