import subprocess as sb

reg_cmd = "/home/build/drop/apps/dropreg/dropreg -s /home/source/ " \
          "-t /home/target/ " \
          "-o /home/output/output.gz.nii --ocompose -c -l --lsim 1 --ltype 2 --llevels 8 8 8 4 4 4 " \
          "--lsampling 0.1 -n --nsim 1 --nffd 80 --nlevels 8 8 8 4 4 4 4 4 4 --nlambda 0.5"

sb.call([reg_cmd], shell=True)

# seg_cmd = "/home/build/drop/apps/dropreg/dropreg " \
#           "-s <path_to_segmentation> " \
#           "-t <path_to_target> " \
#           "-o <path_to_output> " \
#           "--ointerp 0 " \
#           "--fx <path_to_field_x> " \
#           "--fy <path_to_field_y> " \
#           "--fz <path_to_field_z"
#
# sb.call([reg_cmd], shell=True)