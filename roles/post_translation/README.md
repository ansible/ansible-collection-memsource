Post Translation Role
=====================

The post_translation role is used to pull translated strings from the Memsource client for the specified languages, commit them, and push those strings back to the code repository.

Requirements
------------

1. GitHub CLI (<https://cli.github.com/>) | GitHub CLI needs to be installed on the machine running the role for creating a pull request
2. A shell script in the repository to move the translated strings and it's path to the script defined in the variable "shell_script_path"

Role Variables
--------------

Below are the mandatory variables required.
- memsource_username (Can be provided from the command-line, vars file or can be set in environment variables) - (Type: str)
- memsource_password (Can be provided from the command-line, vars file or can be set in environment variables) - (Type: str)
- github_username - (Type: str)
- repo_url - (Type: str)
- repo_branch - (Type: str)
- fork_repo_url - (Type: str) (Please note, a fork of the main repository URL should already be present for the github_username specified)
- languages - (Type: list)
- shell_script_path (Default (/tools/scripts/l18n/post_translation.sh) - can be overridden) (Type: str)
- project_name - (Type: str) (Optional: Either pass project_name or project_uid)
- project_uid - (Type: int) (Optional) - (WARNING: Do not include in pre_translation role as it will
fail)
- github_token - (Type: str) (Optional: GitHub Authentication can be done using SSH)

Dependencies
------------

- The pre_translation role should already be executed for the latest strings to be translated and be available on the Memsource portal for the post_translation script to work
- Global vars are declared in the defaults folder as main.yml which can be overridden by passing vars from the command-line or extra_vars.yml file in the collection's root folder

Steps to create post_translation shell Script
--------------------------------------------
- Create a post_translation.sh file. This file will reside in the project which will be used for translation in the root path as per below e.g.
**/tools/scripts/l18n/post_translation.sh**
Note: The file can be stored in other directories as well, you need to specify the path in the var shell_script_path to override the default path for the shell script (Reference the var in the default/main.yml file)
- A translations folder will be provided with all the translated strings retrieved from Memsource (folder name: translations)\
  Translation folder with all language generated files will be in below format\
  e.g.\
      /translations/fr/django.po\
      /translations/jp/django.po\
      /translations/ko/django.po\
      /translations/ko/messages.po
- Add the logic to move the files to the desired location where the new translated strings should reside, further the playbook would create a Pull Request for the updated strings.

Playbook
--------

The playbook pull.yml is available under playbooks/ directory will be used to run the role:

    ---
    - name: Generic Localization - Post-translation
      hosts: localhost
      roles:
        - role: ansible.memsource.post_translation

Execution Steps
---------------

An Ansible Playbook (pull.yml) will be used to run this role.

1. Provide the required variables from the command-line as per the below example \
    ```ansible-playbook playbooks/pull.yml -e memsource_username=$MEMSOURCE_USERNAME -e memsource_password=$MEMSOURCE_PASSWORD -e repo_url="test_repo/prod" -e repo_branch="devel" -e project_name="MEMSOURCE TRANSLATION PROJECT V2.1"``` \
    or \
    Another way of providing vars using the command-line can be using a separate yml file (e.g. extra_vars.yml, template is available on the root path) \
    ```ansible-playbook playbooks/pull.yml -e @extra_vars.yml```

2. A pull request will be generated in the repository for merging the translated strings

License
-------

Apache-2.0

Author Information
------------------
- Aditya Mulik (aditya.mulik@gmail.com)
