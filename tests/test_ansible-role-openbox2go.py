import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_autostart_file(File):
    f = File('/home/ansible-test-user/.config/openbox/autostart')

    assert f.exists
    assert f.user == 'ansible-test-user'
    assert f.group == 'ansible-test-user'
    assert f.is_file
    assert f.mode == 0o700


def test_bg_file(File):
    f = File('/home/ansible-test-user/.config/openbox/berlin.jpg')

    assert f.exists
    assert f.user == 'ansible-test-user'
    assert f.group == 'ansible-test-user'
    assert f.is_file
    assert f.mode == 0o700
