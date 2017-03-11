master: [![Build Status](https://travis-ci.org/avnes/ansible-role-openbox2go.png?branch=master)](https://travis-ci.org/avnes/ansible-role-openbox2go) develop: [![Build Status](https://travis-ci.org/avnes/ansible-role-openbox2go.png?branch=develop)](https://travis-ci.org/avnes/ansible-role-openbox2go)


# ansible-role-openbox2go

Install openbox and make it ready to use with Plank, Tint2 and Conky.

## Requirements

Requires Xorg to be installed for making openbox usable.

In order to continuously develop and test this role, you will need docker, pip, molecule, testinfra and python-docker-py installed.

```
pip install molecule
pip install testinfra
```

## Role Variables

### defaults/main.yml
```
config_owner:
  Type: String
  Default: "{{ ansible_user_id }}"

config_owner_primary_group:
  Type: String
  Default: "{{ config_owner }}"

bg_autostart:
  Type: Boolean
  Default: True

bg_picture:
  Type: String
  Default: "{{ config_dir }}/berlin.jpg"

bg_command:
  Type: String
  Default: feh --bg-fill "{{ bg_picture }}"

conky_autostart:
  Type: Boolean
  Default: True

nm_applet_autostart:
  Type: Boolean
  Default: True

plank_autostart:
  Type: Boolean
  Default: True

scim_autostart:
  Type: Boolean
  Default: True

screensaver_autostart:
  Type: Boolean
  Default: True

screensaver_command:
  Type: String
  Default: 'xautolock -time 10 -locker slock'

terminal_autostart:
  Type: Boolean
  Default: True

terminal_command:
  Type: String
  Default: lxterminal

tint2_autostart:
  Type: Boolean
  Default: True

software_list:
  Type: List
  Default:
    - { name: 'feh', state: 'present' }
    - { name: 'scim', state: 'present' }
    - { name: 'lxterminal', state: 'present' }
    - { name: 'xautolock', state: 'present' }

software_xtra_debian_family:
  Type: List
  Default:
    - { name: 'network-manager', state: 'present' }

software_xtra_ubuntu_family:
  Type: List
  Default:
    - { name: 'network-manager', state: 'present' }

software_xtra_redhat_family:
  Type: List
  Default:
    - { name: 'network-manager-applet', state: 'present' }

software_xtra_arch_family:
  Type: List
  Default:
    - { name: 'network-manager-applet', state: 'present' }

arch_software_list:
  Type: List
  Default: "{{ software_list }} + {{ software_xtra_arch_family }}"

debian_software_list:
  Type: List
  Default: "{{ software_list }} + {{ software_xtra_debian_family }}"

fedora_software_list:
  Type: List
  Default: "{{ software_list }} + {{ software_xtra_redhat_family }}"

ubuntu_software_list:
  Type: List
  Default: "{{ software_list }} + {{ software_xtra_ubuntu_family }}"
```

### vars/main.yml
```
config_dir:
  Type: String
  Default: "~{{ config_owner }}/.config/openbox"

autostart_file:
  Type: String
  Default: "{{ config_dir }}/autostart"
```

## Dependencies

### Installation
```
ansible-galaxy install -r requirements.yml
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
