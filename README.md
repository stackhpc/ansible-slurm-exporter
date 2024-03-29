<p><img src="https://www.circonus.com/wp-content/uploads/2015/03/sol-icon-itOps.png" alt="graph logo" title="graph" align="right" height="60" /></p>

# Ansible Role: prometheus slurm exporter

[![Build Status](https://travis-ci.com/stackhpc/ansible-slurm-exporter.svg?branch=master)](https://travis-ci.org/stackhpc/ansible-slurm-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-stackhpc.slurm_exporter-blue.svg)](https://galaxy.ansible.com/stackhpc/slurm-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/stackhpc/ansible-slurm-exporter.svg)](https://github.com/stackhpc/ansible-slurm-exporter/tags)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23stackhpc-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#stackhpc)

## Description

Deploy prometheus [slurm exporter](https://github.com/vpenso/prometheus-slurm-exporter) using ansible.

## Requirements

- Ansible >= 2.6 (It might work on previous versions, but we cannot guarantee it)
- gnu-tar on Mac deployer host (`brew install gnu-tar`)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `slurm_exporter_version` | "0.8"    | Slurm exporter package version. Also accepts latest as parameter. |
| `slurm_exporter_web_listen_address` | "0.0.0.0:9100" | Address on which node exporter will listen |
| `slurm_exporter_system_group` | "slurm-exp" | System group used to run slurm_exporter |
| `slurm_exporter_system_user` | "slurm-exp" | System user used to run slurm_exporter |

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - stackhpc.slurm-exporter
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip3 install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py35-ansible28 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
