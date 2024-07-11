# Puppet manifest for setting up a web server for deployment

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create directories
file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

# Create index.html for test release
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    Welcome to web_static!
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Manage current symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Manage ownership recursively
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file_line { 'nginx_hbnb_static_config':
  path    => '/etc/nginx/sites-available/default',
  line    => "        location /hbnb_static/ {\n                alias /data/web_static/current/;\n        }",
  match   => 'server_name _;',
  after   => 'server_name _;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['nginx_hbnb_static_config'],
}
