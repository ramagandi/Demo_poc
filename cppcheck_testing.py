import argparse
import subprocess

def run_cppcheck_cmd(conf_file):
    with open(conf_file) as f:
        list_of_commands = f.read().splitlines()
    cppcheck_commands = ' '.join(list_of_commands)
    cmd = "cppcheck"+" "+cppcheck_commands
    print(cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]
    print(output)

def main():
    parser = argparse.ArgumentParser(description='test example')
    parser.add_argument('--cf', '-conffile', dest='conffile', required=True, help='Enter the configuration file path \
                         which contains the required cppcheck options')

    args = parser.parse_args()
    run_cppcheck_cmd(args.conffile)

if __name__ == "__main__":
    main()
