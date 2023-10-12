# Ansible playbook
This playbook will install docker and deploy beyond-backend on the hosts specified in `inventory.yaml`

## Instructions
* Install ansible on your system
* Modify your `~/.ssh/config` file to be able to reach `beyond.dilt.at` with publickey and without specifying username
* Create a personal access token on GitHub and allow access to private repositories for this token
* Create an ansible vault file `vault.yaml` in this directory via `ansible-vault create vault.yaml`
  * Content should be:
    ```yaml
    ---
    vault_github_user: "<your github username>"
    vault_github_password: "<your created personal access token>"
    ```
* Run playbook via `ansible-playbook -i inventory.yaml --ask-vault-pass setup_host.yaml`
