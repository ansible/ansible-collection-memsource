# Ansible Collection - community.memsource

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![GitHub Linter](https://github.com/Spredzy/ansible-collection-memsource/workflows/Linter/badge.svg)](https://github.com/marketplace/actions/super-linter)

This collection aims to offer an Ansible native experience in order to interact and automate workflows with [Memsouce](https://www.memsource.com/). - "Helping global companies translate efficiently"

## Included content

### Modules

Name | Description
--- | ---
[memsource_import_settings](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_import_settings_info](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_job](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_job_info](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_job_targetfile](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_project](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_project_info](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_project_template](https://github.com/Spredzy/ansible-collection-memsource) |
[memsource_project_template_info](https://github.com/Spredzy/ansible-collection-memsource) |

## Installing this collection

You can install the AWS collection with the Ansible Galaxy CLI:

```sh
#> ansible-galaxy collection install community.memsource
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: community.memsource
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


You can either call modules by their Fully Qualified Collection Namespace (FQCN), such as `community.memsource.memsource_project`, or you can call modules by their short name if you list the `community.memsource` collection in the playbook's `collections` keyword:

```yaml
---
  - name: Gather all projects
    community.memsource.memsource_project_info:
      filters:
        name: Foo
    register: projects
```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Memsource collection repository](https://github.com/Spredzy/ansible-collection-memsource).

See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for more details.
