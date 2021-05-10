master: [![Build Status](https://travis-ci.org/avnes/ansible-role-openbox2go.png?branch=master)](https://travis-ci.org/avnes/ansible-role-openbox2go) develop: [![Build Status](https://travis-ci.org/avnes/ansible-role-openbox2go.png?branch=develop)](https://travis-ci.org/avnes/ansible-role-openbox2go)

# ansible-role-openbox2go

Install openbox and make it ready to use with Plank, Tint2 and Conky.

## Requirements

Requires Xorg to be installed for making openbox usable.

## Role Variables

### defaults/main.yml

```yaml
config_owner:
  Type: String
  Default: "{{ ansible_user_id }}"
  Description: The name of the Linux user owning the Openbox configuration.

config_owner_primary_group:
  Type: String
  Default: "{{ config_owner }}"
  Description: The primary group of the Linux user owning the Openbox configuration.

xkb_options:
  Type: Boolean
  Default: True
  Description: Used to set keyboard configuration in Xorg. See https://wiki.archlinux.org/index.php/Keyboard_configuration_in_Xorg for more info.

xkb_command:
  Type: String
  Default: 'setxkbmap -layout "dk"'
  Description: The command to set keyboard configuration in Xorg.

bg_autostart:
  Type: Boolean
  Default: True
  Description: Set a background image at login.

bg_picture:
  Type: String
  Default: "{{ config_dir }}/berlin.jpg"
  Description: The location of the background image.

bg_command:
  Type: String
  Default: feh --bg-fill "{{ bg_picture }}"
  Description: The command to set a background image.

conky_autostart:
  Type: Boolean
  Default: True
  Description: Launch conky at login.

nm_applet_autostart:
  Type: Boolean
  Default: True
  Description: Launch network-manager at login.

plank_autostart:
  Type: Boolean
  Default: True
  Description: Launch plank dock at login.

scim_autostart:
  Type: Boolean
  Default: True
  Description: Launch scim to add support for non-English languages.

screensaver_autostart:
  Type: Boolean
  Default: True
  Description: Launch dormant screen saver at login.

screensaver_command:
  Type: String
  Default: 'xautolock -time 10 -locker slock'
  Description: The command to run the screen saver.

terminal_autostart:
  Type: Boolean
  Default: True
  Description: Launch a terminal at login.

terminal_command:
  Type: String
  Default: lxterminal
  Description: The command to launch a terminal at login.

tint2_autostart:
  Type: Boolean
  Default: True
  Description: Launch tint2 dock at login.

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

```yaml
config_dir:
  Type: String
  Default: "~{{ config_owner }}/.config/openbox"

autostart_file:
  Type: String
  Default: "{{ config_dir }}/autostart"
```

## Dependencies

### Installation

```yaml
ansible-galaxy install -r requirements.yml -p tests/roles -f
```

## Example Playbook

```yaml
- hosts: all
  vars:
    config_owner: "emma"
    config_owner_primary_group: "{{ config_owner }}"
  roles:
     - { role: ansible-role-openbox2go }
```

## Test

```
virtualenv ~/.virtualenv/ansible-role-openbox2go
source ~/.virtualenv/ansible-role-openbox2go/bin/activate
pip install -r requirements.txt
molecule test
```

## License

MIT

## Author Information

<https://github.com/avnes>
