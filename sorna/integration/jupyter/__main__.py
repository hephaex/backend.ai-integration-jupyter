import argparse
import sys
from ipykernel.kernelapp import IPKernelApp
from . import kernel


custom_args_start = sys.argv.index('--')
parser = argparse.ArgumentParser()
parser.add_argument('-k', '--kernel', type=str)
args = parser.parse_args(sys.argv[custom_args_start + 1:])

kernel_class = getattr(kernel, args.kernel)
IPKernelApp.launch_instance(kernel_class=kernel_class)
