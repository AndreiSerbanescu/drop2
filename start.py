import subprocess as sb

reg_cmd = "/home/build/drop/apps/dropreg/dropreg -s /home/source/ " \
          "-t /home/target/ " \
          "-o /home/interm/interm.nii.gz --ocompose -c -l --lsim 1 --ltype 2 --llevels 8 8 8 4 4 4 " \
          "--lsampling 0.1 -n --nsim 1 --nffd 80 --nlevels 8 8 8 4 4 4 4 4 4 --nlambda 0.5"

seg_heart_cmd = "/home/build/drop/apps/dropreg/dropreg " \
          "-s /home/masks/mask_Heart.nii.gz  " \
          "-t /home/interm/interm.nii.gz " \
          "-o /home/output/mask_heart.nii.gz " \
          "--ointerp 0 " \
          "--fx /home/interm/interm_field_x.nii.gz " \
          "--fy /home/interm/interm_field_y.nii.gz " \
          "--fz /home/interm/interm_field_z.nii.gz"

seg_lung_l_cmd = "/home/build/drop/apps/dropreg/dropreg " \
          "-s /home/masks/mask_Lung_L.nii.gz  " \
          "-t /home/interm/interm.nii.gz " \
          "-o /home/output/mask_lung_l.nii.gz " \
          "--ointerp 0 " \
          "--fx /home/interm/interm_field_x.nii.gz " \
          "--fy /home/interm/interm_field_y.nii.gz " \
          "--fz /home/interm/interm_field_z.nii.gz"

seg_lung_r_cmd = "/home/build/drop/apps/dropreg/dropreg " \
          "-s /home/masks/mask_Lung_R.nii.gz  " \
          "-t /home/interm/interm.nii.gz " \
          "-o /home/output/mask_lung_r.nii.gz " \
          "--ointerp 0 " \
          "--fx /home/interm/interm_field_x.nii.gz " \
          "--fy /home/interm/interm_field_y.nii.gz " \
          "--fz /home/interm/interm_field_z.nii.gz"

sb.call([reg_cmd], shell=True)
sb.call([seg_heart_cmd], shell=True)
sb.call([seg_lung_l_cmd], shell=True)
sb.call([seg_lung_r_cmd], shell=True)