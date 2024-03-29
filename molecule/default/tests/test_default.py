import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/var/lib/slurm_exporter"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    files = [
        "/etc/systemd/system/slurm_exporter.service",
        "/usr/local/bin/prometheus-slurm-exporter"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_user(host):
    assert host.group("slurm-exp").exists
    assert "slurm-exp" in host.user("slurm-exp").groups
    assert host.user("slurm-exp").shell == "/usr/sbin/nologin"
    assert host.user("slurm-exp").home == "/"


def test_service(host):
    s = host.service("slurm_exporter")
#    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:9100"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
