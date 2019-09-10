#!/bin/bash

set -euo pipefail

export GOPATH=~/go

tox -- molecule test --all

