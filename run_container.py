import subprocess as sb
import argparse
import yaml
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Drop2 volumetric tool")

    parser.add_argument('-t', '--target', required=True, type=str, help="Host path to target volume directory")
    parser.add_argument('-o', '--output', required=True, type=str, help="Host path to output directory")
    parser.add_argument('-s', '--source', default="", type=str, help="(Optional) Host path to source volume directory")
    parser.add_argument('-m', '--mask', default="", type=str, help="(Optional) Host path to source mask directory")
    parser.add_argument('--with-mask-segmentation', action='store_true', help="Select this to only perform registration")
    parser.add_argument('--debug', action='store_true', help="Select this for container to not perform any computation")

    args = parser.parse_args()

    with open('docker-compose.yml') as docker_compose_file:

        dc = yaml.load(docker_compose_file)

        print(dc['services']['drop2'])

        target = '{}:/home/target'.format(args.target)
        output = '{}:/home/output'.format(args.output)

        volumes = [target, output]

        if args.source != "":
            volumes.append('{}:/home/source'.format(args.source))

        if args.mask != "":
            volumes.append('{}:/home/mask'.format(args.mask))

        dc['services']['drop2']['volumes'] = volumes

        if args.debug:
            dc['services']['drop2']['command'] = 'tail -F anything'

        environment = ["DEBUG={}".format(args.debug), "WITH_MASK_SEGMENTATION={}".format(args.with_mask_segmentation)]

        old_env = dc['services']['drop2'].get('environment', [])
        dc['services']['drop2']['environment'] = environment + old_env

        print(dc['services']['drop2']['environment'])

    new_dc_file = 'docker-compose-tmp.yml'

    if os.path.exists(new_dc_file):
        os.remove(new_dc_file)

    with open(new_dc_file, 'w') as docker_compose_tmp_file:
        yaml.dump(dc, docker_compose_tmp_file)

    docker_compose_up_cmd = "docker-compose down --volumes " \
                            "&& docker-compose -f {} up --build".format(new_dc_file)
    sb.call([docker_compose_up_cmd], shell=True)

