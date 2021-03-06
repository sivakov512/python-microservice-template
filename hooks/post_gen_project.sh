#!/usr/bin/env bash

git init -b master .

{% if cookiecutter.proto_repository | trim != "" -%}
git submodule add {{ cookiecutter.proto_repository }} proto
{%- endif %}

git add ./

git remote add origin {{ cookiecutter.git_repo_ssh }}
git fetch

echo -e '\nOkay...'
echo 'Now look at the README in your new project and follow instructions.'
echo -e "Don't forget to star template!\nhttps://github.com/sivakov512/python-microservice-template"
