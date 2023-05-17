#!/bin/sh

#https://symflower.com/local/install

set -eu

USE_SUDO=""
#if [ "$(id -u)" -ne 0 ]; then
#	USE_SUDO="sudo "
#fi

export OS=${OS:-"$(uname -s | awk '{print tolower($0)}')"}
export ARCH=${ARCH:-"$(uname -m)"}

DESTINATION_PATH=./symflower_related
DESTINATION_BINARY_PATH=${DESTINATION_BINARY_PATH:-"$DESTINATION_PATH/symflower"}

echo "Downloading and installing the latest binary as root to $DESTINATION_BINARY_PATH:"
$USE_SUDO mkdir -p $(dirname "$DESTINATION_BINARY_PATH")
if command -v wget > /dev/null 2>&1; then
	$USE_SUDO wget -O "$DESTINATION_BINARY_PATH" https://download.symflower.com/local/latest/symflower-$OS-$ARCH
else
	$USE_SUDO curl -SLf -o "$DESTINATION_BINARY_PATH" https://download.symflower.com/local/latest/symflower-$OS-$ARCH
fi
$USE_SUDO chmod +x "$DESTINATION_BINARY_PATH"

echo "Verifying the installation:"

SYMFLOWER_WHICH_PATH=$(which ./symflower_related/symflower)
if [ $? -ne 0 ]; then
	echo "ERROR: \"symflower\" binary cannot be found in the PATH environment variable."
	SYMFLOWER_WHICH_PATH=$DESTINATION_BINARY_PATH
fi
if [ "$SYMFLOWER_WHICH_PATH" != "$DESTINATION_BINARY_PATH" ]; then
	echo "ERROR: Expected \"symflower\" binary in $DESTINATION_BINARY_PATH but it is overwritten via the PATH environment variable with $SYMFLOWER_WHICH_PATH."
fi
"$DESTINATION_BINARY_PATH" --version

echo
echo "You can now generate unit tests with \"symflower\"!"