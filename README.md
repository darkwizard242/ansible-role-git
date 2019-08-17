[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-git.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-git)
![Ansible Role](https://img.shields.io/ansible/role/42239?color=dark%20green%20)
![Ansible Role](https://img.shields.io/ansible/role/d/42239?label=role%20downloads)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-git&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-git)
![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-git?label=release)
![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-git?color=orange&style=flat-square)
![GitHub language count](https://img.shields.io/github/languages/count/darkwizard242/ansible-role-git)


Ansible Role: git
=========

Role to install (_by default_) `git` package  or uninstall (_if  passed as var_)  on **Debian**, **Ubuntu** and **CentOS** systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
git_app: git
git_desired_state: present
```

Variable `git_app`: Defines the app to install i.e. **git**

Variable `git_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **git** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.git
```

For customizing behavior of role (i.e. installation of latest **git** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.git
      vars:
        git_desired_state: latest
```
             
For customizing behavior of role (i.e. un-installation of **git** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.git
      vars:
        git_desired_state: absent
```      
         
License
-------

[MIT](https://github.com/darkwizard242/ansible-role-git/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).