#!/usr/bin/env python3

import os

def check_reboot():
	"""returns true for pending reboot"""
	return os.path.exist("/run/reboot-required")

def main():
	pass

main()
