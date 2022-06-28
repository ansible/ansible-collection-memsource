# Ansible Collection - ansible.memsource

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![GitHub Linter](https://github.com/ansible/ansible-collection-memsource/workflows/Linter/badge.svg)](https://github.com/marketplace/actions/super-linter)

This collection aims to offer an Ansible native experience in order to interact and automate workflows with [Memsouce](https://www.memsource.com/). - "Helping global companies translate efficiently"

## Included content

### Modules

Name | Description
--- | ---
[memsource_import_settings](./plugins/modules/memsource_import_settings.py) | Manage a Memsource import settings configuration
[memsource_import_settings_info](./plugins/modules/memsource_import_settings_info.py) | List all available Memsource import settings configurations
[memsource_job](./plugins/modules/memsource_job.py) | Manage a Memsource job
[memsource_job_info](./plugins/modules/memsource_job_info.py) | List all Memsource job
[memsource_job_targetfile](./plugins/modules/memsource_job_targetfile.py) | Download a Memsource job target file
[memsource_project](./plugins/modules/memsource_project.py) | Manage a Memsource project
[memsource_project_info](./plugins/modules/memsource_project_info.py) | List all Memsource projects available
[memsource_project_template_info](./plugins/modules/memsource_project_template_info.py) | List all Memsource project templates available

### Roles
Name | Description
--- | ---
[pre_translation](./roles/pre_translation) | Role to extract strings from a project and upload to Memsource
[post_translation](./roles/post_translation) | Role to pull translated strings from Memsource and push to the respective project

**Note: Please read the requirements of each Role's README.md before executing the role**

## Installing this collection

You can install the memsource collection with the Ansible Galaxy CLI:

```sh
#> ansible-galaxy collection install ansible.memsource
```

To install directly from GitHub:

```sh
#> ansible-galaxy collection install git@github.com:ansible/ansible-collection-memsource.git
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ansible.memsource
```

The python module dependencies are not installed by `ansible-galaxy`.  They can
be manually installed using pip:

```sh
#> pip install requirements.txt
```

or:

```sh
pip install python-memsource
```

## Using this collection


You can either call modules by their Fully Qualified Collection Namespace (FQCN), such as `ansible.memsource.memsource_project`, or you can call modules by their short name if you list the `ansible.memsource` collection in the playbook's `collections` keyword:

```yaml
---
  - name: Get recent project
    ansible.memsource.memsource_project_info:
      project_name: "Foo"
    register: project
```

## Authentication

There are two supported ways for a user to authenticate with the Memsource API:

* Using the environment variables `$MEMSOURCE_USERNAME` and `$MEMSOURCE_PASSWORD`
* Using the per task level configuration modules `memsource_username` and `memsource_password`

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Memsource collection repository](https://github.com/ansible/ansible-collection-memsource).

See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for more details.
