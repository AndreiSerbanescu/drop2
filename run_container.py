import subprocess as sb
import argparse
import yaml

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Drop2 volumetric tool")

    parser.add_argument('-s', '--source', required=True, type=str, help="Host path to source volume directory")
    parser.add_argument('-t', '--target', required=True, type=str, help="Host path to target volume directory")
    parser.add_argument('-o', '--output', required=True, type=str, help="Host path to output directory")

    args = parser.parse_args()

    with open('docker-compose.yml') as docker_compose_file:

        dc = yaml.load(docker_compose_file)

        print(dc['services']['drop2'])

        source = '{}:/home/source'.format(args.source)
        target = '{}:/home/target'.format(args.target)
        output = '{}:/home/output'.format(args.output)
        volumes = [source, target, output]
        dc['services']['drop2']['volumes'] = volumes

    new_dc_file = 'docker-compose-tmp.yml'
    with open(new_dc_file, 'w') as docker_compose_tmp_file:
        yaml.dump(dc, docker_compose_tmp_file)

    docker_compose_up_cmd = "docker-compose -f {} up --build".format(new_dc_file)
    sb.call([docker_compose_up_cmd], shell=True)

