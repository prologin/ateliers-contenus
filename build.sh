#!/usr/bin/env bash

set -xeuo pipefail

pushd themes/prologin

./build.sh
./compile_resources.sh

popd
