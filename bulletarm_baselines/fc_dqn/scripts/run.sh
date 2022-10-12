#!/bin/bash

# for ((i=1;i<16;i++));do
# {
#     python test.py --load_model_pre='/home/zoooe/workspaces/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-09-19.18:34:35/models/snapshot' --env=object_grasping --num_objects=${i}
# }
# done

for ((j=0;j<8;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-10.20:06:28/models/snapshot' --env=object_grasping --object_index=${j}
}
done


for ((j=8;j<17;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-11.07:22:47/models/snapshot' --env=object_grasping --object_index=${j}
}
done

for ((j=17;j<25;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-11.18:53:52/models/snapshot' --env=object_grasping --object_index=${j}
}
done