import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


GIT_BINARY_PATH = '/usr/bin/git'
PACKAGE = 'git'


def test_git_package_installed(host):
    host.package("PACKAGE").is_installed


def test_git_binary_exists(host):
    host.file('GIT_BINARY_PATH').exists


def test_git_binary_file(host):
    host.file('GIT_BINARY_PATH').is_file


def test_git_binary_whereis(host):
    host.check_output('whereis git') == GIT_BINARY_PATH
