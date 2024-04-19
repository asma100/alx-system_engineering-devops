#kill
exec { 'killmenow':
  command => '/bin/pkill -9 killmenow',
}
