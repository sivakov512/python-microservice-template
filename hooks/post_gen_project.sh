#!/usr/bin/env bash

git init -b master .

{% if cookiecutter.proto_repository | trim != "" -%}
git submodule add {{ cookiecutter.proto_repository }}
{%- endif %}

echo 'Okay...'
echo 'Now install python dependencies with "poetry install"'
