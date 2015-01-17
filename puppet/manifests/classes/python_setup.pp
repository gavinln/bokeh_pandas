# Install python and compiled modules for project
class python_setup {
    case $operatingsystem {
        ubuntu: {
            package { "python-pip":
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
#            package { ["python-zmq", "python-scipy"]:
#                ensure => installed,
#                require => Package['python-pip']
#            }
#            package { ['libfreetype6-dev', 'pkg-config']:
#                ensure => installed
#            }
#            package { ['pyparsing']:
#                ensure => installed,
#                provider => pip,
#                require => Package['python-pip']
#            }
#            package { ["matplotlib"]:
#                ensure => installed,
#                provider => pip,
#                require => Package['numpy', 'pyparsing', 'libfreetype6-dev']
#            }
#            package { 'virtualenv':
#                ensure => installed,
#                provider => pip,
#                require => Package['python-pip']
#            }
#            package { 'untangle':
#                ensure => installed,
#                provider => pip,
#                require => Package['virtualenv']
#            }
#            package { 'yolk':
#                ensure => installed,
#                provider => pip,
#                require => Package['virtualenv']
#            }
#            package { 'pygments':
#                ensure => installed,
#                provider => pip,
#                require => Package['virtualenv']
#            }
#            package { 'nose':
#                ensure => installed,
#                provider => pip,
#                require => Package['virtualenv']
#            }
#            package { 'tornado':
#                ensure => installed,
#                provider => pip,
#                require => Package['virtualenv']
#            }
#            package { 'pandas':
#                ensure => installed,
#                provider => pip,
#                require => Package['numpy']
#            }
#            package { 'seaborn':
#                ensure => installed,
#                provider => pip,
#                require => Package['matplotlib']
#            }
        }
    }
}
