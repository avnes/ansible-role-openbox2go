master: [![Build Status](https://travis-ci.org/avnes/ansible-role-openbox2go.png?branch=master)](https://travis-ci.org/avnes/ansible-role-openbox2go) develop: [![Build Status](https://travis-ci.org/avnes/ansible-role-openbox2go.png?branch=develop)](https://travis-ci.org/avnes/ansible-role-openbox2go)


# ansible-role-openbox2go

Install openbox and make it ready to use with Plank, Tint2 and Conky.

## Requirements

Requires Xorg to be installed for making openbox usable.

In order to continuously develop and test this role, you will need docker, pip, molecule, testinfra and python-docker-py installed.

Install docker, pip and python-docker-py with your distributions package manager. Then install molecule and tesinfra with pip:

```
pip install molecule
pip install testinfra
```

## Role Variables

```
config_owner:
  String (mandatory) to specify the Linux user that should have conky setup for them.
  Default: "{{ ansible_user_id }}"

config_owner_primary_group:
  String (optional) to specify the primary group of the Linux user to own the openbox configuration.
  Default: "{{ config_owner }}"
```

## Dependencies

### Installation
```
ansible-galaxy install -r requirements.yml
```

### Usage
```
vars:
  config_owner: "{{ ansible_user_id }}"
  config_owner_primary_group: "{{ config_owner }}"
roles:
  - { role: avnes.ansible-role-conky }
  - { role: avnes.ansible-role-openbox2go }
  - { role: avnes.ansible-role-tint2 }
```

## Example Playbook

```
- hosts: all
  vars:
    config_owner: "emma"
    config_owner_primary_group: "{{ config_owner }}"
  roles:
     - { role: ansible-role-openbox2go }
```

## Test

```
ansible-galaxy install -r requirements.yml -p tests/roles
molecule create
molecule test
```

## License

MIT

## Author Information

<https://github.com/avnes>
