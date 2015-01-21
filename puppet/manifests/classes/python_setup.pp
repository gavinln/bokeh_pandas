# Install python and compiled modules for project
class python_setup {
    case $operatingsystem {
        ubuntu: {
            package { "python-pip":
                ensure => installed
            }
            package { "python-scipy":
                ensure => installed
            }
            package { "numpy":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { "flask":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { "requests":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { "gevent":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { "gevent-websocket":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { "redis":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { "pandas":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { "bokeh":
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'ipython':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'vincent':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
        }
    }
}
