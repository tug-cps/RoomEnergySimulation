# Ansible playbook to help with initial docker setup

## Instructions
* Install ansible on your system
* Modify your `~/.ssh/config` file to be able to reach `beyond.dilt.at` with publickey and without specifying username
* Run playbook via `ansible-playbook -i inventory.yaml setup_host.yaml`
