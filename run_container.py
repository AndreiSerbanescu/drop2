import subprocess as sb
import argparse
import yaml
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Drop2 volumetric tool")

    parser.add_argument('-t', '--target', required=True, type=str, help="Host path to target volume directory")
    parser.add_argument('-o', '--output', required=True, type=str, help="Host path to output directory")

    args = parser.parse_args()

    with open('docker-compose.yml') as docker_compose_file:

        dc = yaml.load(docker_compose_file)

        print(dc['services']['drop2'])

        target = '{}:/home/target'.format(args.target)
        output = '{}:/home/output'.format(args.output)

        volumes = [target, output]

        dc['services']['drop2']['volumes'] = volumes

    new_dc_file = 'docker-compose-tmp.yml'

    if os.path.exists(new_dc_file):
        os.remove(new_dc_file)

    with open(new_dc_file, 'w') as docker_compose_tmp_file:
        yaml.dump(dc, docker_compose_tmp_file)

    docker_compose_up_cmd = "docker-compose down --volumes " \
                            "&& docker-compose -f {} up --build".format(new_dc_file)
    sb.call([docker_compose_up_cmd], shell=True)

