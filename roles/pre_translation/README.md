Pre Translation Role
====================

The pre_translation role is used to push extracted strings from a GitHub project to the Memsource client for them to be translated to several other languages.

Requirements
------------

A shell script in the repository to move the translated strings and it's path to the script defined in the variable "shell_script_path"

Role Variables
--------------

Below are the mandatory variables required.
- memsource_username (Can be provided from the command-line, vars file or can be set in environment variables) - (Type: str)
- memsource_password (Can be provided from the command-line, vars file or can be set in environment variables) - (Type: str)
- translation_supported_langs - (Type: list)
- shell_script_path (Default (/tools/scripts/l18n/pre_translation.sh) - can be overridden) (Type: str)
- repo_url - (Type: str)
- repo_branch - (Type: str)
- project_name - (Type: str)
- project_template (Required: Project template dedicated to the specfic project to be translated) - (Type: int)
- preTranslate (Optional: Certain translations will be pre_translated from cached memsource database, until stated false) - (Type: bool)

Dependencies
------------

Global vars are declared in the defaults folder as main.yml which can be overridden by passing vars from the command-line or extra_vars.yml file in the collection's root folder.

Steps to create pre_translation shell Script
--------------------------------------------
- Create a pre_translation.sh file. This file will reside in the project which will be used for translation in the root path as per below
**/tools/scripts/l18n/pre_translation.sh**
Note: File can be stored in other directories as well, you need to specify the path in the var shell_script_path to override the default path for the shell script (Reference the var in the default/main.yml file)
- Add the execution commands to extract the files (e.g. po, json)
- Once the file(s) are generated, move the files to a folder (folder name: translations)

Playbook
--------

The playbook push.yml is available under playbooks/ directory will be used to run the role:

    ---
    - name: Generic Localization - Pre-translation
      hosts: localhost
      roles:
        - role: ansible.memsource.pre_translation

Execution Steps
---------------

Ansible Playbook (push.yml) will be used to run this role.

1. Provide the required variables from the command-line as per the below example \
   ```ansible-playbook playbooks/push.yml -e memsource_username=$MEMSOURCE_USERNAME -e memsource_password=$MEMSOURCE_PASSWORD -e repo_url="test_repo/prod" -e repo_branch="devel" -e project_name="Memsource Test Project" -e preTranslae=false -e project_template=310943``` \
   or \
   Another way of providing vars using the command-line can be using a separate yml file (e.g. extra_vars.yml) \
   ```ansible-playbook playbooks/push.yml -e @extra_vars.yml```

2. Extracted strings will be uploaded to the memsource cloud.

License
-------

Apache-2.0

Author Information
------------------
- Aditya Mulik (aditya.mulik@gmail.com)
