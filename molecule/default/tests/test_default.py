import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'git'
PACKAGE_BINARY = '/usr/bin/git'


def test_git_package_installed(host):
    """
    Tests if git package is in installed state.
    """
    assert host.package(PACKAGE).is_installed


def test_git_binary_exists(host):
    """
    Tests if git binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_git_binary_file(host):
    """
    Tests if git binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_git_binary_which(host):
    """
    Tests the output to confirm git's binary location.
    """
    assert host.check_output('which git') == PACKAGE_BINARY
