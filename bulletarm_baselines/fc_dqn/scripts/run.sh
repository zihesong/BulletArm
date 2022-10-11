#!/bin/bash

# for ((i=1;i<16;i++));do
# {
#     python test.py --load_model_pre='/home/zoooe/workspaces/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-09-19.18:34:35/models/snapshot' --env=object_grasping --num_objects=${i}
# }
# done

for ((j=1;j<86;j++));do
{
    python test.py --load_model_pre='/home/zoooe/workspaces/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-09-19.18:34:35/models/snapshot' --env=object_grasping --object_index=${j}
}
done
